# AlchemyOS — Visual Design Language

## Creative Direction: Bio-Mechanical Beksiński

Inspired by Zdzisław Beksiński's dystopian surrealism: organic bone-like structures fused with corroded machinery, desolate amber horizons bleeding into deep violet voids, and the sense that the interface itself is alive — a breathing, symbiotic organism wrapped around cold metal.

Every AlchemyOS screen should feel like looking through a surgical incision into a living machine.

---

## Color Palette

```
┌──────────────────────────────────────────────────────────┐
│  Bone White       #e8d5b7    Primary text, highlights    │
│  Aged Parchment   #c4a67a    Secondary text, borders     │
│  Amber Ember      #d4853a    UI accents, active states   │
│  Burnt Rust       #8b3a2a    Warning, destructive actions│
│  Deep Violet      #2d1b3d    Panel backgrounds           │
│  Void Black       #0d0a12    Root background             │
│  Flesh Undertone  #4a2c3b    Card surfaces, hover states │
│  Copper Oxide     #3d6b5e    Success, system healthy     │
│  Bone Marrow      #f0e0c8    Brightest highlight elements│
│  Rotting Vein     #5c1a2e    Error, critical alerts      │
└──────────────────────────────────────────────────────────┘
```

## Typography

| Use | Font | Style |
|---|---|---|
| Headers / Titles | **Cinzel** (serif, small caps) | Bone-carved monumental |
| Body / UI text | **Crimson Text** (serif) | Aged manuscript feel |
| Code / Terminal | **JetBrains Mono** | Crisp readability in dark |
| Data / Metrics | **Space Mono** | Cold mechanical precision |

---

## Device Interfaces

### 1. ROG Ally — AlchemyOS-Forge (1920×1080, 7-inch touch)

**Boot Sequence:**
Black void. A single amber pulse, slow breathing rhythm. Faint bone-like structures fade in from the edges — ribs and vertebrae forming the AlchemyOS sigil. "ALCHEMYOS" carves itself into view in Cinzel small caps, each letter burning orange then cooling to bone white. A subtle heartbeat thump on the audio.

**Dashboard (Home Screen):**

```
┌──────────────────────────────────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│ ░░  ╔══════════════╗  ╔══════════════╗  ╔══════════╗ ░░ │
│ ░░  ║  VISUALIZER  ║  ║   SEQUENCER  ║  ║  ADIA    ║ ░░ │
│ ░░  ║  ┌─┐ ┌─┐    ║  ║  ■  ▢  ▢  ■  ║  ║  ◉  ◉    ║ ░░ │
│ ░░  ║  │◉│ │◉│    ║  ║  ▢  ■  ■  ▢  ║  ║  ◉──◉    ║ ░░ │
│ ░░  ║  └─┘ └─┘    ║  ║  ■  ■  ▢  ■  ║  ║  ◉  ◉    ║ ░░ │
│ ░░  ║    ACTIVE   ║  ║    120 BPM   ║  ║  AWAKE    ║ ░░ │
│ ░░  ╚══════════════╝  ╚══════════════╝  ╚══════════╝ ░░ │
│ ░░                                                        │
│ ░░  ╔══════════════╗  ╔══════════════╗  ╔══════════╗ ░░ │
│ ░░  ║   SHADERS    ║  ║   METRICS    ║  ║   MESH    ║ ░░ │
│ ░░  ║  ⟐  ✧  ◈   ║  ║ CPU ████░░  ║  ║ ALLY  ●   ║ ░░ │
│ ░░  ║  ◈  ⟐  ✧   ║  ║ GPU ██████  ║  ║ MINI  ●   ║ ░░ │
│ ░░  ║  ✧  ◈  ⟐   ║  ║ RAM ███░░░  ║  ║ PIXEL ○   ║ ░░ │
│ ░░  ║  34 SHADERS  ║  ║  TEMP 62°C  ║  ║ TAB   ●   ║ ░░ │
│ ░░  ╚══════════════╝  ╚══════════════╝  ╚══════════╝ ░░ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
└──────────────────────────────────────────────────────────┘
```

**Key visual elements:**
- All panels are organic rectangles with subtly curved/eroded corners, as if grown rather than drawn
- Panel borders are bone-like — thin lines that branch and split like capillaries
- Background is a slowly breathing void with faint amber particles drifting upward like embers
- Each panel has a subtle inner shadow that makes it feel recessed into flesh
- The mesh indicator (bottom right) shows connected peers as pulsing vertebrae nodes on a spine-like diagram
- Active states glow amber; inactive states are muted violet
- Touch targets have a subtle ripple that looks like blood dispersing in water

