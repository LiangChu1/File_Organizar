# AI-Powered File Organizer

## Overview
AI-Powered File Organizer is a smart CLI application designed to help users automatically organize their text-based documents into structured folders. Leveraging advanced AI techniques, the application categorizes files based on user-defined criteria such as file type, size, or document content. This eliminates the need for manual sorting, enabling users to maintain a clean and efficient file system effortlessly.

## How to Use
1. Install Dependencies:
Ensure all required libraries are installed using pip:
`pip install numpy scikit-learn transformers PyPDF2 python-docx pandas python-pptx yake`
2. Run the Application:
Use the command-line interface to organize files:
`python organize_files.py --input_dir /path/to/input --output_dir /path/to/output --organize_rule type|size|content --rename_files`
- `--input_dir`: Directory containing files to organize.
- `--output_dir`: Directory to store organized files.
- `--organize_rule`: Choose between type, size, or content for organizing files.
- `--rename_files`: (Optional) Rename files based on their content.

## Prerequisites
1. Python: The core programming language used for developing the application.
2. Hugging Face Transformers: Utilized for generating high-quality sentence embeddings using the sentence-transformers/all-mpnet-base-v2 model. This model is ideal for tasks like semantic similarity, clustering, and retrieval.
3. YAKE! (Yet Another Keyword Extractor): A lightweight keyword extraction tool used for summarizing and renaming files based on their content.
4. PyPDF2: A library for extracting text from PDF files.
5. python-docx: A library for extracting text from DOCX files.
6. pandas: Used for handling CSV and Excel files, extracting their content for processing.
7. python-pptx: A library for extracting text from PowerPoint (PPT and PPTX) files.
8. scikit-learn: Used for clustering text embeddings with the KMeans algorithm and evaluating clustering quality using the Silhouette Score.
9. argparse: Provides a command-line interface for user interaction.
10. numpy: Used for numerical operations, particularly in handling embeddings.
11. hashlib: Ensures file integrity by calculating SHA256 checksums during file operations.
12. shutil: Handles file operations like copying and moving files.
13. pathlib: Simplifies file path manipulations.

## Features
1. Organize Files into Tiered Folders:
- By File Type: Group files with similar formats together (e.g., .txt, .pdf, .docx, .csv, .xlsx, .md, .ppt, .pptx).
- By Size: Categorize files into small (<1MB), medium (1MB–10MB), and large (>10MB) size ranges.
- By Content: Use AI to analyze the text inside documents and intelligently group related files based on semantic similarity.

2. AI-Powered Categorization:
- Extract text from documents and convert it into embeddings using the Hugging Face all-mpnet-base-v2 model.
- Cluster documents based on their embeddings to group semantically similar files.
- Use the Silhouette Score to determine the optimal number of clusters for improved accuracy.

3. File Renaming:
- Automatically rename files based on their content using YAKE! keyword extraction.
- Generate meaningful filenames by summarizing the document's content.

4. File Integrity Checks:
- Verify file integrity during operations using SHA256 checksums to ensure no data corruption occurs.

5. User-Friendly Interface:
- Customize organization rules via a simple command-line interface.
- Supports batch processing of files in a directory.

## AI Approaches
### Text Embedding and Clustering
1. Text Extraction:
- Extract text from various file formats (PDF, DOCX, CSV, XLSX, PPT, PPTX, TXT, MD).
- Preprocess text by removing special characters and normalizing spaces.

2. Text Embedding:
- Use the Hugging Face all-mpnet-base-v2 model to convert text into high-dimensional embeddings.
- Handle long texts by splitting them into chunks and averaging their embeddings.

3. Clustering:
- Apply KMeans clustering to group embeddings based on semantic similarity.
- Use the Silhouette Score to determine the optimal number of clusters.

4. File Organization:
- Move files into folders based on their assigned clusters.

### File Renaming
1. Keyword Extraction:
- Use YAKE! to extract meaningful keywords from the document's content.
- Focus on word phrases (e.g., 2-3 grams) for better summarization.

2. Renaming:
- Generate new filenames based on the extracted keywords.
- Replace spaces and special characters with underscores for compatibility.

## Future Enhancements
- Cloud Storage Integration: Support for organizing files stored in cloud platforms like Google Drive, Dropbox, or OneDrive.
- Advanced AI Models: Incorporate more sophisticated models for better categorization and summarization.
- Support for Additional File Types: Extend functionality to handle images, videos, and other media formats.
- Desktop/Mobile App: Convert the application into a standalone desktop or mobile app for broader accessibility.
- User Interface: Develop a graphical user interface (GUI) for easier interaction and customization.
- Automated Scheduling: Add the ability to schedule periodic file organization tasks.
- Multilingual Support: Extend text extraction and keyword extraction capabilities to support multiple languages.