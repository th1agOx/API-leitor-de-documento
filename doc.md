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
datas = re.findall(r'\d{2}/\d{2}/\d{4}/', text)
\d{2} + / = dois digitos de data separando por /
\d{4} = Quatro digitos de data  

- VALORES MONETÁRIOS
values = re.findall(r'\d(R?$?\:USD?usd?\$?\:BRL?)\s?\d{1,5}(?:\.\d{2})*,?\d{2}', text)
R?\$?: pode começar com "R" e/ou "$" — ou seja, "R$", "R", "$" ou nada
\s?: espaço opcional
\d{1,3}: de 1 a 3 dígitos no começo (ex: "1", "99", "999")
(?:\.\d{3})*: grupos opcionais de ponto + 3 dígitos (ex: ".000", ".100")
(?:...) é um grupo de não captura (não salva esse trecho separadamente)
,?\d{2}: vírgula opcional + dois dígitos (ex: ",00")

values = re.findall(r'\R{4}/\d{4})