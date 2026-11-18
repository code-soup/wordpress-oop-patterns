---
name: wordpress-oop-patterns
description: Carl Alexander WordPress OOP pattern catalog with per-article local summaries and PHP examples scraped from carlalexander.ca. Use when modeling domain code, choosing architecture patterns, refactoring toward SOLID, or implementing entities/repositories/REST/admin in WordPress plugins.
license: MIT
metadata:
  author: code-soup
  source: https://carlalexander.ca/tag/wordpress/
  repository: https://github.com/code-soup/wordpress-oop-patterns
  version: "1.1"
---

# WordPress OOP Patterns by Carl Alexander

Curated Carl Alexander articles for WordPress OOP architecture. Install via [Skillshare](SKILLSHARE.md) or clone [code-soup/wordpress-oop-patterns](https://github.com/code-soup/wordpress-oop-patterns).

## Location

| Path | Contents |
|------|----------|
| [references/articles/README.md](references/articles/README.md) | Index of **68 articles** (one `.md` file each) |
| [references/articles/*.md](references/articles/) | Summary + PHP examples pulled from the live site |
| [references/article-catalog.md](references/article-catalog.md) | Topic groupings and quick matrix |
| [references/implementation-patterns.md](references/implementation-patterns.md) | Composite Entity / Repository / DI templates |
| [scripts/fetch-articles.py](scripts/fetch-articles.py) | Re-sync examples from carlalexander.ca |

## When to Use

- Designing entities, repositories, DI, or design patterns in WordPress plugins
- User mentions Carl Alexander, SOLID, strategy/chain/decorator/mediator, or WP REST/admin architecture
- You need **concrete PHP snippets** without opening the browser (read `references/articles/{slug}.md`)

## How to Use

1. Pick a pattern from the matrix below or [article-catalog.md](references/article-catalog.md).
2. Open the matching file under `references/articles/` (slug matches the **live** URL path; `catalog_url` in frontmatter if the catalog link moved).
3. Use examples as starting points; align with your project’s container, hooks, and service providers when applicable.
4. Refresh local copies after site changes (from this repo root):

```bash
python3 scripts/fetch-articles.py
```

## Quick Reference Matrix

| Need | Pattern | Start here |
|------|---------|------------|
| Business logic vs DB | Entity | `references/articles/designing-entities-wordpress-custom-post-types.md` |
| Abstract `WP_Query` | Repository | `references/articles/designing-class-manage-wordpress-posts.md` |
| Dependencies | DI | `references/articles/dependency-injection-wordpress.md` |
| Pipelines | Chain of responsibility | `references/articles/chain-of-responsibility-pattern-wordpress.md` |
| Swappable logic | Strategy | `references/articles/importing-data-wordpress-strategy-pattern.md` |
| REST | System design | `references/articles/designing-system-wordpress-rest-api-endpoints.md` |
| Admin UI | System design | `references/articles/designing-system-wordpress-admin-pages.md` |

## CodeSoup / Phoenix alignment (optional)

When working in [code-soup/phoenix](https://github.com/code-soup/phoenix):

| Pattern | This plugin |
|---------|----------------|
| DI + modules | `CodeSoup\Phoenix\Core\Container`, providers in `includes/providers/` |
| Hooks | `CodeSoup\Phoenix\Core\Hooker` — queue before `Hooker::run()` |
| Domain | `includes/phoenix/` |

## Best Practices

- Prefer article files over the catalog when you need code.
- Do not treat scraped examples as production-ready without WPCS, nonces, and namespace review.
- Article prose © Carl Alexander — link to the `url` in each file for full context.