import PyPDF2

def merge_pdfs(pdf_list, output_pdf):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Loop through the list of PDFs and add them to the writer
    for pdf in pdf_list:
        print(f"Processing: {pdf}")
        try:
            with open(pdf, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page in range(len(reader.pages)):
                    pdf_writer.add_page(reader.pages[page])
                    print(f"Added page {page + 1} from {pdf}")
        except Exception as e:
            print(f"Failed to process {pdf}: {e}")

    # Write the merged PDF to a file
    try:
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)
            print(f"Merged PDF saved as: {output_pdf}")
    except Exception as e:
        print(f"Failed to save merged PDF: {e}")

if __name__ == "__main__":
    # List of PDFs to merge
    pdf_files = ["final_page1.pdf", "final_page2.pdf"]

    # Output PDF file name
    output_pdf_file = "gifting catalogue new guru enterprises.pdf"

    # Call the function to merge the PDFs
    merge_pdfs(pdf_files, output_pdf_file)
