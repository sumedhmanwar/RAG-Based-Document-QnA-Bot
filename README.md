# RAG-Based-Document-QnA-Bot-
v1 - 
Developed a RAG system for querying documents using natural language.
Utilized LangChain to process and chunk documents from a HuggingFace Dataset, created embeddings. Stored and
indexed vector embeddings in ChromaDb to enable efficient semantic search and retrieval, optimized it using semantic
cache. Integrated a LLama LLM to generate context-based answers from retrieved data via Streamlit interface


V2 with Semantic Cache- 

1. We are uploading questions and answers (of that could be highly popular) in redis.
2. When a question is passed, we are seeing how similar it is with our redis cache questions using cosine similarity between query and key (redis question) embedding. 
3. If it is high, we are giving answer from cache, that is way faster. 
4. 