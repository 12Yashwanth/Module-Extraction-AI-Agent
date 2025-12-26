import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("sk-efgh5678efgh5678efgh5678efgh5678efgh5678"))

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a documentation analysis assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

MODULE_PROMPT = """
You are an AI assistant analyzing product documentation.

Using ONLY the information provided below, generate:
1. A clear and detailed description of the MODULE
2. Clear and accurate descriptions for each SUBMODULE

Do NOT add any information not present in the text.
Do NOT assume functionality.

Documentation Content:
{content}

Return the result in plain text.
"""


def refine_module_descriptions(module_data):
    combined = module_data["Description"]

    for sub, desc in module_data["Submodules"].items():
        combined += f"\n{sub}: {desc}"

    prompt = MODULE_PROMPT.format(content=combined)

    refined_text = call_llm(prompt)

    module_data["Description"] = refined_text
    return module_data

if __name__ == "__main__":
    sample_module = {
        "module": "SampleModule",
        "Description": "This module handles sample operations.",
        "Submodules": {
            "SubmoduleA": "Handles part A of the operations.",
            "SubmoduleB": "Handles part B of the operations."
        }
    }

    refined = refine_module_descriptions(sample_module)
    print(refined)  