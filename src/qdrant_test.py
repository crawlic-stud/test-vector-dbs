import time
from qdrant_client.models import PointStruct
import numpy as np
from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient

from pastas import get_pastas

client = QdrantClient("/qdrant-db")

texts = get_pastas()
ids = list(range(len(texts)))

client.add(
    "my_collection",
    texts
)

if __name__ == "__main__":
    start = time.perf_counter()
    
    search_result = client.query(
        collection_name="my_collection",
        query_text="я гей"
    )
    print(f"done in {time.perf_counter - start:.2f} s")
    print(search_result)