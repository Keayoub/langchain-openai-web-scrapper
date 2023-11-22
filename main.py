import pprint
from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_playwright, scrape_with_playwright_ai


# TESTING
if __name__ == "__main__":    

    # News sites mostly have <span> tags to scrape
    urls = [
        "https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/"
    ]
    schema = {
        "properties": {
            "title": {"type": "string"},
            "description": {"type": "string"}
        },
        "required": ["title", "description"],
    }

    tags_to_extract = ["span", "p", "li"]
    extracted_content = scrape_with_playwright_ai(urls, schema=schema)
    pprint.pprint(extracted_content)