**Visualizer Mode (fullscreen):**
The 3D visualizer fills the screen behind semi-transparent Beksiński-inspired UI elements. Control strips at bottom edge are bone fragments — thin, jagged, with amber runes indicating parameters. FFT waveform is drawn as a twitching nerve fiber across the bottom. Crossfader is a vertebrae slider.

**Adia Companion Mode:**
Adia's 8 eyes appear arranged in a circular mandala. Each eye has a human iris but surrounded by mechanical aperture blades. When she speaks, her "mouth" is a sine-wave incision across the bottom of the eye cluster. Her chat responses appear in parchment-colored boxes with burnt edges.

---

### 2. Stream Deck Neo — AlchemyOS-Deck (8×96×96px keys + 248×58 LCD)

**Idle State (no mode active):**
All 8 keys display faint amber pulsing eyes in darkness. The LCD screen shows "ALCHEMYOS" in Cinzel small caps with a slow heartbeat line underneath.

**Visualizer Mode:**
- Keys 0-7: Each shows a live 96×96 thumbnail of a visual generator. Framed in thin bone-white borders that respond to audio — borders pulse/thicken with the beat.
- LCD: Horizontal FFT spectrum rendered as 248 vertical bone-spike columns, amber at the bottom fading to violet at the tips.

**Sequencer Mode:**
- Keys: 4×2 grid of amber step indicators. Active steps glow bright amber, inactive are dim violet dots. Current step has a rotating mandala ring.
- LCD: 32-bar progress as a spine with vertebrae. Current bar highlighted amber. BPM shown as a beating amber heart icon.

**Metrics Mode:**
- Keys: CPU (brain-like wireframe), RAM (stacked bone plates), Temp (thermometer vein), Disk (spine segments), Network (neuron branches), Audio (cochlea spiral), Battery (amber fluid level), FPS (flickering flame).
- LCD: Full status readout in JetBrains Mono, amber on void black.

**Adia Mode:**
- Keys 0-6: Her eyes in different states (open, half-lidded, closed, blinking, excited, curious, asleep).
- Key 7: Always labeled "ASK ADIA" in bone white on deep violet.
- LCD: Her last message scrolls horizontally in Crimson Text, with a subtle sine wave underneath when she's "speaking."

---

### 3. Pixel 10 Pro — AlchemyOS-Mobile (2400×1080)

**Glyph Companion Screen:**

```
┌──────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ <- amber ember particles
│                              │
│      ◉  ◉  ◉  ◉  ◉  ◉      │
│         ◉      ◉            │ <- Glyph's 8 eyes
│      ◉  ◉  ◉  ◉  ◉  ◉      │    (animated mandala)
│                              │
│  ┌────────────────────────┐ │
│  │  "Good evening, Dru.   │ │ <- Chat bubble with
│  │  How did the welding   │ │    burnt parchment edges
│  │  go today?"            │ │
│  └────────────────────────┘ │
│                              │
│  ┌────────────────────────┐ │
│  │        [GALLERY]       │ │ <- Amber-bordered buttons
│  │  [MEMORY]   [STATUS]   │ │    with bone texture
│  └────────────────────────┘ │
└──────────────────────────────┘
```

- Dark void background with slow amber particle drift
- Glyph's eye mandala at center top — eyes animate independently, mechanical aperture irises contract/dilate
- Chat bubbles: parchment texture, burnt/charred edges, serif font
- Buttons: raised bone-like surface, engraved labels
- Status bar at top: Mesh connection spine with amber nodes for each connected peer
- Pull-to-refresh: the mandala eyes all close and reopen

**FlyCode Screen:**
- Code editor in JetBrains Mono on void black
- Line numbers are amber
- Active line has a subtle amber glow behind it
- AI responses appear in parchment-toned panels from the bottom
- The opencode server connection indicator is a pulsing neuron at top right

---

### 4. HP Mini — AlchemyOS-Node (Headless, via Web Dashboard)

**Status Dashboard (browser-based, 800×480):**

