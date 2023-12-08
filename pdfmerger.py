import PyPDF2
import sys
import os
from pypdf import PdfWriter

merger = PdfWriter()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
        
merger.write(f"{sys.argv[1]}.pdf")

# merger.write("combine.pdf")
merger.close()