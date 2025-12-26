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
