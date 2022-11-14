
# <a href="app_empresa/templates/cadastro.html">empresa_desafio</a>
# 1- Clonar o repositório na maquina
git clone https://github.com/Sleomorais/empresa_desafio

# 2- Abrir a pasta com codigo do VSCode e criar a venv pelo terminal

-Precisa ter o python instalado na máquina
python -m venv ./venv

# 3- Ativar a venv e baixar o requirements.txt

-Dar permisão de iniciar a venv
No powershell admin digitar
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    e digitar A para aceitar todos
-Ativar a venv
.\venv\Scripts\activate

-Com a venv ativada
pip install -r requirements.txt

# 4- Usando o django

-Iniciar o projeto
python manage.py runserver
