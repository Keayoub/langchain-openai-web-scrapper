import requests
import re
import pprint
from bs4 import BeautifulSoup

from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_playwright, scrape_with_playwright_ai
from scrape import scrape

url = "https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
# Extract all the text content. This approach is generalized and
# might not always yield perfect results for all websites.
content_text = soup.get_text()
html_content = response.text
tags_to_extract = ["span", "p", "li"]
extracted_content = scrape(url, tags_to_extract)
pprint.pprint(extracted_content)
