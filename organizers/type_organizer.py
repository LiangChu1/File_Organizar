from collections import defaultdict

def group_files_by_type(file_paths):
    """Group files by their type (e.g., PDF, DOCX, TXT)."""
    file_types = defaultdict(list)
    for file in file_paths:
        file_types[file.suffix.lower()].append(file)
    return file_types