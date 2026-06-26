# AlchemyOS Architecture

## System Topology

```
LAYER 1: HARDWARE
┌─────────────────────────────────────────────────────────────────────┐
│  ROG Ally         HP Mini          Pixel 10 Pro    M3Tab    Nuu+   │
│  AMD Z1E          Intel x86        Tensor G5       ARM      MT6580 │
│  16GB RAM         8GB RAM          12GB RAM        3GB RAM  2GB RAM│
│  RDNA3 GPU        Headless         Adreno GPU      Mali     Mali   │
│  RTL8852BE WiFi   AIC8800D80 WiFi  WiFi 7          WiFi 5   WiFi 4│
│  StreamDeckUSB    ✗                ✗               ✗        ✗      │
└─────────────────────────────────────────────────────────────────────┘

LAYER 2: OPERATING SYSTEM
┌─────────────────────────────────────────────────────────────────────┐
│  Bazzite          Linux Mint       Android+Termux  Android  Android │
│  (Fedora Ostree)  (Debian base)    (crDroid)       (Stock)  (LOS)  │
│  kernel-ally      kernel-generic   kernel-android  stock     custom│
│  Gamescope        Headless         Termux:Boot     ✗        ✗      │
│  PipeWire         ✗                ✗               ✗        ✗      │
└─────────────────────────────────────────────────────────────────────┘

LAYER 3: P2P MESH (alchemy_p2p.py)
┌─────────────────────────────────────────────────────────────────────┐
│  Discovery:   Tailscale MagicDNS + mDNS + UDP broadcast (port 8888) │
│  Transport:   WireGuard (online) / Raw TCP (LAN)                   │
│  Auth:        AES-256-GCM challenge/response handshake             │
│  Port:        45999 (TCP)                                          │
│  Heartbeat:   Every 10s, mark offline after 30s                    │
│  Messages:    JSON over encrypted TCP socket                       │
└─────────────────────────────────────────────────────────────────────┘

LAYER 4: APPLICATION SERVICES
┌─────────────────────────────────────────────────────────────────────┐
│  Visualizer Engine  AI Inference     AI Companion    VNC Client     │
│  alchemy_os.py      Ollama:11434     Glyph daemon    AllyDroid      │
│  StreamDeck Bridge  SD Server:7860   FlyCode client  Cyber Monitor  │
│  Audio FFT:9993     Proxy:7879       ✗               ✗              │
│  WebGL Forge:8000   OpenCode:4096    ✗               ✗              │
└─────────────────────────────────────────────────────────────────────┘
```

## Port Map

| Port | Protocol | Device | Service |
|---|---|---|---|
| 22 | TCP | Ally, Mini | SSH |
| 45999 | TCP | All nodes | AlchemyOS P2P mesh |
| 8888 | UDP | All nodes | LAN autodiscovery beacon |
| 8080 | UDP (localhost) | Ally | Engine → StreamDeck LCD images |
| 8081 | UDP (localhost) | Ally | StreamDeck → Engine key events |
| 8082 | UDP (localhost) | Ally | Engine → Chat GUI responses |
| 9993 | UDP (localhost) | Ally | Audio FFT band data |
| 9994 | UDP (localhost) | Ally | Audio command channel |
| 9995 | UDP (localhost) | Ally | Synth engine commands |
| 8000 | TCP | Ally | Visualizer Forge HTTP/WebRTC |
| 11434 | TCP | Ally, Mini | Ollama API |
| 7860 | TCP | Mini | Stable Diffusion API |
| 7879 | TCP | Mini | Glyph DeepSeek proxy |
| 5000 | TCP | Mini | Cyber Monitor Flask API |
| 5001 | TCP | Mini | ADIA Chat server |
| 6080 | TCP | Mini | noVNC WebSocket |
| 4096 | TCP | Mini | OpenCode server (FlyCode) |
| 5900 | TCP | Ally, Mini | VNC (wayvnc / krfb / x11vnc) |
| 5555 | TCP | Pixel | ADB over TCP |

