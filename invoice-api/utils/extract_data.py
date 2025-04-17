import re
from datetime import datetime

def extract_block_data(text):
    datas = re.findall(
        r'(\d{2}[\/\.,]\d{2}[\/\.,]\d{4})'
        r'(?:\d{2}[ ,.\-]*)?(?:January|February|MarchApril|May|June|'
        r'July|August|September|October|November|December)[ ,.\-]*\d{2}[ ,.\-]*\d{4}|'
        ,
        text,
        re.IGNORECASE
    )   

    values = re.findall(
        r'(?:$|R\$|BRL|USD)?\s?\d{1,5}(?:\.\d{3})*(?:,\d{2}|\.\d{2})', 
        text,
        re.IGNORECASE
    )

    invoice_id = re.findall(
        r'Invoice Number[:\s\-]*([A-Z]{0,3}[\d]{4,15})', 
        text,
        re.IGNORECASE
    )

    document_id = re.findall(
        r'(?:Numero Da Nota[:\s]*|)(?:\b(?:NF|RPA|NFS)[\s\-.]*)?(\d{4,10})',
        text,
        re.IGNORECASE
    )

    return invoice_id, document_id, datas, values

#FILTRO
##PARA DATAS USAR DATEUTIL.PARSER