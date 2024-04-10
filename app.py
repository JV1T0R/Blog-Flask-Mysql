from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2803',
    database='flask_blog',
)

cursor = db_connection.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    campo_vazio = None

    if request.method == 'POST':
        titulo = request.form.get('Título')
        conteudo = request.form.get('Conteúdo')
        if titulo and conteudo:
            cursor.execute("INSERT INTO postagens (titulo, conteudo) VALUES (%s, %s)", (titulo, conteudo))
            db_connection.commit()
        else:
            campo_vazio = "Por favor, preencha todos os campos do formulário."

    cursor.execute("SELECT * FROM postagens")
    postagens = cursor.fetchall()

    if postagens:
        return render_template('index.html', postagens=postagens, campo_vazio=campo_vazio)
    else:
        sem_postagens = "Nenhuma Postagem Encontrada."
        return render_template('index.html', sem_postagens=sem_postagens, campo_vazio=campo_vazio)


if __name__ == '__main__':
    app.run(debug=True)

