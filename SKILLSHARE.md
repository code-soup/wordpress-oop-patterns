# Installing WordPress OOP Patterns via Skillshare

Compatible with [Skillshare](https://skillshare.runkids.cc/) and the [Agent Skills](https://agentskills.io/) layout.

## Prerequisites

```bash
brew install runkids/tap/skillshare
```

## From GitHub

```bash
skillshare install github.com/code-soup/wordpress-oop-patterns --track
skillshare sync
```

## From local clone

```bash
cd ~/www/codesoup/projects/skills/wordpress-oop-patterns
skillshare install . --track
skillshare sync
```

## Verify

```bash
skillshare list | grep wordpress-oop-patterns
skillshare status
```

## Update

```bash
skillshare update wordpress-oop-patterns
skillshare sync
```

## Uninstall

```bash
skillshare uninstall wordpress-oop-patterns
skillshare sync
```

## Skillshare UI import

In the Skillshare web UI, add the remote:

`https://github.com/code-soup/wordpress-oop-patterns`

This repo is a **single-skill root** (same layout as [vendor-scoping-wordpress-plugins](https://github.com/code-soup/vendor-scoping-wordpress-plugins)): `SKILL.md` lives at the repository root.