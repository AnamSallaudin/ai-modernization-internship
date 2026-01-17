import sys
import json
import re
from pathlib import Path


def extract_entities(code: str):
    classes = re.findall(r"class\s+(\w+)", code)
    functions = re.findall(r"def\s+(\w+)", code)
    return classes, functions


def analyze_directory(target_dir: str):
    results = {}

    for path in Path(target_dir).rglob("*.py"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
        except Exception:
            continue

        classes, functions = extract_entities(code)

        if classes or functions:
            results[str(path)] = {
                "classes": classes,
                "functions": functions
            }

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <path-to-code>")
        sys.exit(1)

    target_dir = sys.argv[1]
    results = analyze_directory(target_dir)

    Path("output").mkdir(exist_ok=True)

    with open("output/entities.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Analyzed {len(results)} files. Output written to output/entities.json")
