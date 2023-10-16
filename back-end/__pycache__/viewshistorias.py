from flask import render_template, request, redirect, session, flash,url_for
from CV42 import app, db
from models import Historias
from controlers import NovaHistoriaForm



@app.route('/rpg')
def rpg():
    # Obtenha o nome da imagem da consulta de URL
    image_name = request.args.get('image_name')
    return render_template('rpg.html', image_name=image_name)

@app.route('/lista_historia')
def lista_historia():
   return render_template('lista.html')

@app.route('/nova-historia', methods=['POST', 'GET'])
def nova_historia():
    form = NovaHistoriaForm()  # Instancie o objeto do formulário

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('nova_historia')))
    

    usuario_id = session.get('usuario_id')
    
    if request.method == 'POST' and form.validate_on_submit():
        titulo = form.titulo.data
        genero = form.genero.data
        conteudo = form.conteudo.data

        new_historia = Historias(titulo=titulo, genero=genero, conteudo=conteudo,usuario_id=usuario_id)

        db.session.add(new_historia)
        db.session.commit()
        flash('Historia cadastrada com sucesso')
    return render_template('historias.html', form=form) 


# Rota para editar uma história
@app.route('/editar-historia/<int:id>', methods=['GET', 'POST'])
def editar_historia(id):
    # Implemente a lógica de edição de história aqui
    pass


@app.route('/tornar_publico_historia/<int:historia_id>')
def tornar_publico_historia(historia_id):
    historia = Historias.query.get_or_404(historia_id)
    historia.publico = True
    db.session.commit()
    flash('História tornada pública com sucesso!', 'success')
    return redirect(url_for('lista'))

@app.route('/tornar_privado_historia/<int:historia_id>')
def tornar_privado_historia(historia_id):
    historia = Historias.query.get_or_404(historia_id)
    historia.publico = False
    db.session.commit()
    flash('História privada com sucessso', 'success')
    return redirect(url_for('lista'))