```
┌────────────────────────────────────────────────────────┐
│  ALCHEMYOS NODE    ░░░░░░░░░░░░░░      ◉ CONNECTED    │
│  HP MINI           amber particles                     │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   OLLAMA     │  │ STABLE DIFF  │  │  GLYPH PROXY │ │
│  │   ◉ ACTIVE   │  │   ◉ IDLE    │  │  ◉ STREAMING │ │
│  │ llama3:8b    │  │ v1.5 loaded  │  │ 3 req/min    │ │
│  │ 2.3GB VRAM   │  │              │  │              │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                        │
│  ═════════════════ SPINE STATUS ═══════════════════   │
│  ◉─────◉─────○─────◉─────◉                           │
│  ALLY  MINI  PIXEL  TAB   NUU                          │
│                                                        │
│  ┌──────────────────────────────────────────────────┐ │
│  │ CPU  ████████░░ 45%   TEMP  62°C                 │ │
│  │ RAM  ██████░░░░ 58%   DISK  23%                  │ │
│  │ NET  ██████████ ██     UPTIME  14d 6h            │ │
│  └──────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────┘
```

- All panels bordered with branching bone-like lines
- Service statuses show as mechanical irises: open amber = active, closed violet = stopped
- The spine diagram shows all mesh peers as vertebrae on a spinal cord
- Metrics use amber-to-violet gradient bars
- Background: dark void with occasional ember drift

---

### 5. MediaTab 3 — AlchemyOS-View

**AllyDroid Launcher (home screen):**

A darkened version of the existing AllyDroid glassmorphism design, but with Beksiński elements:
- Background: void black with subtle amber ember particles
- App icons: bone-white glyphs on black, surrounded by thin mechanical aperture rings
- VNC viewer launches into a darkened overlay with throat-like screen bezel — as if looking through a wound into the Ally's display
- Connection indicator: a spine of amber nodes, each node a peer, pulsating with connection health

---

### 6. Nuu+ — AlchemyOS-Lite

**Cyber Monitor (96×64 tiny display):**

```
┌──────────────────────────────┐
│  ◉ ALLY  62°C  ████░░       │
│  ◉ MINI  OK    ██████       │
│  ○ PIXEL AWAY  ░░░░░░       │
│  ◉ TAB   OK    ███░░░       │
│                              │
│  ░░░░░░░░░░░░░░░░░░░░░░░░   │
└──────────────────────────────┘
```

Minimal — just mesh peer status as a vertical spine of amber nodes, and a horizontal FFT bar. No decoration, pure function. The "AlchemyOS" wordmark appears briefly at boot then fades.

---

## Motion Design Principles

| Element | Behavior |
|---|---|
| **Background void** | Slow drift of amber ember particles (0.5px/s upward), subtle breathing pulse (4s cycle, ±2% opacity) |
| **Panel borders** | Capillary branches grow subtly when panel is focused |
| **Buttons** | On press: surface depresses inward (2px), brief amber flash, then returns with a subtle "flesh settling" rebound |
| **Transitions** | Screen changes dissolve through a brief amber flash, like an eye blinking |
| **Notifications** | Appear as if cut into the screen — a thin amber incision opens, message slides in, incision heals closed |
| **FFT/audio** | Waveforms render as twitching nerve fibers, not clean lines |
| **Loading** | A mechanical iris slowly opens, revealing the content behind |
| **Error states** | Screen edges darken with vein-like rot spreading inward from corners |
| **Success states** | A brief copper oxide bloom radiates from the affected element |

---

## Sound Design (bonus)

| Event | Sound |
|---|---|
| Boot complete | Low sub-bass thump + metallic resonance decay (like a tuning fork struck on bone) |
| Mode switch | Mechanical aperture click + soft amber chime |
| Adia speaks | Whispered undertone mixed with subtle sine wave |
| Error | Distant, muffled impact (like something heavy falling in another room) |
| Mesh peer connects | Soft vertebrae click — like bones realigning |
| Button press | Muted tactile thud — flesh on metal |

---

## Implementation Notes

- All UI built with PyQt5 on Ally, Compose on Android, HTML/CSS on web dashboards
- Color palette defined as CSS custom properties / PyQt stylesheet variables for consistency
- Amber ember particle effect: lightweight Canvas/WebGL overlay (or QPainter on Qt)
- All fonts available as open source (Cinzel, Crimson Text, JetBrains Mono, Space Mono via Google Fonts)
- Dark theme is the only theme — no light mode. AlchemyOS is a creature of the void.
