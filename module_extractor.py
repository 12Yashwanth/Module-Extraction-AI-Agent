import argparse
import json
import logging

from crawler.url_validator import validate_and_normalize_urls
from crawler.crawler import crawl_documentation
from processor.content_extract import extract_main_content
from processor.content_cleaner import clean_content
from processor.hierarchy_builder import build_hierarchy
from output.json_formatter import format_to_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline(urls):
    logger.info("Validating URLs...")
    urls = validate_and_normalize_urls(urls)

    logger.info("Crawling documentation...")
    pages = crawl_documentation(urls)

    logger.info("Extracting and cleaning content...")
    all_content = []
    for html in pages.values():
        extracted = extract_main_content(html)
        cleaned = clean_content(extracted)
        all_content.extend(cleaned)

    logger.info("Building module hierarchy...")
    hierarchy = build_hierarchy(all_content)

    logger.info("Formatting output...")
    return format_to_json(hierarchy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pulse Module Extraction AI Agent")
    parser.add_argument(
        "--urls",
        nargs="+",
        required=True,
        help="List of documentation URLs"
    )
    args = parser.parse_args()

    try:
        output = run_pipeline(args.urls)
        print(json.dumps(output, indent=2))
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
