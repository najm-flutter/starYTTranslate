from google import genai
from google.genai import types
import os

from file_paths import API_KEY

MODLE = "gemini-2.5-pro"
PROMPT = """

You are a professional English-to-Arabic subtitle translator with expertise across various fields, including but not limited to technology, science, medicine, business, education, and entertainment.

Translate the following YouTube subtitle blocks into Arabic, while strictly preserving the following:

✅ The same number of subtitle blocks as the input.
✅ The timestamps and subtitle structure (1 or 2 lines per block).
✅ Do not merge, remove, or split any blocks.
✅ Each Arabic translation line must correspond 1-to-1 with the original.

🔷 Additional rules for field-specific terms:

If a subtitle contains a technical or specialized term (e.g., from medicine, law, computer science, engineering, economics, etc.), translate it using this format:
(Arabic meaning)[Original English term]

Example: [loop] (حلقة), [arthritis] (التهاب المفاصل)


For general content (conversations, stories, interviews, etc.), prioritize natural and culturally fluent Arabic.
Do not translate timestamps or modify the subtitle structure.
the output only srt form 
the translate language is arabic
"""


def api_key():
    try:
        with open(API_KEY) as file:
            return file.read().strip()
    except Exception:
        return None


def test_connected(api_key):
    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model=MODLE,
            contents=[
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text="hi")],
                )
            ],
        )
        return response.text
    except Exception:
        return None


def is_api_key_stored() -> bool:
    if not os.path.exists(API_KEY):
        return False
    with open(API_KEY) as file:
        return True if file.read().strip() else False
