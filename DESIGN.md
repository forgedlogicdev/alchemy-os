# AlchemyOS — Visual Design Language

## Creative Direction: Alchemical Grimoire

Inspired by medieval illuminated manuscripts, alchemical treatises, and the hermetic tradition. The interface is an alchemist's workbench — parchment, gold leaf, crystal, and iron. Potions bubble in glass vessels. Elemental sigils mark the corners. Constellations map the mesh of connected devices. Every screen feels like a page from a grimoire bound in leather and stained with use.

The four classical elements (fire, water, air, earth) form the visual grammar: fire for active/processing states, water for audio/data flow, air for network/communication, earth for storage/stability. Gold represents the philosopher's stone — the perfected state, completion, enlightenment.

---

## Color Palette

```
┌──────────────────────────────────────────────────────────┐
│  Gold             #c9a84c    Primary accent, borders     │
│  Bright Gold      #e8c854    Highlights, active glow    │
│  Dim Gold         #8a6d2b    Secondary borders, muted   │
│  Parchment        #f4e4c1    Primary text on dark       │
│  Dark Parchment   #d4c4a0    Secondary text             │
│  Emerald          #2d6a4f    Success, vitality, water   │
│  Bright Emerald   #40916c    Active healthy states      │
│  Royal Purple     #4a0e4e    Depth, the void, mystery   │
│  Crimson          #8b1a1a    Warnings, fire, passion    │
│  Ink Black        #1a1a2e    Text on parchment bg       │
│  Charcoal         #2c1810    Root background            │
│  Copper           #b87333    Earth, metrics, warmth     │
│  Silver           #8a9597    Inactive, muted, air       │
└──────────────────────────────────────────────────────────┘
```

## Typography

| Use | Font | Style |
|---|---|---|
| Titles / Wordmark | **UnifrakturMaguntia** (blackletter) | Medieval manuscript headers |
| Panel headings | **IM Fell English SC** (small caps serif) | Engraved stone/wood feel |
| Body / Chat text | **IM Fell English** (italic serif) | Handwritten journal |
| Code / Data / Metrics | **Courier Prime** (monospace) | Scribe's ledger |

## Elemental Vocabulary

| Element | Symbol | Color | Domain |
|---|---|---|---|
| Fire | 🜂 | Crimson/Gold | CPU, GPU, active processes, heat |
| Water | 🜄 | Emerald/Blue | Audio flow, FFT, liquid data |
| Air | 🜁 | Silver/Gray | Network, P2P mesh, communication |
| Earth | 🜃 | Copper/Green | Storage, disk, persistence |
| Quintessence | 🜍 | Gold | The OS itself, completion |
| Vitriol | 🜔 | Purple | Transformation, shader compilation |
| Amalgam | 🜘 | Mixed | Combined states, crossfades |

---

## Device Interfaces

### 1. ROG Ally — AlchemyOS-Forge

**Boot Sequence:**
Darkness. A single gold spark ignites. The alchemical sigil ⚗ fades in, rotating slowly as gold leaf filigree spreads outward. "Alchemy OS" appears in UnifrakturMaguntia blackletter, each letter burning gold then cooling. The four elemental symbols mark the screen corners. A bell tolls once.

**Dashboard (Home Screen):**
- **Background:** Dark charcoal with parchment-like fibrous texture. Gold dust motes drift upward like particles in a sunbeam through an apothecary window.
- **Panels:** Framed like illuminated manuscript pages — double border (gold outer, thin inner), corner brackets. Each has a gold filigree drop cap on the title.
- **Scrying Mirror (Visualizer):** A circular "mirror" with rotating mandala, alchemical rings, and a glowing center point. Looks like divination.
- **Formula Scroll (Sequencer):** Grid of squares like alchemical notation. Active beats glow gold. Bars labeled as "phases." BPM shown with a ♩ symbol.
- **Homunculus (Adia):** A glass flask containing bubbling liquid. Bubbles rise. The liquid sloshes gently. She "lives" in the vessel.
- **Ingredient Cabinet (Shaders):** Small glass jars with colored liquids and cork stoppers — each representing a shader.
- **Apothecary Log (Metrics):** Measurements marked with elemental symbols. Progress bars look like filled measuring tubes.
- **Celestial Constellation (Mesh):** Peers shown as stars (★ aligned, ☆ obscured) connected by a golden constellation line.

