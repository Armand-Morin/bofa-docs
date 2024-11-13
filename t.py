import sys
from PyPDF2 import PdfReader
from markdownify import markdownify as md
import os
import re

def extract_text_from_pdf(pdf_path):
    try:
        pdf = PdfReader(pdf_path)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

def convert_to_markdown(text):
    # Improve hyperlink and Markdown formatting
    text = re.sub(r'\((http[^\s]+)\)', r'[\1](\1)', text)  # Convert URLs to Markdown links if needed
    return md(text, heading_style="ATX")  # Use ATX style (# for headings)

def get_pdf_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.pdf')]

def save_markdown_file(markdown_text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
    except Exception as e:
        print(f"Error saving {output_path}: {e}")

input_directory = "/Users/armandmorin/Documents/GitHub/bofa-docs"
output_directory = os.path.join(input_directory, 'out')

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

pdf_files = get_pdf_files(input_directory)

for pdf_file in pdf_files:
    print('Converting', pdf_file)
    pdf_path = os.path.join(input_directory, pdf_file)
    text = extract_text_from_pdf(pdf_path)
    if text:
        markdown_text = convert_to_markdown(text)
        output_path = os.path.join(output_directory, pdf_file.replace('.pdf', '.md'))
        save_markdown_file(markdown_text, output_path)
        print(f'Saved: {output_path}')
    else:
        print(f"Skipping {pdf_file} (no text found)")
