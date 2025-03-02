import argparse
from pathlib import Path
from utils.file_utils import organize_files
from extractors.keyword_extractor import rename_files_based_on_content

def main(input_dir, output_dir, organize_rule, rename_files):
    """Main function to organize files."""
    supported_extensions = [".txt", ".pdf", ".docx", ".csv", ".xlsx", ".md", ".ppt", ".pptx"]
    file_paths = [fp for fp in Path(input_dir).rglob("*.*") if fp.is_file() and fp.suffix.lower() in supported_extensions]
    print(f"Found {len(file_paths)} files in {input_dir}")

    # Group files by type
    if organize_rule == "type":
        from organizers.type_organizer import group_files_by_type
        file_groups = group_files_by_type(file_paths)
        organize_files(file_groups, output_dir, "Type")
        print("Files organized by type successfully!")

    # Categorize files by size
    elif organize_rule == "size":
        from organizers.size_organizer import categorize_files_by_size
        file_groups = categorize_files_by_size(file_paths)
        organize_files(file_groups, output_dir, "Size")
        print("Files organized by size successfully!")

    # Cluster files based on content
    elif organize_rule == "content":
        from organizers.content_organizer import cluster_files
        file_groups = cluster_files(file_paths)
        if file_groups:
            organize_files(file_groups, output_dir, "Cluster")
            print("Files organized by content successfully!")

    # Rename files based on content
    if rename_files:
        rename_files_based_on_content(output_dir)

if __name__ == "__main__":
    # Set up CLI arguments
    parser = argparse.ArgumentParser(description="Organize files by type, size, or content.")
    parser.add_argument("--input_dir", type=str, required=True, help="Directory containing files to organize.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to store organized files.")
    parser.add_argument("--organize_rule", type=str, choices=["type", "size", "content"], required=True, help="Organize files by type, size, or content.")
    parser.add_argument("--rename_files", action="store_true", help="Rename files based on content using keyword extraction.")
    args = parser.parse_args()

    # Run the main function with user-provided directories
    main(input_dir=args.input_dir, output_dir=args.output_dir, organize_rule=args.organize_rule, rename_files=args.rename_files)