from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cursos = []

@app.route('/')
def index():
    return render_template('index.html', cursos=cursos)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    descricao = request.form['descricao']
    avaliacao = request.form['avaliacao']
    url = request.form['url']
    nivel = request.form['nivel']
    categoria = request.form['categoria']
    
    curso = {
        'nome': nome,
        'plataforma': plataforma,
        'descricao': descricao,
        'avaliacao': avaliacao,
        'url': url,
        'nivel': nivel,
        'categoria': categoria
    }
    
    cursos.append(curso)
    
    return redirect(url_for('index'))

@app.route('/excluir/<int:index>', methods=['POST'])
def excluir(index):
    if 0 <= index < len(cursos):
        del cursos[index] 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
