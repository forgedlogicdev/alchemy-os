#!/usr/bin/env bash
set -euo pipefail

# ═══════════════════════════════════════════════════════════════
# ALCHEMYOS SETUP — Run once after fresh Bazzite install on Ally
# ═══════════════════════════════════════════════════════════════

RED='\033[0;31m'; BLUE='\033[0;34m'; GREEN='\033[0;32m'; NC='\033[0m'
echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}    A L C H E M Y O S   S E T U P           ${NC}"
echo -e "${BLUE}============================================${NC}"

if [ "$EUID" -ne 0 ]; then
    echo "Run as root: sudo bash setup.sh"
    exit 1
fi

ALCHEMY="/var/alchemy"
mkdir -p /var/alchemy

# ── 1. Mount the sacred partition ──────────────────────────
echo -e "\n${BLUE}[1/7]${NC} Mounting sacred partition..."
if ! mountpoint -q /var/alchemy; then
    mount /dev/disk/by-label/alchemy_data /var/alchemy || \
    mount /dev/sdb4 /var/alchemy
fi
echo "UUID=$(blkid -s UUID -o value /dev/sdb4) /var/alchemy btrfs defaults,noatime 0 2" >> /etc/fstab
echo -e "${GREEN}  Mounted.${NC}"

# ── 2. Install system packages via rpm-ostree ──────────────
echo -e "\n${BLUE}[2/7]${NC} Layering packages..."
rpm-ostree install -y \
    python3 python3-pip python3-devel \
    python3-numpy python3-pillow python3-psutil \
    python3-sounddevice portaudio-devel \
    ollama flite \
    git curl wget \
    tailscale \
    pipewire pipewire-alsa \
    qt5-qtbase-devel python3-qt5 \
    hidapi python3-pyusb \
    ffmpeg \
    openssl openssl-devel || true
echo -e "${GREEN}  Packages layered (reboot may be needed).${NC}"

# ── 3. Install Python dependencies ─────────────────────────
echo -e "\n${BLUE}[3/7]${NC} Installing Python packages..."
pip install --break-system-packages \
    streamdeck Pillow inputs sounddevice numpy psutil \
    pyusb cryptography flask requests pyperclip || true
echo -e "${GREEN}  Python deps installed.${NC}"

# ── 4. Install Stream Deck udev rules ──────────────────────
echo -e "\n${BLUE}[4/7]${NC} Setting up Stream Deck Neo..."
cat > /etc/udev/rules.d/99-streamdeck.rules << 'UDEV'
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="009a", MODE="0666"
KERNEL=="hidraw*", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="009a", MODE="0666"
UDEV
udevadm control --reload-rules && udevadm trigger
echo -e "${GREEN}  Stream Deck rules installed.${NC}"

# ── 5. Configure Ollama ────────────────────────────────────
echo -e "\n${BLUE}[5/7]${NC} Starting Ollama..."
systemctl enable --now ollama 2>/dev/null || true
sleep 2
ollama pull llama3.2 2>/dev/null || echo "  (pull later with ollama pull llama3.2)"
echo -e "${GREEN}  Ollama configured.${NC}"

# ── 6. Deploy systemd services ─────────────────────────────
echo -e "\n${BLUE}[6/7]${NC} Installing systemd services..."
cp /var/alchemy/systemd/*.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable alchemy-audio.service
systemctl enable alchemy-visualizer.service
systemctl enable alchemy-os.service
systemctl enable alchemy-p2p.service
echo -e "${GREEN}  Services installed and enabled.${NC}"

# ── 7. Configure P2P node ──────────────────────────────────
echo -e "\n${BLUE}[7/7]${NC} Configuring P2P mesh..."
mkdir -p ~/.config/alchemy
cat > ~/.config/alchemy/p2p_config.json << 'JSON'
{
    "node_id": "alchemy-ally",
    "password": "CHANGE_ME_ALCHEMY_P2P",
    "capabilities": ["gpu", "ai", "storage", "display", "audio"],
    "tailscale": true
}
JSON
echo -e "${RED}  ! EDIT ~/.config/alchemy/p2p_config.json with your real password !${NC}"

# ── P2P hotspot config (offline fallback) ──────────────────
cat > /var/alchemy/scripts/enable_mesh_hotspot.sh << 'HOTSPOT'
#!/bin/bash
nmcli dev wifi hotspot ifname wlan0 ssid "AlchemyOS-Mesh" password "alchemy_mesh_key" 2>/dev/null || \
nmcli dev wifi hotspot ifname wlp1s0 ssid "AlchemyOS-Mesh" password "alchemy_mesh_key"
HOTSPOT
chmod +x /var/alchemy/scripts/enable_mesh_hotspot.sh

echo ""
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}    ALCHEMYOS SETUP COMPLETE                 ${NC}"
echo -e "${GREEN}============================================${NC}"
echo ""
echo "  Next steps:"
echo "  1. Edit ~/.config/alchemy/p2p_config.json"
echo "  2. Start Tailscale: sudo tailscale up"
echo "  3. Reboot (rpm-ostree layered packages need it)"
echo "  4. Stream Deck Neo should light up on next boot"
echo ""
echo "  Offline mode: sudo bash /var/alchemy/scripts/enable_mesh_hotspot.sh"
echo "  Start now:    sudo systemctl start alchemy-os.service"
echo ""
