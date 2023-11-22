import asyncio
import pprint

from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_playwright, scrape_with_playwright_ai


# TESTING
if __name__ == "__main__":
    token_limit = 1000

    # News sites mostly have <span> tags to scrape
    cnn_url = "https://www.cnn.com"
    wsj_url = "https://www.wsj.com"
    nyt_url = "https://www.nytimes.com/ca/"
    ecommerce_url = "https://appsumo.com"
    enghub_url = "https://dev.azure.com/DataAI/Readiness/_wiki/wikis/Readiness/91/Accelerating-Solutions-with-Cosmos-DB"

    urls = [wsj_url, cnn_url, nyt_url, ecommerce_url, enghub_url]
    schema = {
        "properties": {
            "news_article_title": {"type": "string"},
            "news_article_summary": {"type": "string"},
        },
        "required": ["news_article_title", "news_article_summary"],
    }
    
    tags_to_extract = ["span"]
    extracted_content = scrape_with_playwright_ai(urls, schema=schema)
    pprint.pprint(extracted_content)