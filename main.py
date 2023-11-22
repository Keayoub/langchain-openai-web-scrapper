import asyncio
import pprint

from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_llm_loader, ascrape_playwright
from langchain.document_loaders import AsyncHtmlLoader

# TESTING
if __name__ == "__main__":
    token_limit = 1000

    # News sites mostly have <span> tags to scrape
    cnn_url = "https://www.cnn.com"
    wsj_url = "https://www.wsj.com"
    nyt_url = "https://www.nytimes.com/ca/"
    ecommerce_url = "https://appsumo.com"
    enghub_url = "https://dev.azure.com/DataAI/Readiness/_wiki/wikis/Readiness/91/Accelerating-Solutions-with-Cosmos-DB"

    urls = [cnn_url]
    schema = {
        "properties": {
            "news_article_title": {"type": "string"},
            "news_article_summary": {"type": "string"},
        },
        "required": ["news_article_title", "news_article_summary"],
    }
    tags_to_extract = ["span", "article"]

    async def scrape_with_playwright(url: str, **kwargs):
        html_content = await ascrape_playwright(url)

        print("Extracting content with LLM")

        # print(html_content)

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content = extract(
            **kwargs, content=html_content_fits_context_window_llm
        )

        pprint.pprint(extracted_content)

    # Scrape and Extract with LLM
    asyncio.run(scrape_with_Async_loader(urls=[wsj_url], schema=SchemaNewsWebsites))
