from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('processos.db')

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, senha TEXT)''')
    conn.commit()
    conn.close()

init_db()  # Cria a tabela se ela não existir

@app.route('/listausuarios', methods=['GET'])
def index():
    if request.method == 'GET':
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        users = cursor.fetchall()
        conn.close()
        return render_template('listausuarios.html', users=users)
    
    nome = request.form['nome']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome))
    users = cursor.fetchall()
    conn.close()
    return render_template('listausuarios.html', users=users)

@app.route('/cadusuario', methods=['GET', 'POST'])
def cadusuario():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    return render_template('cadusuario.html')

if __name__ == '__main__':
    app.run(debug=True)
