import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def find_optimal_clusters(embeddings, max_clusters=10):
    """Find the optimal number of clusters using the Silhouette Score."""
    silhouette_scores = []
    n_samples = len(embeddings)
    cluster_range = range(2, min(max_clusters, n_samples) + 1)  # Ensure valid range

    for k in cluster_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(embeddings)
        if k > 1 and k < n_samples:  # Silhouette score requires 2 <= k < n_samples
            silhouette_scores.append(silhouette_score(embeddings, labels))

    # Find the number of clusters with the highest Silhouette Score
    if silhouette_scores:
        optimal_clusters = cluster_range[np.argmax(silhouette_scores)]
    else:
        optimal_clusters = 2  # Default to 2 clusters if no valid scores

    return optimal_clusters