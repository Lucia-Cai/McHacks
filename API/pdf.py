from PyPDF2 import PdfReader 


def extract_text_from_pdf(pdf_path):
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PdfReader object
        pdf_reader = PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Initialize an empty string to store the extracted text
        extracted_text = ""

        # Iterate through each page and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text().replace('\n',' ')

    return extracted_text





if __name__ == "__main__":
    t = extract_text_from_pdf('test.pdf')
    print(t)
