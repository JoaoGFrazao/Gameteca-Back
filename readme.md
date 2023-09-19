### API de Boardgames

Esta é uma API simples para cadastrar board games (jogos de tabuleiro) criada usando Flask e SQLAlchemy. A API permite adicionar, listar e excluir board games em um banco de dados SQLite.

#### Configuração do Ambiente Virtual

Para executar este projeto, é recomendável criar um ambiente virtual Python. Siga as etapas abaixo:

1. Abra um terminal na raiz do projeto
2. Executo o seguinte comando para criar um ambiente virtual:

​	```python -m venv venv```

3. Ative o ambiente virtual:

- No Windows:

​	```venv\Scripts\activate```

- No macOS e Linux:

​	```	source venv/bin/activate```

#### Instalação de Dependências

Após criar e ativar o ambiente virtual, você precisa instalar as bibliotecas necessárias. O projeto fornece um arquivo `requirements.txt`. Para instalar as dependências, execute o seguinte comando:

```pip install -r requirements.txt```

#### Executando a API

Para iniciar o servidor da API, execute o seguinte comando na raiz do projeto:

```python app.py```

Agora, a API estará acessível em `http://localhost:5000`.

### Endpoints da API

A API possui os seguintes endpoints:

- `GET /list_all`: Lista todos os boardgames no banco de dados.
- `POST /add_game`: Adiciona um novo boardgame.
- `DELETE /boardgames/<int:id>`: Exclui um boardgame pelo seu ID.

A API também possui uma rota principal (`/`) que exibe uma página HTML simples.

<h3>Documentação em Swagger</h3>

A documentação em Swagger estará acessível em `http://localhost:5000/apidocs`



