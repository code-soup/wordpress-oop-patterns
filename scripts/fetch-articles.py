#!/usr/bin/env python3
"""Fetch Carl Alexander articles and write one markdown file per post with code examples."""

from __future__ import annotations

import html
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

USER_AGENT = "WordPressOOPPatternsSkill/1.1 (+https://github.com/code-soup/wordpress-oop-patterns)"
DELAY_SECONDS = 0.75
SITEMAP_URL = "https://carlalexander.ca/sitemap.xml"
MANUAL_URL_ALIASES = {
    "helping-wordpress-make-friends-decorator-pattern": "https://carlalexander.ca/wordpress-decorator-pattern/",
    "how-i-marketed-published-niche-wordpress-book": "https://carlalexander.ca/marketing-and-publishing-niche-wordpress-book/",
    "php-strings-how-to-format-them": "https://carlalexander.ca/php-string-formatting/",
}
STOPWORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "as",
        "do",
        "for",
        "from",
        "how",
        "if",
        "in",
        "is",
        "it",
        "of",
        "on",
        "or",
        "the",
        "to",
        "using",
        "with",
        "wordpress",
        "you",
        "your",
    }
)

ENTRY_RE = re.compile(
    r"^### (.+)\n"
    r"\*\*URL:\*\* (https://carlalexander\.ca/[^\s]+)\n"
    r"\*\*Teaches:\*\* (.+?)(?=\n\n|\Z)",
    re.MULTILINE,
)

PRE_RE = re.compile(
    r"<pre[^>]*class=\"[^\"]*lang:php[^\"]*\"[^>]*>(.*?)</pre>",
    re.IGNORECASE | re.DOTALL,
)

TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)
H1_RE = re.compile(r"<h1[^>]*class=\"[^\"]*entry-title[^\"]*\"[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)


def slug_from_url(url: str) -> str:
    path = url.rstrip("/").split("/")[-1]
    return re.sub(r"[^a-z0-9\-]", "-", path.lower())


def slug_tokens(slug: str) -> set[str]:
    parts = {part for part in slug.split("-") if part and part not in STOPWORDS}
    return parts


def load_sitemap_urls() -> list[str]:
    xml = fetch_url(SITEMAP_URL)
    candidates = re.findall(r"<loc>(https://carlalexander\.ca/[^<]+)</loc>", xml)
    skip_paths = {
        "",
        "articles",
        "now",
        "active",
        "newsletter",
        "discover-object-oriented-programming",
        "object-oriented-programming-wordpress",
    }
    filtered: list[str] = []
    for url in candidates:
        path = urlpath(url)
        if path in skip_paths:
            continue
        if "/" in path:
            continue
        if path.startswith(("tag", "category", "author", "wp-")):
            continue
        filtered.append(url.rstrip("/") + "/")
    return filtered


def urlpath(url: str) -> str:
    return url.replace("https://carlalexander.ca/", "").strip("/")


def resolve_url(catalog_url: str, sitemap_urls: list[str]) -> str:
    catalog_slug = slug_from_url(catalog_url)
    if catalog_slug in MANUAL_URL_ALIASES:
        return MANUAL_URL_ALIASES[catalog_slug]
    catalog_tokens = slug_tokens(catalog_slug)
    if not catalog_tokens:
        return catalog_url

    best_url = catalog_url
    best_score = 0.0

    for candidate in sitemap_urls:
        candidate_slug = slug_from_url(candidate)
        candidate_tokens = slug_tokens(candidate_slug)
        if not candidate_tokens:
            continue
        overlap = len(catalog_tokens & candidate_tokens)
        score = overlap / len(catalog_tokens)
        if score > best_score:
            best_score = score
            best_url = candidate

    if best_score >= 0.45 and best_url != catalog_url:
        return best_url
    return catalog_url


def url_exists(url: str) -> bool:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return 200 <= response.status < 400
    except urllib.error.HTTPError as error:
        if error.code == 405:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=30):
                return True
        return False


