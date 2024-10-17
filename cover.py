import fitz  # PyMuPDF

# Function to cover the logo at the same position on all pages
def cover_logo_in_pdf(input_pdf, output_pdf, logo_rect):
    # Open the input PDF
    pdf_document = fitz.open(input_pdf)
    cover_color = (228 / 255, 247 / 255, 241 / 255)
    
    # Loop through all the pages
    for page_num in range(2,pdf_document.page_count):
        page = pdf_document[page_num]
        print('covering page ',page)
        # Define a white rectangle to cover the logo (or change the color as needed)
        page.draw_rect(logo_rect, color=cover_color, fill=True, overlay=True)
        
    # Save the modified PDF as a new file
    pdf_document.save(output_pdf)
    pdf_document.close()

if __name__ == "__main__":
    # Input and output file paths
    input_pdf = "SAKTI HYD GIFTING CATALOGUE-2.pdf"
    output_pdf = "SAKTI HYD GIFTING CATALOGUE-2_covered_rect1(1).pdf"

    # Define the rectangle where the logo is located (x0, y0, x1, y1)
    # You need to adjust these values to match the position and size of the logo on your PDF
    logo_rect = fitz.Rect(28, 35, 100, 100)
    logo_rect_1 = fitz.Rect(20, 15, 128, 130)

    # Call the function to cover the logo
    cover_logo_in_pdf(input_pdf, output_pdf, logo_rect_1)

    print(f"Logo covered and saved to {output_pdf}")
