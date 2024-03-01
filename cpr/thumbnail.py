from pdf2image import convert_from_path

import os

# Get the directory of the current Python script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the directory where your PDF files are located (same directory as the script)
pdf_directory = current_directory

# Get a list of all files in the directory
all_files = os.listdir(pdf_directory)

# Filter only the PDF files
pdf_files = [file for file in all_files if file.endswith('.pdf')]

# List of PDF file paths
#pdf_files = ['interface1.pdf', 'interface2.pdf', 'interface3.pdf', 'easy_mode.pdf', 'black_chrome.pdf', 'black_chrome_plus.pdf', 'danger_gal_dossier.pdf', 'night_market_index.pdf']

# Specify the path to the directory containing the poppler binaries
poppler_path = r'C:\poppler-24.02.0\Library\bin'

for pdf_file in pdf_files:
    # Convert the first page of the PDF file to an image
    images = convert_from_path(pdf_file, first_page=1, last_page=1, poppler_path=poppler_path)

    # Save the image as a JPEG file
    image_path = f"images/{pdf_file.split('.')[0]}.jpg"
    images[0].save(image_path, 'JPEG')
