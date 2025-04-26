# Invoice Extraction API 📄🚀

**Descrição:**  
API desenvolvida para realizar extração automatizada de informações de documentos em PDF, como número de nota fiscal, datas e valores.  
A extração é feita por meio de expressões regulares (Regex) e processamento adicional, com a saída estruturada em formato .xlsx, pronta para integração com fluxos automatizados.

Essa API foi pensada para ser acionada automaticamente via **Power Automate**, a partir de eventos que detectam a necessidade de registrar documentos fiscais (AP - Accounts Payable).  
Ela documenta os principais pontos de uma invoice/documento fiscal nacional (Brasil), extraindo informações relevantes e entregando-as de forma organizada.

---

## ✨ Objetivos
- Automatizar a extração de dados críticos de documentos financeiros.
- Facilitar a integração com sistemas de RPA (ex: UiPath, Power Automate).
- Reduzir tempo manual de análise de documentos.
- Disponibilizar os dados extraídos em formato estruturado (.xlsx).
- Tornar o processo totalmente adaptável a fluxos automatizados de negócios.

---

## ⚙️ Tecnologias Utilizadas
- Python 3.11
- Flask (para futura transformação em API web, se necessário)
- PyMuPDF (`fitz`) para leitura de PDFs
- Expressões Regulares (Regex) para interpretação textual
- Virtualenv para gerenciamento de ambiente
- Power Automate para automação do fluxo de entrada
- JIRA para acompanhamento de backlog (equipe de RPA)

---

## 🛠️ Como Funciona a API (Visão Geral)

1. **Power Automate** detecta necessidade de processar um arquivo de Accounts Payable (AP).
2. **Chamada para a API** (acionamento do `app.py`).
3. O `app.py` orquestra a extração chamando o módulo `extract_data.py`.
4. O `extract_data.py` utiliza expressões regulares para capturar:
   - Número do Documento (Invoice ID)
   - Datas de emissão
   - Valores monetários
5. Esses dados são refinados e armazenados em variáveis controladas.
6. O módulo `AP_structuring.py` (em fase de integração) será responsável por receber essas variáveis e montar a estrutura final.
7. A estrutura é gravada no arquivo `.xlsx` dentro da pasta `/output`.
8. O resultado final é retornado no fluxo original, dentro do Power Automate.

---

## 🗂 Estrutura do Projeto

invoice-api/ ├── app.py # Script principal (orquestrador da API) ├── extract_data.py # Funções de extração de dados por Regex ├── AP_structuring.py # (Em desenvolvimento) Organização dos dados extraídos ├── test_extract_data.py # Scripts de teste da extração ├── output/ │ └── documentacao_AP.xlsx # Planilha de saída para controle de contas ├── doc/ │ └── README.md │ └── requisitos.txt ├── venv/ # Ambiente virtual Python └── pycache/ # Cache interno do Python

---
## 🚀 Como Rodar o Projeto

1. Clone o Repositório:
   ```bash
   git clone https://github.com/seu-usuario/invoice-api.git
   cd invoice-api

2. Ative o Ambiente Virtual:

# Windows
.\venv\Scripts\activate

3. Instale as Depêndencias:

pip install -r doc/requisitos.txt

4. Execute a API

python app.py

## 📥 Exemplo de Entrada (PDF)
Arquivo PDF contendo informações como:

Nota Fiscal: AB-12345
Data de Emissão: 25/04/2025
Valor: R$ 1.250,00

## 📤 Exemplo de Saída
Arquivo documentacao_AP.xlsx preenchido automaticamente com:

Número do Documento	Data de Emissão	Valor
AB-12345	25/04/2025	1250,00

## 🔎 Sobre a Documentação
Cada função e módulo contém:

Docstring explicativa

Tipagem explícita dos parâmetros e retornos

Comentários técnicos para pontos-chave do processo

Exemplos práticos em test_extract_data.py

## 📋 BackLog
As tarefas estão divididas de acordo com o módulo responsável (API principal, extração, estruturação).

Cada feature é documentada no backlog para rastreamento de progresso (parte de RPA).

A integração visa suportar automações robustas e confiáveis.

## 📣 Observação Final
Este projeto é parte de uma iniciativa para otimizar fluxos documentais e consolidar boas práticas de extração de dados via pipelines automatizados, sendo uma base sólida para integrações futuras com APIs REST ou bots de automação.