import PyPDF2

def split_pdf(input_pdf, output_pdf_prefix):
    # Open the input PDF file
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)

        print(f"Total pages in PDF: {total_pages}")

        # Save the first page as a separate PDF
        if total_pages > 0:
            writer_first = PyPDF2.PdfWriter()
            writer_first.add_page(reader.pages[0])
            output_first_page = f"{output_pdf_prefix}_part_1.pdf"
            with open(output_first_page, 'wb') as output_file:
                writer_first.write(output_file)
                print(f"Saved: {output_first_page}")

        # Save all remaining pages (2 to total_pages) as a single PDF
        if total_pages > 1:
            writer_rest = PyPDF2.PdfWriter()
            for page_num in range(1, total_pages):
                writer_rest.add_page(reader.pages[page_num])

            output_rest_pages = f"{output_pdf_prefix}_part_2.pdf"
            with open(output_rest_pages, 'wb') as output_file:
                writer_rest.write(output_file)
                print(f"Saved: {output_rest_pages}")

if __name__ == "__main__":
    # Input PDF path
    input_pdf = "final.pdf"

    # Output file prefix
    output_pdf_prefix = "split_output"

    # Call the function to split the PDF
    split_pdf(input_pdf, output_pdf_prefix)
