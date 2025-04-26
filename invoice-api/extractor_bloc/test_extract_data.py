import fitz
from extract_data import extract_block_data

def read_pdf_text(path):
    doc = fitz.open(path)
    full_text = ''
    for page in doc:
        full_text += page.get_text()
    return full_text

if __name__ == "__main__" :
    pdf_path = r"C:\Documentos\test.pdf"
    extracted_data = read_pdf_text(pdf_path)   ## within this phase the .pdf is extracted

    invoice_id, datas, values = extract_block_data(extracted_data)

    print(f'\n NUMERO DE DOCUMENTO : { invoice_id }')
    print(f'\n DATA : {datas}')
    print(f'\n VALOR : {values}')