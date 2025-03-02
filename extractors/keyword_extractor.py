import yake
import re
import os
from pathlib import Path
from extractors.text_extractor import extract_text

def extract_keywords_with_yake(text, n_grams=(2, 3)):
    """Extract word summaries using YAKE!."""
    kw_extractor = yake.KeywordExtractor()
    try:
        # Extract keywords with word phrases
        keywords = kw_extractor.extract_keywords(text)
        # Filter for word phrases
        filtered_keywords = [kw[0] for kw in keywords if len(kw[0].split()) in range(n_grams[0], n_grams[1] + 1)]
        return filtered_keywords[0] if filtered_keywords else None
    except Exception as e:
        print(f"Error extracting keywords with YAKE!: {e}")
        return None

def rename_files_based_on_content(output_dir):
    """Rename files based on their content using summarization."""
    for root, _, files in os.walk(output_dir):
        for file in files:
            file_path = Path(root) / file
            text = extract_text(file_path)
            if text:
                summary = extract_keywords_with_yake(text)
                if summary:
                    # Generate a new filename based on the summary
                    new_name = summary.replace(" ", "_")  # Replace spaces with underscores
                    new_name = re.sub(r'[^\w\-_\. ]', '_', new_name)  # Replace invalid characters
                    new_name = f"{new_name}{file_path.suffix}"  # Add original file extension
                    new_path = file_path.parent / new_name

                    # Rename the file
                    try:
                        file_path.rename(new_path)
                        print(f"Renamed {file_path.name} to {new_path.name}")
                    except Exception as e:
                        print(f"Error renaming {file_path.name}: {e}")