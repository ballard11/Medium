"""
Publish a markdown article to Medium as a draft.

Usage:
    python publish.py cfb-data-analysis
    python publish.py maryland-car-crashes --status draft
    python publish.py zillow-home-values --tags "data science,real estate"
"""

import argparse
import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path


def get_medium_user_id(token):
    """Fetch the authenticated user's Medium ID."""
    resp = requests.get(
        "https://api.medium.com/v1/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    resp.raise_for_status()
    return resp.json()["data"]["id"]


def publish_article(token, user_id, title, content, tags=None, status="draft"):
    """Publish content to Medium. Returns the API response data."""
    payload = {
        "title": title,
        "contentFormat": "markdown",
        "content": content,
        "publishStatus": status,
    }
    if tags:
        payload["tags"] = [t.strip()[:25] for t in tags[:3]]

    resp = requests.post(
        f"https://api.medium.com/v1/users/{user_id}/posts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json=payload,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def extract_title(markdown_text):
    """Pull the first H1 heading from markdown as the title."""
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            return stripped.lstrip("# ").strip()
    return "Untitled"


def main():
    parser = argparse.ArgumentParser(
        description="Publish a project's article.md to Medium"
    )
    parser.add_argument(
        "project",
        help="Project folder name (e.g. cfb-data-analysis)",
    )
    parser.add_argument(
        "--status",
        choices=["draft", "public", "unlisted"],
        default="draft",
        help="Publish status (default: draft)",
    )
    parser.add_argument(
        "--tags",
        help='Comma-separated tags, e.g. "data science,python,plotly"',
        default="",
    )
    parser.add_argument(
        "--file",
        default="article.md",
        help="Markdown file within the project folder (default: article.md)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).parent
    load_dotenv(repo_root / ".env")

    token = os.getenv("MEDIUM_TOKEN")
    if not token:
        print("ERROR: MEDIUM_TOKEN not found in .env")
        sys.exit(1)

    article_path = repo_root / args.project / args.file
    if not article_path.exists():
        print(f"ERROR: {article_path} not found")
        print(f"Make sure {args.project}/{args.file} exists.")
        sys.exit(1)

    content = article_path.read_text(encoding="utf-8")
    title = extract_title(content)

    if len(title) > 100:
        print(f"WARNING: Title is {len(title)} chars (max 100). Truncating.")
        title = title[:100]

    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []

    print(f"Publishing: {title}")
    print(f"  From:   {article_path}")
    print(f"  Status: {args.status}")
    print(f"  Tags:   {tags if tags else '(none)'}")
    print()

    confirm = input("Proceed? [y/N] ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        sys.exit(0)

    user_id = get_medium_user_id(token)
    result = publish_article(
        token=token,
        user_id=user_id,
        title=title,
        content=content,
        tags=tags,
        status=args.status,
    )

    print()
    print("Published successfully!")
    print(f"  URL:    {result.get('url', 'N/A')}")
    print(f"  ID:     {result.get('id', 'N/A')}")
    print(f"  Status: {result.get('publishStatus', 'N/A')}")


if __name__ == "__main__":
    main()
