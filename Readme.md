## Desafio B2w


##### Foi criado a api de acordo com os requisitos do desafio:

###### Requisitos:

###### - A API deve ser REST
###### - Para cada planeta, os seguintes dados devem ser obtidos do banco de dados da aplicação, sendo inserido manualmente:
###### Nome, Clima, Terreno
###### - Para cada planeta também devemos ter a quantidade de aparições em filmes, que podem ser obtidas pela API pública do Star Wars:  https://swapi.co/

###### Funcionalidades desejadas: 

###### - Adicionar um planeta (com nome, clima e terreno)
###### - Listar planetas
###### - Buscar por nome
###### - Buscar por ID
###### - Remover planeta

---
## Tutorial
#### Entre na pasta em que ficará o projeto: ```cd projeto```
#### Crie seu VirtualEnv   ``` python3 -m venv venv ```
#### Ative seu virtualenv  ``` source venv/bin/activate ```
#### Ative seu virtualenv  ``` source venv/bin/activate ```
#### Baixe o repositorio   ``` git clone https://github.com/diegoarioza/desafio_api_b2w.git ```
#### Entre na pasta do projeto ``` cd desafio_api_b2w/ ```
#### Instale os requerimentos ``` pip3 install -r requirements.txt  ```
#### Execute o runserver ``` python manage.py runserver ```

#### Get planetas: http://127.0.0.1:8000/starwars/
#### Get Planeta Individual: http://127.0.0.1:8000/starwars/9/
#### Busca por id: http://127.0.0.1:8000/starwars/?id=9
#### Busca por Nome: http://127.0.0.1:8000/starwars/?nome=Dagobah
#### Busca Genérica: http://127.0.0.1:8000/starwars/?search=Dagobah

#### OBS: Modo de execução somente para testes, em produção nutilize um webserver como apache ou nginx com wsgi (ex. gunicorn)
