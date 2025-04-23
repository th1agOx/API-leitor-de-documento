import fitz
from extract_data import extract_block_data

def read_pdf_text(path):
    doc = fitz.open(path)
    full_text = ''
    for page in doc:
        full_text += page.get_text()
    return full_text

if __name__ == "__main__" :
    pdf_path = r"C:\Documentos\test2.pdf"
    extracted_data = read_pdf_text(pdf_path)

    invoice_id, document_id, datas, values = extract_block_data(extracted_data)

    print(f'\n NUMERO DE DOCUMENTO : { invoice_id + document_id}')
    print(f'\n DATA : {datas}') 
    print(f'\n VALOR : {values}')