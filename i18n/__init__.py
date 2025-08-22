import json
from pathlib import Path

_locales = {}

for file in Path(__file__).parent.glob("*.json"):
    _locales[file.stem] = json.loads(file.read_text(encoding="utf-8"))

def i18n(lang: str, key: str) -> str:
    return _locales.get(lang, _locales["ru"]).get(key, key)
