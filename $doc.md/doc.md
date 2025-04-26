Funcionalidade e caminhos

Power automate reconhece o recebimento do e-mail pelo outlook , o python é exportado no fluxo como API , reconhece o arquivo .pdf lê e extrai os três pontos de dados .
Com isso ocorre a saída desses dados para o documento csv e uma nova AP com esses dados atualizados é criado

A api vai servir para reconhecer o documento e vai acionar o extract, que vai ser responsável por identificar os dados que são preciso e extrair os 3 dados no formato JSON.


Fluxo Real 

Power Automate envia o PDF 

Flask API recebe 

Aciona o extract_data, que extrai os dados

API salva os dados no arquivo .csv ou .xlsx

API retorna uma resposta de status + os dados extraidos 

Power automate captura essa resposta


# REQUIREMENTS.TXT
- FUNCIONA COMO UM ALIASES PARA UNIVERSALISAR TODAS AS DEPÊNDENCIAS NECESSÁRIAS PARA O PROHJETO EM PYHTON

# REGEX

- DATAS

    EXEMPLOS DE COMPARAÇÃO DOS 3 BLOCOS : 

    DATA EXTRAÍDA	                EM QUAL BLOCO ELE INTERPRETA ?
                    
    10/09/2024	                    BLOCO 1

    September 10, 2024	            BLOCO 2

    10 September 2024	            BLOCO 3

    September 2024	                BLOCO 2️

    10, September, 2024	            BLOCO 3️

    March 2025	                    BLOCO 2️



# ------------------------------------------------------COMEÇAR DOCUMENTAÇÃO DE LEITOR DE DOCUMENTOS FISCAIS INTELIGENTE AQUI :

read_pdf_text(pdf_path) → Lê o texto completo do PDF. (Aqui ainda não faz Regex, só lê.)

extract_block_data(extracted_data) → Aqui sim que o Regex é aplicado no texto extraído.

No final, o invoice_id, datas e values vêm dos findall() que você criou nos padrões de Regex.

Então tecnicamente, o que "aciona o Regex" mesmo é quando você chama a função:

python
Copiar
Editar
invoice_id, datas, values = extract_block_data(extracted_data)
e não exatamente o read_pdf_text.
O read_pdf_text só prepara o texto.

Quer que eu também ajuste seu código corrigindo uns pequenos detalhes que achei? (tipo o invoice que tá errado e falta no document_id?) 🚀
Te mando já pronto se quiser!