### 2. Stream Deck Neo — AlchemyOS-Deck

**Keys:** Each key is an alchemical seal — the symbol for an element or compound rendered in gold on dark background. Glow intensifies on press. Key VII always reads "Ask Adia" in small caps.

**LCD Bar:** Rendered as a parchment scroll. FFT spectrum drawn as vertical ink strokes. Mode name in IM Fell English SC.

**Mode Switcher:** Planetary alignment dots at bottom — gold dot indicates current mode. Labels use alchemical stage names (Scrying Mirror, Apothecary, Great Work, Formula, Homunculus).

### 3. Pixel 10 Pro — AlchemyOS-Mobile

**Glyph Companion:**
- **Header:** Time in Courier Prime, mesh peers as star constellation mini-map.
- **Crystal Ball:** A glowing orb containing Glyph's 8 eyes, arranged in a circular mandala within the crystal. The crystal floats gently with a subtle magnetic bob.
- **Name:** "Glyph" rendered in UnifrakturMaguntia blackletter beneath the crystal.
- **Chat bubbles:** Glyph's messages have illuminated drop caps (the first letter in gold blackletter). Parchment-toned backgrounds with gold borders. User messages are darker, more muted.
- **Typing indicator:** "⚗ Glyph distills a response..."
- **Action buttons:** Three sealed scrolls — Gallery, Grimoire, Humours. Gold text on dark, with double-border treatment.
- **Elemental corners:** The four elemental symbols mark the screen edges at low opacity.

### 4. HP Mini — AlchemyOS-Node (web dashboard)

**Status Page:**
- Service status cards as alchemical apparatus — Ollama as a crucible, Stable Diffusion as a scrying mirror, Proxy as a distillation coil.
- Mesh status as a celestial chart with star nodes.
- Metrics as apothecary measurements with elemental symbols.
- Background: parchment-textured dark with gold dust.

### 5. MediaTab 3 — AlchemyOS-View

**AllyDroid Launcher:** Existing Android launcher restyled with alchemical theming — gold accents, parchment tones, constellation mesh indicator, elemental corner sigils.

### 6. Nuu+ — AlchemyOS-Lite

Minimal — constellation of peer stars with elemental status glyphs. Pure function.

---

## Motion Design

| Element | Behavior |
|---|---|
| **Gold dust** | Slow upward drift, 20-50 particles, bright gold, slight horizontal wander |
| **Crystal ball (Glyph)** | Gentle magnetic float (±6px, 4s cycle) |
| **Flask (Adia)** | Bubbles rise and pop, liquid sloshes with subtle surface tension |
| **Panel borders** | Gold filigree subtly brightens on hover/focus |
| **Transitions** | Page dissolves through gold wash, like turning a vellum page |
| **Notifications** | A rolled scroll unfurls from top edge with a soft parchment sound |
| **Loading** | An alembic fills drop by drop with golden liquid |
| **Errors** | Ink spills and spreads from the affected element |
| **Success** | Gold leaf blooms outward from the completed action |

## Sound Design

| Event | Sound |
|---|---|
| Boot | Cathedral bell toll + parchment rustle |
| Mode switch | Glass vial clink |
| Adia speaks | Liquid burble + whispered words |
| Error | Ink brush stroke — sharp, short |
| Mesh peer connects | Star chime — soft, crystalline |
| Button press | Wax seal stamp — dull thud |

---

## Implementation

- All color values defined as CSS custom properties / PyQt stylesheet variables
- Fonts: UnifrakturMaguntia, IM Fell English (SC), Courier Prime — all open source via Google Fonts
- Gold dust particle effect: lightweight canvas overlay
- Alchemical symbol rendering: Unicode characters (U+1F702-U+1F718 range), fallback to SVG for custom sigils
- Dark parchment theme only — AlchemyOS is a medieval workbench, not a modern OS
