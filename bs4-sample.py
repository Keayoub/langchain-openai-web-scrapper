import os
import pprint
import asyncio

from scrape import scrape_with_playwright_ai

urls = [
    "https://www.wsj.com",
    "https://www.nytimes.com",
    "https://www.bbc.com",
    "https://www.theguardian.com",
]
schema = {
    "properties": {
        "news_article_title": {"type": "string"},
        "news_article_summary": {"type": "string"},
    },
    "required": ["news_article_title", "news_article_summary"],
}

tags_to_extract = ["span", "article"]
extracted_content = scrape_with_playwright_ai(urls, schema=schema)
pprint.pprint(extracted_content)
