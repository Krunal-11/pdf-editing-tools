import PyPDF2

def split_pdf(input_pdf, output_pdf_prefix):
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)
        print(f"Total pages in PDF: {total_pages}")

        pages_per_pdf = 4

        for i in range(15):
            start_page = i * pages_per_pdf
            end_page = start_page + pages_per_pdf
            if i == 9:
                end_page = total_pages
            writer = PyPDF2.PdfWriter()
            for page_num in range(start_page, end_page):
                if page_num < total_pages:
                    writer.add_page(reader.pages[page_num])
            output_pdf = f"{output_pdf_prefix}_part_{i + 1}.pdf"
            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)
                print(f"Saved: {output_pdf}")

if __name__ == "__main__":
    input_pdf = "SAKTI HYD GIFTING CATALOGUE-2.pdf"

    output_pdf_prefix = "split_output"

    # Call the function to split the PDF
    split_pdf(input_pdf, output_pdf_prefix)
