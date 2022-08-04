from modules.crude import ConnectDb
from modules.sql import Sql
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', msg = 'OK')

@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        conn = ConnectDb()
        conn.dbconnect()
        if not conn.conn:
            return render_template('index.html', msg = 'ERRO')
        sql = Sql()
        sql.createsql('read', 'usercpf', cpf, 0, 0)
        users = conn.read(sql.sql)
        if cpf in [i[0] for i in users]:
            return render_template('index.html', msg = 'CPF já cadastrado')
        sql.createsql('insert', 'user', cpf, nome, sobrenome)
        conn.create(sql.sql)
        sql.createsql('read', 'user', 0, 0, 0)
        users = conn.read(sql.sql)
        conn.conn.close()
        return render_template('inserir.html', users = users)

if __name__ == '__main__':
    app.run()
