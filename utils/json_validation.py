import re
import json

def extract_json_block(text: str) -> dict:
    match = re.search(r'\{[\s\S]*\}', text)
    if not match:
        raise ValueError("Tidak ditemukan blok JSON")

    json_str = match.group(0)
    return json.loads(json_str)