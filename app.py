from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola_db'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        cidade = request.form['cidade']
        estado = request.form['estado']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO alunos (nome, idade, cidade, estado) VALUES (%s, %s, %s, %s)', (nome, idade, cidade, estado))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect('/cadastrar_aluno')
    
    return render_template('cadastrar_aluno.html')

@app.route('/cadastrar_curso', methods=['GET', 'POST'])
def cadastrar_curso():
    if request.method == 'POST':
        curso = request.form['curso']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cursos (curso) VALUES (%s)', (curso,))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect('/cadastrar_curso')
    
    return render_template('cadastrar_curso.html')

@app.route('/cadastrar_professores', methods=['GET', 'POST'])
def cadastrar_professores():
    if request.method == 'POST':
        nome = request.form['nome']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO professores (nome) VALUES (%s)', (nome,))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect('/cadastrar_professores')
    
    return render_template('cadastrar_professores.html')

@app.route('/cadastrar_unidades', methods=['GET', 'POST'])
def cadastrar_unidades():
    if request.method == 'POST':
        unidade = request.form['unidade']
        cidade = request.form['cidade']
        estado = request.form['estado']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO unidades (unidade, cidade, estado) VALUES (%s, %s, %s, %s)', (nome, cidade, estado))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect('/cadastrar_unidades')
    
    return render_template('cadastrar_unidades.html')

if __name__ == '__main__':
    app.run(debug=True)