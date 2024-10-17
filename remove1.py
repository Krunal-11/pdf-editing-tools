import PyPDF2

def delete_first_page(input_pdf, output_pdf):
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        writer = PyPDF2.PdfWriter()
        
        for page_num in range(1, len(reader.pages)):
            writer.add_page(reader.pages[page_num])
        
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)
            print(f"Deleted the first page and saved to {output_pdf}")

if __name__ == "__main__":
    input_pdf = "final.pdf" 
    output_pdf = "final_page2.pdf"  
    delete_first_page(input_pdf, output_pdf)
