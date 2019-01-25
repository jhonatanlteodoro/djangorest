# Djangorest
um pequeno exemplo de uma api com django rest



### Como rodar este projeto?.

* Clone o repositório.
* Crie um novo ambiente virtual com python3.
* Ative a o ambiente.
* Instale as dependências.
* Rode as migrações do banco.
* Execute os teste para verificar se tudo está funcionando **Os testes aqui não dão 100% de cobertura no código.
* Rode o servidor

```
git clone https://github.com/jhonatanlteodoro/djangorest.git
cd djangorest
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```

 ### Usando a api:

 Temos alguns endpoints nesta api que são
  * GET - /api/v1/product
  * GET - /api/v1/product/id-obj
  * POST - /api/v1/product
  * PATCH - /api/v1/product/id-obj
  * DELETE - /api/v1/product/id-obj
  * PUT - /api/v1/product/id-obj
