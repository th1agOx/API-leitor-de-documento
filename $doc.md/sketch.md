Refletir como vai inserir esses três pontos ( Objetivo	Estilo	Entrega ) para essa estrutura de arquivos :
C:\Controles\LeituraPdf\invoice-api\__pycache__

C:\Controles\LeituraPdf\invoice-api\output\documentacao_AP.xlsx

C:\Controles\LeituraPdf\invoice-api\app.py ...\extract_data.py ...\test_extract_data.py

C:\Controles\LeituraPdf\venv\include .\lib .\Scripts \gitignore \pyvenv.cfg

C:\Controles\LeituraPdf\doc md e requirements.txt

Para toda estrutura de arquivo * estou exportando como API para ser usada de ponto de pedido de envio de extração para saida com dados perfeitamente extraidos e estruturação no caminho \output onde está um arquivo de AP estruturado pronto para entrada de dados extraido do regex e o ambiente de teste criado no mesmo caminho da extração do blocos em regex


encaixar informação no mensionando que isso é uma API, por que as vezes não parece logico para outros usuarios e etc, essa api esperará ser agtivada por um fluxo no power automate que reconhece a necessidade de precisar solicar um arquivo AP , documentando os principais pontos de uma invoice / doumento fiscal nacional ( Brasil ) , com isso a API aciona o extract_data, que extrai os dados e envia eles por conta de interpretadores de texto ( Regex ) + funções que vai refinar e resumir os dados retornado e enviar para o AP_structuring.py que será responsaveis por usar essas variasves onde estaram os dados armazenados e trazidos do arquivo de estração de bloco que assim estruturado, sera enviado para o arquivo.xlsx ( AP fiscal estruturada e enviada como output ( retorno ) da api devolvendo isso no fluxo ( "encaixado" ) na API

git add README.md	Diz ao Git que você quer adicionar o README no próximo commit
git commit -m "Mensagem do commit"	Faz o commit com a mensagem explicando o que você fez
git push origin main	Envia as alterações para o GitHub na branch main