def strip_tags(fragment: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def extract_code_blocks(page_html: str) -> list[str]:
    blocks: list[str] = []
    for match in PRE_RE.finditer(page_html):
        raw = match.group(1)
        code = strip_tags(raw)
        if len(code) < 10:
            continue
        if code in blocks:
            continue
        blocks.append(code)
    return blocks


def fetch_url(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def parse_title(page_html: str, fallback: str) -> str:
    title_match = TITLE_RE.search(page_html)
    if title_match:
        title = html.unescape(title_match.group(1)).split("|")[0].strip()
        if title and len(title) < 200:
            return title
    h1 = H1_RE.search(page_html)
    if h1:
        title = strip_tags(h1.group(1)).split("\n")[0].strip()
        if title and len(title) < 200:
            return title
    return fallback


def write_article(
    path: Path,
    title: str,
    url: str,
    teaches: str,
    codes: list[str],
    catalog_url: str | None = None,
) -> None:
    lines = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f"url: {url}",
        f'slug: {slug_from_url(url)}',
        f"fetched: {date.today().isoformat()}",
    ]
    if catalog_url and catalog_url != url:
        lines.append(f"catalog_url: {catalog_url}")
    lines.append("---")
    lines.extend(
        [
            "",
            f"# {title}",
            "",
            "## Summary",
            "",
            teaches.strip(),
            "",
        ]
    )

    if codes:
        lines.extend(["## Code examples", ""])
        for index, code in enumerate(codes, start=1):
            lines.extend([f"### Example {index}", "", "```php", code, "```", ""])
    else:
        lines.extend(
            [
                "## Code examples",
                "",
                "_No SyntaxHighlighter PHP blocks found on the live page. Read the source article._",
                "",
            ]
        )

    lines.extend(["## Source", "", url, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    catalog = skill_root / "references" / "article-catalog.md"
    out_dir = skill_root / "references" / "articles"
    out_dir.mkdir(parents=True, exist_ok=True)

    if not catalog.is_file():
        print(f"Missing catalog: {catalog}", file=sys.stderr)
        return 1

    catalog_text = catalog.read_text(encoding="utf-8")
    entries = list(ENTRY_RE.finditer(catalog_text))
    if not entries:
        print("No articles parsed from catalog.", file=sys.stderr)
        return 1

    index_lines = [
        "# Article index",
        "",
        f"Generated {date.today().isoformat()}. One local file per Carl Alexander article.",
        "",
    ]

    print("Loading sitemap...")
    sitemap_urls = load_sitemap_urls()

    ok = 0
    failed: list[str] = []

    for match in entries:
        heading_title = match.group(1).strip()
        catalog_url = match.group(2).strip()
        teaches = match.group(3).strip()
        url = catalog_url
        if not url_exists(url):
            resolved = resolve_url(catalog_url, sitemap_urls)
            if resolved != catalog_url:
                print(f"Redirect {slug_from_url(catalog_url)} -> {slug_from_url(resolved)}")
                url = resolved
        slug = slug_from_url(url)
        out_path = out_dir / f"{slug}.md"

        try:
            page = fetch_url(url)
            title = heading_title or parse_title(page, heading_title)
            codes = extract_code_blocks(page)
            write_article(
                out_path,
                title,
                url,
                teaches,
                codes,
                catalog_url=catalog_url,
            )
            index_lines.append(f"- [{title}]({slug}.md) — {url}")
            ok += 1
            print(f"OK {slug} ({len(codes)} examples)")
        except (urllib.error.URLError, TimeoutError, ValueError) as error:
            failed.append(f"{slug}: {error}")
            print(f"FAIL {slug}: {error}", file=sys.stderr)

        time.sleep(DELAY_SECONDS)

    (out_dir / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    print(f"\nDone: {ok}/{len(entries)} articles. Index: {out_dir / 'README.md'}")
    if failed:
        print("Failures:", file=sys.stderr)
        for line in failed:
            print(f"  {line}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())