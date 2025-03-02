from collections import defaultdict
from utils.embedding_utils import get_text_embeddings
from utils.clustering_utils import find_optimal_clusters
from utils.text_utils import preprocess_text
from extractors.text_extractor import extract_text
from sklearn.cluster import KMeans

def cluster_files(file_paths):
    """Cluster files based on extracted text or filenames."""
    texts = []
    valid_files = []

    for fp in file_paths:
        text = extract_text(fp)
        if text:
            text = preprocess_text(text)
            texts.append(text)
            valid_files.append(fp)
        else:
            print(f"Skipping {fp} (no extractable content)")

    if not texts:
        print("No valid text extracted. Exiting.")
        return {}

    embeddings = get_text_embeddings(texts)
    n_samples = len(embeddings)

    # Handle edge cases
    if n_samples == 1:
        print("Only one file with valid text. No clustering needed.")
        return {0: valid_files}
    elif n_samples == 2:
        print("Only two files with valid text. Defaulting to 2 clusters.")
        return {0: [valid_files[0]], 1: [valid_files[1]]}

    optimal_clusters = find_optimal_clusters(embeddings)
    print(f"Optimal number of clusters: {optimal_clusters}")

    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings)

    clustered_files = defaultdict(list)
    for file, label in zip(valid_files, labels):
        clustered_files[label].append(file)

    return clustered_files