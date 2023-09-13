import argparse
import os
from pdftolatex.pdf import *

def convert(filepath):
    """Convert pdf at filepath to .tex file"""
    
    # Define source and target directories
    source_dir = '../data'
    target_dir = '../latex_output'
    
    # Create target directory if it doesn't exist
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)

    # Check if filepath is a directory
    if os.path.isdir(filepath):
        for f in os.listdir(filepath):
            full_path = os.path.join(filepath, f)
            if os.path.isfile(full_path):  # Skip directories
                convert(full_path)
        return
    
    # Skip if not a PDF
    if not filepath.lower().endswith('.pdf'):
        return
    
    # Extract filename without extension
    filename = os.path.splitext(os.path.basename(filepath))[0]
    
    # Full path to the source PDF file
    source_pdf_path = os.path.join(source_dir, filename + '.pdf')
    
    # Full path to the target LaTeX file
    target_tex_path = os.path.join(target_dir, f"{filename}.tex")
    
    # Convert PDF to LaTeX (assuming PDF and TexFile classes are defined in pdftolatex.pdf)
    pdf = PDF(source_pdf_path)
    texfile = TexFile(pdf)
    texfile.generate_tex_file(target_tex_path)


def main():   
    parser = argparse.ArgumentParser(description="Generate a .tex file from a .pdf file.")
    print("generate tex done")
    parser.add_argument('--filepath', type=str, help="Path to pdf to be converted")
    print("generate path to pdf to be converted")
    parser.add_argument('--folderpath', type=str, help="Path to folder containing pdfs to be converted. All pdfs in the folder will be converted")
    print("gnerate path to folder containing pdfs to be converted")
    
    args = parser.parse_args()

    filepath = args.filepath
    folderpath = args.folderpath

    if folderpath:
        folderpath = os.path.join('data', folderpath)  # Assuming the folder is inside 'data'
        convert(folderpath)
    else:
        filepath = os.path.join('data', filepath)  # Assuming the file is inside 'data'
        convert(filepath)

if __name__ == "__main__":
    main()
