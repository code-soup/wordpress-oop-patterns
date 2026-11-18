# WordPress OOP Patterns Agent Skill

An [Agent Skill](https://agentskills.io) catalog of [Carl Alexander](https://carlalexander.ca/) WordPress OOP articles: local summaries, PHP examples, and implementation patterns for AI-assisted plugin architecture.

## What This Skill Does

Helps agents and developers when:

- Modeling domain code (entities, repositories, custom post types)
- Choosing architecture patterns (SOLID, strategy, chain, decorator, mediator, …)
- Designing REST, admin, routing, or event systems in WordPress
- Refactoring procedural plugins toward object-oriented structure

The skill ships **68 per-article reference files** (scraped from carlalexander.ca) plus composite templates in `references/implementation-patterns.md`.

## Installation

### Skillshare (recommended)

```bash
skillshare install github.com/code-soup/wordpress-oop-patterns --track
skillshare sync
```

See [SKILLSHARE.md](SKILLSHARE.md) for local clone and updates.

### Manual

```bash
git clone https://github.com/code-soup/wordpress-oop-patterns.git
```

Add the clone to your agent’s skills directory per [agentskills.io](https://agentskills.io), or run `skillshare install ./wordpress-oop-patterns` from the parent folder.

## Usage

Once installed, mention Carl Alexander patterns, SOLID, DI, or WordPress plugin architecture; the agent loads `SKILL.md` and reads `references/articles/{slug}.md` as needed.

Refresh article snapshots after upstream site changes:

```bash
python3 scripts/fetch-articles.py
```

## Layout

```
wordpress-oop-patterns/
├── SKILL.md                          # Entry point for agents
├── SKILLSHARE.md                     # Skillshare install notes
├── scripts/
│   └── fetch-articles.py             # Re-sync from carlalexander.ca
└── references/
    ├── article-catalog.md            # Topic groupings
    ├── implementation-patterns.md    # Entity / Repository / DI templates
    └── articles/                     # One file per article
        ├── README.md                 # Index
        └── *.md
```

## Requirements

- Python 3.9+ (only for `fetch-articles.py`)
- Network access when re-fetching articles

## Content and attribution

Article prose and examples are © [Carl Alexander](https://carlalexander.ca/). Each file includes the canonical URL; use the live site for full context. This repository is an **index and study aid**, not a replacement for the originals.

## License

MIT — see [LICENSE](LICENSE). Third-party article content remains governed by the author’s site terms.