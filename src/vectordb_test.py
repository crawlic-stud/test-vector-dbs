from docarray import BaseDoc
from docarray.typing import NdArray
from docarray import DocList
import numpy as np
from vectordb import InMemoryExactNNVectorDB, HNSWVectorDB

from pastas import get_pastas


_SHAPE = 512


class ToyDoc(BaseDoc):
    text: str = ""
    embedding: NdArray[_SHAPE]


# Specify your workspace path
db = HNSWVectorDB[ToyDoc](workspace="./workspace_path")

# Index a list of documents with random embeddings
doc_list = [
    ToyDoc(text=text, embedding=np.random.rand(_SHAPE)) for text in get_pastas()
]
db.index(inputs=DocList[ToyDoc](doc_list))

# Perform a search query
query = ToyDoc(text="стример", embedding=np.random.rand(_SHAPE))
results = db.search(inputs=DocList[ToyDoc]([query]), limit=10)


if __name__ == "__main__":
    # Print out the matches
    for m in results[0].matches:
        print(m.text)
