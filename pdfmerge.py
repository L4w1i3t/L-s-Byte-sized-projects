import os
from PyPDF2 import PdfMerger

merger = PdfMerger()
current_dir = os.getcwd()

pdf_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.pdf')]

if not pdf_files:
    print("No PDF files found in the current directory.")
else:
    pdf_files.sort()
    for pdf in pdf_files:
        try:
            merger.append(os.path.join(current_dir, pdf))
            print(f"Merged: {pdf}")
        except Exception as e:
            print(f"Error merging {pdf}: {e}")

    try:
        merger.write("merged.pdf")
        merger.close()
        print("PDF files have been merged successfully into 'merged.pdf'.")
    except Exception as e:
        print(f"Error writing merged PDF: {e}")