import fitz  # PyMuPDF

# Function to find the logo coordinates (assuming it is an image in all pages)
def find_logo_coordinates(pdf_file):
    # Open the PDF
    pdf_document = fitz.open(pdf_file)
    logo_rect = None  # This will store the coordinates of the logo

    # Loop through the pages to find the logo's coordinates (assuming it's an image)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        print(f"Scanning Page {page_num + 1} for images...")

        # Try-except to handle potential bad image errors
        try:
            # Extract all images from the page
            images = page.get_images(full=True)
            if images:
                for img_index, img_info in enumerate(images):
                    xref = img_info[0]
                    image_rect = page.get_image_bbox(xref)
                    print(f"  Found image {img_index + 1} on Page {page_num + 1} at {image_rect}")
                    
                    # If we are on the first page, capture the first image's bounding box as the logo
                    if page_num == 0:
                        logo_rect = image_rect
                        print(f"  Logo coordinates on Page 1: {logo_rect}")
                        break  # Assuming the first image is the logo we want to cover
                if logo_rect:
                    break  # Exit after finding the logo on the first page
        except Exception as e:
            print(f"Error processing images on page {page_num + 1}: {e}")
            continue  # Continue to the next page if there's an error

    pdf_document.close()

    # Return the logo coordinates found on the first page
    if logo_rect:
        return logo_rect
    else:
        raise ValueError("Logo not found on any page.")
# Function to cover the logo on all pages using the found coordinates
def cover_logo_in_pdf(input_pdf, output_pdf, logo_rect):
    # Open the input PDF
    pdf_document = fitz.open(input_pdf)

    # Loop through all the pages to cover the logo
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        print(f"Covering logo on Page {page_num + 1}...")

        # Draw a white rectangle to cover the logo at the specified location
        page.draw_rect(logo_rect, color=(1, 1, 1), fill=True, overlay=True)

    # Save the modified PDF as a new file
    pdf_document.save(output_pdf)
    pdf_document.close()
    print(f"Logo covered and saved to {output_pdf}")

if __name__ == "__main__":
    # Input and output file paths
    input_pdf = "SAKTI HYD GIFTING CATALOGUE-2.pdf"
    output_pdf = "your_output_file.pdf"

    # Step 1: Find the logo's coordinates on the first page
    try:
        logo_rect = find_logo_coordinates(input_pdf)
        print(f"Logo found at {logo_rect}, proceeding to cover it on all pages.")

        # Step 2: Cover the logo on all pages using the found coordinates
        cover_logo_in_pdf(input_pdf, output_pdf, logo_rect)

    except ValueError as e:
        print(e)
