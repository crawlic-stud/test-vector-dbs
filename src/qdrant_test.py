import sys
import time

from qdrant_client import QdrantClient

from pastas import get_pastas

# host with docker:
# https://qdrant.tech/documentation/quickstart/#download-and-run
client = QdrantClient("http://localhost:6333")

# texts = get_pastas()
# ids = list(range(len(texts)))

# client.add("my_collection", texts)

if __name__ == "__main__":
    start = time.perf_counter()

    search_result = client.query(
        collection_name="my_collection", query_text=sys.argv[1]
    )
    print(f"done in {time.perf_counter() - start:.2f} s")
    print([f"{r.score:.2f}: {r.document}" for r in search_result])
