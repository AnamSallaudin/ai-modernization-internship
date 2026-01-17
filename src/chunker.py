import json
from pathlib import Path


def load_entities():
    with open("output/entities.json", "r", encoding="utf-8") as f:
        return json.load(f)


def chunk_entities(entities):
    chunks = []

    for file_path, data in entities.items():
        for cls in data.get("classes", []):
            chunks.append({
                "id": f"{file_path}::{cls}",
                "text": f"Class {cls} is defined in {file_path}.",
                "source": file_path,
                "type": "class"
            })

        for fn in data.get("functions", []):
            chunks.append({
                "id": f"{file_path}::{fn}",
                "text": f"Function {fn} is defined in {file_path}.",
                "source": file_path,
                "type": "function"
            })

    return chunks


if __name__ == "__main__":
    entities = load_entities()
    chunks = chunk_entities(entities)

    Path("output").mkdir(exist_ok=True)

    with open("output/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    print(f"Generated {len(chunks)} chunks. Output written to output/chunks.json")
