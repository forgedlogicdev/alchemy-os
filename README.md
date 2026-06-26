# AlchemyOS

A cross-device distributed operating system for live VJ performance, AI companionship, and creative computing. One OS, many faces — tailored for each device in the ecosystem.

## Vision

AlchemyOS transforms a collection of devices into a unified, offline-capable creative computing mesh. A VJ rig where the ROG Ally drives GPU visualizations, the Stream Deck Neo provides tactile control, the HP Mini serves as an AI inference node, the Pixel 10 Pro hosts a personal AI companion, and tablets serve as wireless secondary displays — all connected via a password-protected P2P mesh that works with or without internet.

## Device Matrix

| Device | AlchemyOS Flavor | Base OS | Primary Role |
|---|---|---|---|
| **ROG Ally** | AlchemyOS-Forge | Bazzite | GPU visualizer engine + P2P mesh master |
| **HP Mini** | AlchemyOS-Node | Linux Mint | Headless AI inference (Ollama/SD) + build server |
| **Pixel 10 Pro** | AlchemyOS-Mobile | Android + Termux | Glyph AI companion + FlyCode mobile coding |
| **Nuu+** | AlchemyOS-Lite | LineageOS | Companion display + notification relay |
| **MediaTab 3** | AlchemyOS-View | Android | Wireless second screen via AllyDroid |
| **Stream Deck Neo** | AlchemyOS-Deck | N/A (peripheral) | Physical control surface (USB to Ally) |

## P2P Mesh — Dual Transport

```
                    ┌──────────────┐
                    │   INTERNET   │
                    │ (Tailscale)  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         ┌─────────┐ ┌─────────┐ ┌──────────┐
         │ROG Ally │ │HP Mini  │ │Pixel 10  │
         │(Master) │ │(Worker) │ │(Client)  │
         └────┬────┘ └─────────┘ └──────────┘
              │
              │ Hotspot "AlchemyOS-Mesh"
              │ (offline fallback)
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
┌───────┐ ┌───────┐ ┌───────┐
│ M3Tab │ │ Nuu+  │ │HP Mini│
│(View) │ │(Lite) │ │(LAN)  │
└───────┘ └───────┘ └───────┘
```

- **Online mode:** All devices connect via Tailscale WireGuard VPN. MagicDNS resolves each node (`alchemy-ally`, `alchemy-mini`, etc.).
- **Offline mode:** ROG Ally creates hotspot `AlchemyOS-Mesh`. All devices join and discover peers via mDNS (`_alchemy-p2p._tcp.local:45999`). Zero internet dependency.
- **Auth:** AES-256-GCM challenge/response with shared passphrase on all messages.
- **Mesh host:** ROG Ally always (best WiFi chip, always present at performances).

## Quick Links

- [ARCHITECTURE.md](ARCHITECTURE.md) — Full system topology, port map, service dependency graph
- [INSTALL.md](INSTALL.md) — Per-device installation guides
- [docs/p2p-protocol.md](docs/p2p-protocol.md) — Mesh message format and discovery
- [docs/service-map.md](docs/service-map.md) — Systemd services and boot chain

## Repository Structure

```
alchemy-os/
├── README.md
├── ARCHITECTURE.md
├── INSTALL.md
├── docs/
│   ├── p2p-protocol.md
│   ├── service-map.md
│   └── shader-vault.md
├── forge/                    # AlchemyOS-Forge (ROG Ally)
├── node/                     # AlchemyOS-Node (HP Mini)
├── mobile/                   # AlchemyOS-Mobile (Pixel)
├── p2p/                      # Shared P2P mesh daemon
├── drivers/                  # Hardware drivers
├── systemd/                  # Boot chain service files
├── scripts/                  # Install + tooling
└── .github/workflows/        # CI/CD
```

## License

MIT
