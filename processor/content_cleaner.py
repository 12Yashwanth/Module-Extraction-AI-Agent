def clean_content(extracted_elements):
    cleaned = []
    seen_texts = set()

    for item in extracted_elements:
        text = item["text"]

        if len(text) < 20:
            continue

        if text.lower() in seen_texts:
            continue

        seen_texts.add(text.lower())

        text = " ".join(text.split())

        cleaned.append({
            "tag": item["tag"],
            "text": text
        })

    return cleaned
