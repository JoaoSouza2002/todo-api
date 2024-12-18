# To-Do API

Este é um projeto simples de uma API RESTful para gerenciar tarefas (To-Do List) construída com Python e FastAPI. A API permite a criação, leitura, atualização e exclusão de tarefas, utilizando um banco de dados SQLite para armazenar os dados.

## Funcionalidades

- **Criar tarefa**: Adicionar uma nova tarefa à lista.
- **Listar tarefas**: Obter todas as tarefas cadastradas.
- **Obter tarefa específica**: Consultar uma tarefa pelo seu ID.
- **Atualizar tarefa**: Alterar os dados de uma tarefa existente.
- **Excluir tarefa**: Remover uma tarefa da lista.

## Tecnologias Utilizadas

- **FastAPI**: Framework web para construir APIs com Python.
- **SQLite**: Banco de dados relacional utilizado para persistência dos dados.
- **Pydantic**: Biblioteca para validação de dados.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.

## Pré-requisitos

Antes de começar, você precisará ter o Python instalado em sua máquina. Recomenda-se também criar um ambiente virtual para isolar as dependências do projeto.

### Passos para rodar o projeto

1. **Clonar o repositório**:

   ```bash
   git clone https://github.com/JoaoSouza2002/todo-api.git
   cd todo-api
Criar e ativar um ambiente virtual:

Windows:

bash
Copiar código
python -m venv venv
.\venv\Scripts\activate
Linux/Mac:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instalar as dependências:

bash
Copiar código
pip install -r requirements.txt
Rodar a API:

bash
Copiar código
uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.

Endpoints
GET /todos: Retorna todas as tarefas.
GET /todos/{id}: Retorna uma tarefa específica pelo ID.
POST /todos: Cria uma nova tarefa.
PUT /todos/{id}: Atualiza uma tarefa existente.
DELETE /todos/{id}: Exclui uma tarefa.
Exemplo de uso
Criar uma nova tarefa (POST)
bash
Copiar código
curl -X 'POST' \
  'http://127.0.0.1:8000/todos' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Estudar Python",
  "description": "Revisar conceitos de FastAPI"
}'
Obter todas as tarefas (GET)
bash
Copiar código
curl -X 'GET' 'http://127.0.0.1:8000/todos'
Excluir uma tarefa (DELETE)
bash
Copiar código
curl -X 'DELETE' 'http://127.0.0.1:8000/todos/1'
Contribuindo
Se você deseja contribuir para este projeto, fique à vontade para enviar pull requests! Certifique-se de descrever as alterações feitas de forma clara.

Licença
Este projeto está sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.