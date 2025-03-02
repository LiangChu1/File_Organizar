from collections import defaultdict

def categorize_files_by_size(file_paths):
    """Categorize files by size: small (<1MB), medium (1MB–10MB), large (>10MB)."""
    size_categories = defaultdict(list)
    for file in file_paths:
        size = file.stat().st_size  # Get file size in bytes
        if size < 1_000_000:  # <1MB
            size_categories["small"].append(file)
        elif size <= 10_000_000:  # 1MB–10MB
            size_categories["medium"].append(file)
        else:  # >10MB
            size_categories["large"].append(file)
    return size_categories