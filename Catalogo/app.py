from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

produtos = []

@app.route('/')
def catalogo():
    return render_template('catalog.html', produtos=produtos)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        descricao = request.form.get('descricao')
        if nome and preco and descricao: 
            produtos.append({'nome': nome, 'preco': preco, 'descricao': descricao})
        return redirect(url_for('catalogo'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)