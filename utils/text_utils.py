import re

def preprocess_text(text):
    """Preprocess text by removing special characters and normalizing spaces."""
    text = re.sub(r'\s+', ' ', text)  # Normalize spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text.lower().strip()

def split_text_into_chunks(text, tokenizer, max_tokens=500):
    """Split long text into chunks that fit within the model's token limit."""
    tokens = tokenizer.tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0

    for token in tokens:
        current_chunk.append(token)
        current_length += 1
        if current_length >= max_tokens:
            chunks.append(tokenizer.convert_tokens_to_string(current_chunk))
            current_chunk = []
            current_length = 0

    if current_chunk:
        chunks.append(tokenizer.convert_tokens_to_string(current_chunk))

    return chunks