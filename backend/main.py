from flask import Flask
from config.init_db import init_db
import json
from models.senhas_model import create_password
from models.senhas_model import search_password_in_cofre
from models.senhas_model import delete_password

from models.cofres_permissoes_model import search_cofres_with_permission

app = Flask(__name__)
port = 5000



if __name__ == "__main__":
    print(f"\n> Servidor rodando na porta {port}")
    init_db()

    app.run(port=port)
    