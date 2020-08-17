# Navedex

## Iniciando o sistema

Para se iniciar o sistema, devem ser executados os seguintes comandos no diretório raiz da aplicação:

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Esses comandos irão instalar as bibliotecas, criar o banco de dados e executar a API que, por padrão será executada na seguinte URL:

```
http://127.0.0.1:8000/
```

OBS.: Iremos considerar essa URL padrão, mas, para alterá-la, pode-se definir outro IP, com o seguinte comando:

```
python manage.py runserver [IP]:[PORTA]
```

## Autenticação

### Cadastro de Usuário

Para se cadastrar um usuário, deve-se realizar uma requisição, com o método POST, na URL:

```
http://127.0.0.1:8000/auth/users/
```

Com o seguinte conteúdo como body:

```
{
	"email": "user@teste.com",
	"password": "password",
	"confirm_password": "password"
}
```

Sendo esperado obter, como resposta:

```
{
  "email": "user@teste.com"
}
```

### Login

Para se realizar o login de um usuário, deve-se realizar uma requisição, com o método POST, na URL:

```
http://127.0.0.1:8000/auth/login/
```

Com o seguinte conteúdo como body:

```
{
	"email": "user@teste.com",
	"password": "password"
}
```

Sendo esperado obter, como resposta:

```
{
  "refresh": "[TOKEN_REFRES]",
  "access": "[TOKEN_ACCESS]"
}
```

Para então se criar o seguinte header de autenticação do usuário:

```
{
    'Authorization': 'Bearer [TOKEN_ACCESS]'
}
```


## Navers

### Index

Para se listar todos os navers criados por um usuário, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/navers/
```

Pode-se realizar o filtro por nome, tempo de empresa e cargo. Um exemplo de filtro seria:

```
http://127.0.0.1:8000/api/navers/?job_role=Desenvolvedor
```

É esperado então obter, como resposta, a listagem de navers criados pelo usuário, por exemplo:

```
[
  {
    "id": 37,
    "name": "New Naver",
    "birthdate": "1999-05-15",
    "admission_date": "2020-06-12",
    "job_role": "Desenvolvedor"
  }
]
```

### Show

Para se exibir informações sobre um único naver criado por um usuário, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/navers/<id_naver>/
```

É esperado então obter, como resposta, todas as informações referentes ao naver, por exemplo:

```
{
  "id": 37,
  "name": "New Naver",
  "birthdate": "1999-05-15",
  "admission_date": "2020-06-12",
  "job_role": "Desenvolvedor",
  "projects": [
    {
      "id": 11,
      "name": "projeto legal"
    }
  ]
}
```

### Store

Para se criar um novo naver na base de dados, deve-se realizar uma requisição, com o método POST, na URL:

```
http://127.0.0.1:8000/api/navers/create/
```

Com o seguinte conteúdo como body:

```
{
    "name": "Fulano",
    "birthdate": "1999-05-15",
    "admission_date": "2020-06-12",
    "job_role": "Desenvolvedor",
	"projects": [14]
}
```

É esperado então que o naver seja criado na base de dados e associado ao usuário logado que o criou. Deve-se também receber como resposta o seguinte conteúdo:

```
{
  "name": "Fulano",
  "birthdate": "1999-05-15",
  "admission_date": "2020-06-12",
  "job_role": "Desenvolvedor",
  "projects": [
    14
  ]
}
```

### Update

Para se atualizar um naver existente na base de dados, deve-se realizar uma requisição, com o método PUT, na URL:

```
http://127.0.0.1:8000/api/navers/update/<id_naver>/
```

Com o seguinte conteúdo como body:

```
{
	"name": "Fulano",
    "birthdate": "1999-05-15",
    "admission_date": "2020-06-12",
    "job_role": "Desenvolvedor Sênior",
    "projects": [14]
}
```

É esperado então que o naver seja atualizado na base de dados e deve-se receber, como resposta, o seguinte conteúdo:

```
{
  "id": 38,
  "name": "Fulano",
  "birthdate": "1999-05-15",
  "admission_date": "2020-06-12",
  "job_role": "Desenvolvedor Sênior",
  "projects": [
    14
  ]
}
```

### Delete

Para se excluir um naver existente na base de dados, deve-se realizar uma requisição, com o método DELETE, na URL:

```
http://127.0.0.1:8000/api/navers/<id_naver>/
```

É esperado então que o naver seja excluído da base de dados e não é esperado nenhum conteúdo como resposta.

## Projetos

### Index

Para se listar todos os projetos criados por um usuário, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/projects/
```

Pode-se realizar o filtro por nome. Um exemplo de filtro seria:

```
http://127.0.0.1:8000/api/projects/?name=New Project
```

É esperado então obter, como resposta, a listagem de projetos criados pelo usuário, por exemplo:

```
[
  {
    "id": 13,
    "name": "New Project"
  }
]
```

### Show

Para se exibir informações sobre um único projeto criado por um usuário, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/projects/<id_project>/
```

É esperado então obter, como resposta, todas as informações referentes ao projeto, por exemplo:

```
{
  "id": 11,
  "name": "projeto ok",
  "navers": [
    {
      "id": 37,
      "name": "New Naver",
      "birthdate": "1999-05-15",
      "admission_date": "2020-06-12",
      "job_role": "Desenvolvedor"
    }
  ]
}
```

### Store

Para se criar um novo projeto na base de dados, deve-se realizar uma requisição, com o método POST, na URL:

```
http://127.0.0.1:8000/api/projects/create/
```

Com o seguinte conteúdo como body:

```
{
	"name": "Novo Projeto",
	"navers": [37]
}
```

É esperado então que o projeto seja criado na base de dados e associado ao usuário logado que o criou. Deve-se também receber como resposta o seguinte conteúdo:

```
{
  "name": "Novo Projeto",
  "navers": [
    37
  ]
}
```

### Update

Para se atualizar um projeto existente na base de dados, deve-se realizar uma requisição, com o método PUT, na URL:

```
http://127.0.0.1:8000/api/projects/update/<id_project>/
```

Com o seguinte conteúdo como body:

```
{
	"name": "Novo Projeto Update",
	"navers": [37]
}
```

É esperado então que o projeto seja atualizado na base de dados e deve-se receber, como resposta, o seguinte conteúdo:

```
{
  "id": 15,
  "name": "Novo Projeto Update",
  "navers": [
    37
  ]
}
```

### Delete

Para se excluir um projeto existente na base de dados, deve-se realizar uma requisição, com o método DELETE, na URL:

```
http://127.0.0.1:8000/api/projects/<id_project>/
```

É esperado então que o projeto seja excluído da base de dados e não é esperado nenhum conteúdo como resposta.