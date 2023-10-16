from flask import render_template, request, redirect, session, flash,url_for,send_from_directory
from CV42 import app, db
from models import Jogos,Historias
from controlers import id_image, deleta_arquivo,FormularioJogo
import time

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')


@app.route('/new-game')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioJogo()
    return render_template('new.html', titulo = 'Cadastro de novos jogos', form=form)

@app.route('/criar', methods=['POST',])
def criar():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    
    #CRIAÇÃO DE NOVOS JOGOS
    form = FormularioJogo(request.form)
    
    if not form.validate_on_submit:
        return redirect(url_for('novo'))
    
    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
    usuario_id = session['usuario_id']
    jogo = Jogos.query.filter_by(nome = nome, usuario_id=usuario_id).first()
    
    if jogo:
        flash('Jogo existe na lista de jogos')
        return  redirect(url_for('novo'))
    novo_jogo = Jogos(nome = nome, categoria = categoria, console = console, usuario_id = usuario_id)
    db.session.add(novo_jogo)
    db.session.commit()
   
    
    #CAPA DO JOGO
    arquivo = request.files['arquivo']
    upload_path= app.config['UPLOAD_PATH']
    timestemp = time.time()
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}-{timestemp}.jpg')
    
    return redirect(url_for('lista'))




@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    
    jogo=Jogos.query.filter_by(id=id).first()
    
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    
    
    capa_jogo = id_image(id)
    return render_template('editar.html', titulo = 'Edição de Jogos', jogo=jogo, capa_jogo= capa_jogo, form=form, id=id)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    form = FormularioJogo(request.form)
    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()

        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

        db.session.add(jogo)
        db.session.commit()
        
        arquivo = request.files['arquivo']
        upload_path= app.config['UPLOAD_PATH']
        timestam = time.time()
        deleta_arquivo(jogo.id)
        arquivo.save(f'{upload_path}/capa{jogo.id}-{timestam}.jpg')

    return redirect(url_for("lista"))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login',))
     
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('lista'))

@app.route('/deletar-historia/<int:id>')
def deletar_historia(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login',))
     
    Historias.query.filter_by(id=id).delete()
    db.session.commit()
    
    return redirect(url_for('lista'))
    
    
@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads',nome_arquivo)

@app.route('/lista')
def lista():
    usuario_id = session.get('usuario_id')
    if usuario_id:
        lista = Jogos.query.filter_by(usuario_id=usuario_id).order_by(Jogos.id)
        lista_historias = Historias.query.filter_by(usuario_id=usuario_id).order_by(Historias.id)
        return render_template('lista.html', jogos=lista,historias=lista_historias)
    else:
        flash('Faça login para visualizar sua lista de jogos.')
        return redirect(url_for('login'))

@app.route('/tornar_publico/<int:jogo_id>')
def tornar_publico(jogo_id):
    jogo = Jogos.query.get_or_404(jogo_id)
    jogo.publico = True
    if jogo.publico:
        flash("Deu certo")
    db.session.commit()
    flash('História tornada pública com sucesso!', 'success')
    return redirect(url_for('lista'))

@app.route('/tornar_privado/<int:jogo_id>')
def tornar_privado(jogo_id):
    jogo = Jogos.query.get_or_404(jogo_id)
    jogo.publico = False
    if jogo.publico:
        flash("Deu errado")
    db.session.commit()
    flash('História privada com sucesso!', 'success')
    return redirect(url_for('lista'))

@app.route('/publicacoes')
def publicas():
    jogos_publicos = Jogos.query.filter_by(publico=True).all()
    historias_publicos = Historias.query.filter_by(publico=True).all()
    return render_template('publicos.html', historias=historias_publicos, jogos=jogos_publicos)