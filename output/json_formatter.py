def format_to_json(modules):
    formatted_output = []

    for module in modules:
        formatted_output.append({
            "module": module["module"].strip(),
            "Description": module["Description"].strip(),
            "Submodules": {
                sub.strip(): desc.strip()
                for sub, desc in module["Submodules"].items()
            }
        })

    return formatted_output
