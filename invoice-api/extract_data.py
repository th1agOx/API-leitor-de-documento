import re
from datetime import datetime

def extract_block_data(data):
    #CRIAR VARIAÇÃO JAN, SEP ...
    datas = re.findall(
        r'''(
            \d{1,2}[\/\.,-]\d{1,2}[\/\.,-]´\d{2,4}                              ## bloco 1 DD/MM/AAAA ou D.M.AA 
            |               
            (?:\d{1,2}[\/\.,-]*)? # opcional
            (?:January|February|March|April|May|June|                          ## bloco 2 September 10, 2024 
            July|August|September|October|November|December )
            [ ,.\-]*\d{1,2}?[ ,.\-]* # não opcioanl
            \d{2,4} 
            |    
            \d{1,2}[ ,.\-]*                                                     ## bloco 3 10,September 2024 
            (?:January|February|March|April|May|June|
            July|August|September|October|November|December)
            [ ,.\-]*
            \d{2,4})''',
        data,
        re.IGNORECASE | re.VERBOSE
    )

    values = re.findall(
        r'''(?:R\$|$|BRL|USD)?
            \s*
            \d{1,6} 
            (?:[\.,]\d{1,2})*
            |
            (?:\d{1,6}[\.,]\d{1,2})
            (?:[\.,]\d{1,2}?)''', 
        data,
        re.IGNORECASE | re.VERBOSE
    )

    invoice_id = re.findall(
        r'Invoice Number[:\s\-]*([A-Z]{0,3}[\d]{4,15})', 
        data,
        re.IGNORECASE | re.VERBOSE
    )

    document_id = re.findall(
        r'(?:Numero Da Nota[:\s]*|)(?:\b(?:NF|RPA|NFS)[\s\-.]*)?(\d{4,10})',
        data,
        re.IGNORECASE | re.VERBOSE
    )

    return invoice_id, document_id, datas, values

#FILTRO
##PARA DATAS USAR DATEUTIL.PARSER