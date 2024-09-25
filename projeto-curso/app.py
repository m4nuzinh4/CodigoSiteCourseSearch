from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os cursos cadastrados
cursos = []

@app.route('/')
def index():
    return render_template('index.html', cursos=cursos)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    # Captura os dados do formulário
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    descricao = request.form['descricao']
    avaliacao = request.form['avaliacao']
    url = request.form['url']
    nivel = request.form['nivel']
    categoria = request.form['categoria']
    
    # Cria um dicionário para o curso
    curso = {
        'nome': nome,
        'plataforma': plataforma,
        'descricao': descricao,
        'avaliacao': avaliacao,
        'url': url,
        'nivel': nivel,
        'categoria': categoria
    }
    
    # Adiciona o curso à lista
    cursos.append(curso)
    
    # Redireciona para a página inicial
    return redirect(url_for('index'))

@app.route('/excluir/<int:index>', methods=['POST'])
def excluir(index):
    if 0 <= index < len(cursos):
        del cursos[index]  # Remove o curso da lista
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
