import re
import base64
import json

def call(html):
    # Find matches
    data = []
    patterns = [
        # {
        #     "type": "json",
        #     "encoded": False,
        #     "encoding": "utf-8",
        #     "pattern": r'<script\s+type="application/ld\+json">\s*(\{.*?\})\s*<\/script>'
        # },
        # {
        #     "type": "json",
        #     "encoded": False,
        #     "encoding": "utf-8",
        #     "pattern": r'<script\s+type="application/ld\+json"\s+data-testid="[^"]+">\s*(\{.*?\})\s*<\/script>'
        # },
        {
            "type": "json",
            "encoded": True,
            "encoding": "utf-8",
            "pattern": r'(?<=<!--)[A-Za-z0-9+/=]+(?=-->)'
        }
    ]
    # Process each pattern
    for pattern in patterns:
        matches = re.findall(pattern["pattern"], html.decode("utf-8"), re.DOTALL)
        for match in matches:
            if pattern["encoded"]:  
                # If it's Base64-encoded, decode it
                try:
                    data.append(json.loads(base64.b64decode(match).decode(pattern["encoding"])))
                except Exception:
                    pass
            else:
                data.append(json.loads(match))
    return data