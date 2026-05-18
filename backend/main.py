from flask import Flask
from config.init_db import init_db

app = Flask(__name__)
port = 5000



if __name__ == "__main__":
    print(f"\n> Servidor rodando na porta {port}")
    init_db() #Apenas cria o banco e as tabelas.

    app.run(port=port)
    