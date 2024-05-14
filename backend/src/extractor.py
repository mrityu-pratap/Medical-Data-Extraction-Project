from pdf2image import convert_from_path
import pytesseract
import util
from parser_prescription import PrescriptionParser
from parser_pd import PatientDetailsParser

POPPLER_PATH = r'E:\Sunny\CodeBasics\Python\softwares\poppler-24.02.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract(file_path, file_format):
    # extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    if len(pages) > 0:
        page = pages[0]
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
        pass # extract data from prescription
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
        pass # extract data from patient details
    else:
        raise Exception(f"Invalid File Format: {file_format}")

    return extracted_data

if __name__ == '__main__':
    data = extract('../resources/patient_details/pd_2.pdf', 'patient_details')
    print(data)
