import os
import shutil
from pathlib import Path
from utils.checksum_utils import calculate_checksum

def organize_files(file_groups, output_dir, group_name):
    """Move files into organized folders based on a grouping rule."""
    os.makedirs(output_dir, exist_ok=True)

    for group, files in file_groups.items():
        group_dir = Path(output_dir) / f"{group_name}_{group}"
        group_dir.mkdir(parents=True, exist_ok=True)

        for file in files:
            destination = group_dir / file.name
            try:
                original_checksum = calculate_checksum(file)
                shutil.copy2(file, destination)  # Use copy2 to preserve metadata
                new_checksum = calculate_checksum(destination)

                if original_checksum == new_checksum:
                    file.unlink()  # Delete original only if copy is identical
                    print(f"Moved {file} to {destination} successfully.")
                else:
                    print(f"Warning: Checksum mismatch, not deleting {file}!")
            except Exception as e:
                print(f"Error moving {file} to {destination}: {e}")