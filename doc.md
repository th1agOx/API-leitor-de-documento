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