## Boot Chain (ROG Ally)

```
systemd boot sequence:
  1. aic8800.service            (WiFi driver loader, oneshot)
  2. tailscaled.service         (VPN mesh)
  3. NetworkManager-wait-online (ensure connectivity)
  4. ollama.service             (local LLM)
  5. alchemy-p2p.service        (mesh node daemon)
  6. alchemy-audio.service      (PipeWire FFT capture → UDP 9993)
  7. alchemy-visualizer.service (Stream Deck Neo render engine)
  8. alchemy-os.service         (core engine, alchemy_os.py)
```

## Boot Chain (HP Mini)

```
systemd boot sequence:
  1. aic8800.service            (WiFi driver loader, oneshot)
  2. tailscaled.service         (VPN mesh)
  3. NetworkManager-wait-online (ensure connectivity)
  4. ollama.service             (local LLM)
  5. glyph-sd-server.service    (Stable Diffusion)
  6. glyph-proxy.service        (DeepSeek API relay)
  7. alchemy-p2p.service        (mesh node daemon)
  8. opencode.service           (AI coding server for FlyCode)
```

## Data Flow: VJ Performance (Offline Mode)

```
StreamDeck Neo ──HID──► alchemy_os.py (Ally) ──UDP──► daemon.py ──USB──► Neo LCD
                              │
                    Audio FFT (PipeWire) ──UDP──► visualizer shaders
                              │
                    P2P ──► HP Mini (Ollama backfill for Adia AI)
                              │
                    WebRTC ──► M3Tab / Nuu+ (wireless audience display)
```

## Data Flow: AI Companion Mode

```
Pixel 10 Pro ──P2P──► HP Mini ──Ollama──► LLM response ──P2P──► Pixel
    │                                       │
    │  glyph_daemon.py                      │  Stable Diffusion
    │  (user chat)                          │  (image generation)
    │                                       │
    └──P2P──► HP Mini ──SD API──► generated image ──P2P──► Pixel
```

## Data Flow: Mobile Coding (FlyCode)

```
Pixel 10 Pro ──HTTP+SSE──► HP Mini ──opencode serve──► AI agent loop
  (FlyCode app)              (port 4096)                 (code gen, diff, build)
```

## Persistent Storage Layout

```
/var/alchemy/              (ROG Ally, Btrfs, survives OS reinstalls)
├── engine/                alchemy_os.py, daemon.py, renderer.py
├── shaders/               GLSL/WGSL shader vault
├── visualizers/           WebGL forge, Vulkan engine
├── audio/                 FFT feeder, synth engine configs
├── ai/                    Adia memory, Ollama configs
├── recordings/            VJ session captures (WebM)
├── p2p/                   Mesh node config + peer keys
└── presets/               VJ presets, sequencer patterns

/opt/alchemy/              (HP Mini, survives OS reinstalls)
├── ollama/                Models + config
├── sd-server/             Stable Diffusion models + output
├── glyph-proxy/           DeepSeek relay + config
├── opencode/              Coding server + session data
└── p2p/                   Mesh node config + peer keys
```

## P2P Message Protocol

```
Message format (AES-256-GCM encrypted, JSON payload):

{
  "version": 1,
  "from": "alchemy-ally",
  "to": "alchemy-mini",
  "id": "uuid-4",
  "type": "capability_ad | request | response | heartbeat",
  "action": "generate_image | llm_chat | system_status | shader_build",
  "capabilities": ["gpu", "ai", "storage", "display"],
  "payload": {},
  "timestamp": 1719876543
}

Discovery (mDNS):
  Service: _alchemy-p2p._tcp.local
  TXT records: node_id, capabilities, version

UDP Beacon (port 8888, broadcast):
  {"node_id": "alchemy-ally", "ip": "10.0.0.5", "port": 45999, "caps": ["gpu","ai","storage","display"]}
```
