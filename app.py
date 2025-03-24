from flask import Flask, request, jsonify
import sqlite3

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Livros (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                imagem_url TEXT NOT NULL
            )
        """)

init_db()

app = Flask(__name__)

@app.route('/doar', methods=['POST'])
def doar():
    dados = request.get_json()
    titulo = dados.get('titulo')
    autor = dados.get('autor')
    categoria = dados.get('categoria')
    imagem_url = dados.get('imagem_url')
    if not titulo or not autor or not categoria or not imagem_url:
        return jsonify({"mensagem": "Dados incompletos"}),400
    with sqlite3.connect('database.db') as conn:
        conn.execute("""
            INSERT INTO Livros (titulo, autor, categoria, imagem_url)
            VALUES ("{titulo}", "{autor}", "{categoria}", "{imagem_url}")
        """)
        conn.commit()
        return jsonify({"mensagem": "Livro doado com sucesso!"}),201

if __name__ == '__main__':
    app.run(debug=True)