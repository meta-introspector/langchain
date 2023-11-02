#!/usr/bin/env python
# coding: utf-8
from langchain.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="mistral")
text = "This is a test document."
query_result = embeddings.embed_query(text)
print(query_result)
