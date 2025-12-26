def build_hierarchy(cleaned_content):
    modules = []
    current_module = None
    current_submodule = None

    for item in cleaned_content:
        tag = item["tag"]
        text = item["text"]

        if tag == "h1":
            if current_module:
                modules.append(current_module)

            current_module = {
                "module": text,
                "Description": "",
                "Submodules": {}
            }
            current_submodule = None

        elif tag == "h2" and current_module:
            current_submodule = text
            current_module["Submodules"][current_submodule] = ""

        elif tag in ["p", "li"]:
            if current_submodule:
                current_module["Submodules"][current_submodule] += text + " "
            elif current_module:
                current_module["Description"] += text + " "

    if current_module:
        modules.append(current_module)

    return modules
