# crawler/url_validator.py
from urllib.parse import urlparse

def validate_and_normalize_urls(urls):
    valid_urls = set()

    for url in urls:
        if not url:
            continue

        parsed = urlparse(url)
        #print(parsed)
        if parsed.scheme not in ["http", "https"]:
            raise ValueError(f"Invalid URL scheme: {url}")
        if not parsed.netloc:
            raise ValueError(f"Invalid URL (missing domain): {url}")
        normalized_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip("/")

        valid_urls.add(normalized_url)

    return list(valid_urls)

"""if __name__ == "__main__":
    test_urls = [
        "http://example.com",
        "https://example.com/",
        "http://example.com/path"
    ]

    try:
        valid_urls = validate_and_normalize_urls(test_urls)
        print("Valid URLs:", valid_urls)
    except ValueError as e:
        print("Error:", e)"""