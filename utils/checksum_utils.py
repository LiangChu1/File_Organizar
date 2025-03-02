import hashlib

def calculate_checksum(file_path):
    """Calculate SHA256 checksum to verify file integrity."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error calculating checksum for {file_path}: {e}")
        return None