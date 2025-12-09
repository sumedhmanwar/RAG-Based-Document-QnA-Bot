from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction

ef = OllamaEmbeddingFunction(
    url="http://localhost:11434/api/embeddings",
    model_name="nomic-embed-text:latest"
)
print(ef(["hello world"]))



