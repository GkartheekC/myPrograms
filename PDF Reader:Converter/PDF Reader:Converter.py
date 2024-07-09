# importing the required modules 
from PyPDF2 import PdfReader, PdfWriter 

# import module
import fitz
  
def PDFsplit(pdf, splits): 
    # creating pdf reader object 
    reader = PdfReader(pdf) 
  
    # starting index of first slice 
    start = 0
  
    # starting index of last slice 
    end = splits[0] 
  
  
    for i in range(len(splits)+1): 
        # creating pdf writer object for (i+1)th split 
        writer = PdfWriter() 
  
        # output pdf file name 
        outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'
        print(outputpdf)
        # adding pages to pdf writer object 
        print(start)
        print(end)
        for page in range(start,end): 
            writer.add_page(reader.pages[page]) 
            # writing split pdf pages to pdf file 
            with open(outputpdf, "wb") as f: 
                writer.write(f) 
            # interchanging page split start position for next split 
        start = end
        document = fitz.open(outputpdf)
        zoom = 4
        mat = fitz.Matrix(zoom, zoom)
        pngfile = document.load_page(0)
        pix = pngfile.get_pixmap(matrix=mat)
        outputfile = pdf.split('.pdf')[0] + str(i) + '.png'
        pix.save(outputfile) 
        try: 
            print("check")
            # setting split end position for next split 
            end = splits[i+1] 
        except IndexError: 
            # setting split end position for last split 
            end = len(reader.pages) 
                
  
  
def main(): 
    # pdf file to split 
    pdf = 'example.pdf'

    # creating pdf reader object 
    reader = PdfReader(pdf)
  
    # split page positions 
    splits = []
    for i in range(len(reader.pages)):
        splits.append(i+1)
  
    # calling PDFsplit function to split pdf 
    PDFsplit(pdf, splits) 
  

# calling the main function 
main() 