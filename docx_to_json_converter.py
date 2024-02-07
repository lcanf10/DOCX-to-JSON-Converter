import json
import glob
from docx import Document

def docx_to_json(docx_path, json_file_path):
    print(f"Processing: {docx_path}")  # Debugging: Print the file being processed
    doc = Document(docx_path)
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip() != '']
    if not paragraphs:  # Check if paragraphs list is empty
        print(f"No content found in {docx_path}")
        return  # Skip empty documents
    data = {'paragraphs': paragraphs}
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Converted to {json_file_path}")  # Confirmation message

def convert_folder(docx_folder_path, output_folder_path):
    docx_files = glob.glob(f"{docx_folder_path}/*.docx")
    if not docx_files:  # Check if the list of files is empty
        print(f"No DOCX files found in {docx_folder_path}")
        return
    for docx_file in docx_files:
        json_file_name = f"{output_folder_path}/{docx_file.split('/')[-1].replace('.docx', '.json')}"
        docx_to_json(docx_file, json_file_name)

# Update these paths according to your setup
docx_folder_path = '/path/to/your/docx/folder'
output_folder_path = '/path/to/your/output/json/folder'

convert_folder(docx_folder_path, output_folder_path)
