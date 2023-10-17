Consulta CEP

Este é um simples aplicativo web em Python que usa o framework Flask para fornecer um serviço de busca de CEP (Código de Endereçamento Postal) e uma página da web para o usuário interagir com o serviço. Ele usa a API BrasilAPI para buscar informações de CEP a partir de um CEP fornecido.

Pré-requisitos
Certifique-se de ter as seguintes bibliotecas instaladas antes de executar este aplicativo:

Flask: Um framework web leve para Python. Você pode instalá-lo com o comando pip install Flask.
Como usar
Clone este repositório ou faça o download do código fonte para o seu sistema.

Navegue até o diretório onde você salvou o código.

bash
Copy code
cd path/to/cep-consulta.app
Execute o aplicativo com o seguinte comando:

bash
Copy code
python app.py
Isso iniciará o servidor web local Flask.

Abra o navegador e acesse http://127.0.0.1:5000/. Você verá uma página da web simples com um campo de pesquisa de CEP.

Digite um CEP válido no campo de pesquisa e clique no botão "Pesquisar". O aplicativo fará uma solicitação à API BrasilAPI e retornará as informações do CEP.

