from pdf2docx import Converter

def pdf_to_word(input_pdf, output_docx):
    # Create a converter object
    cv = Converter(input_pdf)
    
    # Convert PDF to Word document
    cv.convert(output_docx, start=0, end=None)  # Start=0, end=None will convert all pages
    
    # Close the converter
    cv.close()
    print(f"Conversion complete. Word file saved as {output_docx}")

if __name__ == "__main__":
    # Input PDF file path
    input_pdf = "SAKTI HYD GIFTING CATALOGUE-2.pdf"
    
    # Output Word file path
    output_docx = "output_file.docx"
    
    # Call the conversion function
    pdf_to_word(input_pdf, output_docx)
