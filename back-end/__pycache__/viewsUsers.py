from flask import render_template, request, redirect, session, flash,url_for
from CV42 import app, db
from controlers import LoginUsuario, CadastroUsuario,GeekForm
from models import  Usuarios, PerfilUsuario
from flask_bcrypt import check_password_hash,generate_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = LoginUsuario()
    return render_template('login.html', proxima=proxima , form=form)
@app.route('/cadastro', methods= ['GET', 'POST'])
def cadastro():
    form = CadastroUsuario(request.form)
    
    if request.method == 'POST' and form.validate():
        nome = form.nome.data
        nickname = form.nickname.data
        email = form.email.data
        senha = form.senha.data
        confirm_senha = form.confirmacao.data
        if senha != confirm_senha:
            flash('As senhas deve ser compativeis')
            return redirect(url_for('cadastro'))
        senha = generate_password_hash(senha)
        novo_usuario = Usuarios(nome = nome, nickname = nickname, email = email, senha = senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('login'))
    # Verifique se a indentação está correta aqui
    return render_template('cadastro.html', form=form)


@app.route('/logaut')
def logaut():
    session['usuario_logado'] = None
    return redirect(url_for('login'))

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = LoginUsuario()
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()

    if usuario and check_password_hash(usuario.senha, form.senha.data):
        session['usuario_logado'] = usuario.nickname
        session['usuario_id'] = usuario.id 
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Nickname ou senha incorretos')
        return redirect(url_for('login'))

@app.route('/form', methods= ['GET', 'POST'])
def formulario():
    form = GeekForm()

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('formulario')))
    
    usuario_id = session.get('usuario_id')

    if request.method == 'POST' and form.validate_on_submit():
        idade = form.idade.data
        genero =  form.genero.data
        localizacao =  form. localizacao.data
        interesse = ', '.join(form.interesses.data) 
        dispositivos =  form.dispositivos.data
        evento_geek =  form.eventos_geek.data
        sistema_operacional = form.sistema_operacional.data
        item_colecionavel = form.itens_colecionaveis.data

        new_formulario =PerfilUsuario(
            idade=idade,
            genero=genero,
            localizacao=localizacao, 
            interesse=interesse,
            dispositivos=dispositivos,
            evento_geek=evento_geek, 
            sistema_operacional=sistema_operacional,
            item_colecionavel=item_colecionavel,
            usuario_id=usuario_id)

        db.session.add(new_formulario)
        db.session.commit()
        flash('Seu perfil foi salvo com sucesso')
    return render_template('formulario.html', form=form) 