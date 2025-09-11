## Workshop Back-End (Turma 2, 2025.2)

### CRUD de CEP
- **Configuração**<br><br>
**1)** `python -m venv venv`<br>
**2)** `.\venv\Scripts\activate` ou `source venv/Scripts/activate`<br>
**3)** `pip install -r requirements.txt`<br>
**4)** `python manage.py makemigrations`<br>
**5)** `python manage.py migrate`<br>
**6)** `python manage.py runserver`

- **Endpoints**<br><br>
**Listar)** `http://127.0.0.1:8000/enderecos/`<br>
**Cadastrar)** `http://127.0.0.1:8000/enderecos/novo/`<br>
**Detalhar)** `http://127.0.0.1:8000/enderecos/id/`<br>
**Editar)** `http://127.0.0.1:8000/enderecos/id/editar/`<br>
**Deletar)** `http://127.0.0.1:8000/enderecos/id/deletar/`<br>
