import json


def get_pastas() -> list[str]:
    with open("src/motya.pastas.json", encoding="utf-8") as f:
        objects = json.load(f)

    return [obj.get("text", "") for obj in objects]
