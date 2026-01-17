import json
import sys


def load_chunks():
    with open("output/chunks.json", "r", encoding="utf-8") as f:
        return json.load(f)


def retrieve(query, chunks, top_k=5):
    query = query.lower()
    scored = []

    for chunk in chunks:
        text = chunk["text"].lower()
        score = sum(1 for word in query.split() if word in text)

        if score > 0:
            scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [chunk for _, chunk in scored[:top_k]]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python retriever.py <query>")
        sys.exit(1)

    query = sys.argv[1]
    chunks = load_chunks()
    results = retrieve(query, chunks)

    print(f"\nQuery: {query}\n")
    if not results:
        print("No relevant chunks found.")
    else:
        for i, chunk in enumerate(results, 1):
            print(f"{i}. [{chunk['type']}] {chunk['text']}")
