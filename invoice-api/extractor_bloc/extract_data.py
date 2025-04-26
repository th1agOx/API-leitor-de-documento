import re
from datetime import datetime

def extract_block_data(data):
    day = r'\d{1,2}'
    year = r'\d{2,4}'
    separator = r'[\/\.,\-\s]*'

    month_names =  r'(?:January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|' \
                   r'July|Jul|August|Aug|September|Sept?|Sep|October|Oct|' \
                   r'November|Nov|December|Dec)'
    
    date_pattern = rf''' 
        (?:  
            {day}{separator}{day}{separator}{year}       
        )
        |
        (?:
            {day}{separator}{month_names}{separator}{year}
        )
        |
        (?:
            {month_names}{separator}{day}{separator}{year}
        )
    '''

    datas = re.findall(   ##   pre-loading phase of regex regular expressions 
        date_pattern,
        data,
        re.IGNORECASE | re.VERBOSE
    )

    currency = r'(?:R\$|$|BRL|USD)'
    value_before_comma = r'\d{1,6}'
    value_after_comma = r'\d{1,2}'

# O REGEX precisa reconhecer o currency de valores antes e depois da virgula
    values_pattern = rf'''
        (?:
            {currency}?\s*{value_before_comma}{separator}{value_after_comma}
        )
        |
        (?:
            {value_before_comma}{separator}{value_after_comma}
        )
    '''

    values = re.findall(
        values_pattern,
        data,
        re.IGNORECASE | re.VERBOSE
    )

# FINALIZAR 
    def extract_documents_ids(data):
        separator_invoice_id = r'[\-\.\#\:]'
        invoice_number= rf'[A-Z0-9]+(?:{separator_invoice_id}[A-Z0-9]+)*'

        invoice_pattern = rf'''    
            (:? 
                {invoice_number} 
            )
        '''

        invoice_id = re.findall(
            invoice_pattern, 
            data,
            re.IGNORECASE | re.VERBOSE
        )
# COMPLETAR IF
        if invoice_id:
            invoice_id = invoice

        document_id = re.findall(
        
            data,
            re.IGNORECASE | re.VERBOSE
        )

        return invoice_id, datas, values