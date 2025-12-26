import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_documentation(start_urls, max_pages=100):
    visited = set()
    to_visit = list(start_urls)
    pages = {}

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        try:
            response = requests.get(current_url, timeout=10)
            if response.status_code != 200:
                continue
        except requests.RequestException:
            continue

        visited.add(current_url)
        pages[current_url] = response.text

        soup = BeautifulSoup(response.text, "html.parser")
        base_domain = urlparse(current_url).netloc

        for link in soup.find_all("a", href=True):
            href = link["href"].strip()

            # Ignore unwanted links
            if href.startswith(("mailto:", "tel:", "#")):
                continue
            if any(href.endswith(ext) for ext in {".pdf", ".jpg", ".png", ".zip"}):
                continue

            absolute_url = urljoin(current_url, href)
            parsed = urlparse(absolute_url)

            # Crawl only same domain
            if parsed.netloc == base_domain and absolute_url not in visited:
                to_visit.append(absolute_url.rstrip("/"))

    return pages
