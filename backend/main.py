from flask import Flask
from config.init_db import init_db
from models.user_model import update_username
from models.user_model import create_new_user
from models.user_model import delete_user


app = Flask(__name__)
port = 5000



if __name__ == "__main__":
    print(f"\n> Servidor rodando na porta {port}")
    init_db()

  
    app.run(port=port)
    