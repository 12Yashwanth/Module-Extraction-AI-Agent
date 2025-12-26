from bs4 import BeautifulSoup

def extract_main_content(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    main_content = (
        soup.find("main") or
        soup.find("article") or
        soup.find("div", {"role": "main"}) or
        soup.find("section") or
        soup.body
    )

    if not main_content:
        return ""

    extracted_text = []

    for element in main_content.find_all(["h1", "h2", "h3", "p", "li", "table"]):
        text = element.get_text(strip=True)
        if text:
            extracted_text.append({
                "tag": element.name,
                "text": text
            })

    return extracted_text

print(extract_main_content("<html><body><main><h1>Title</h1><p>This is a paragraph.</p></main></body></html>"))
