import numpy as np
from transformers import pipeline, AutoTokenizer
from utils.text_utils import split_text_into_chunks

def get_text_embeddings(texts, model="sentence-transformers/all-mpnet-base-v2"):
    """Generate embeddings for texts, handling long texts by chunking."""
    tokenizer = AutoTokenizer.from_pretrained(model)
    embedder = pipeline("feature-extraction", model=model, tokenizer=model)

    embeddings = []
    for text in texts:
        # Split long text into chunks
        chunks = split_text_into_chunks(text, tokenizer)
        if not chunks:
            embeddings.append(np.zeros(embedder.model.config.hidden_size))  # Default embedding
            continue

        # Compute embeddings for each chunk
        chunk_embeddings = [np.mean(embedder(chunk)[0], axis=0) for chunk in chunks]
        # Average embeddings of all chunks
        embeddings.append(np.mean(chunk_embeddings, axis=0))

    return embeddings