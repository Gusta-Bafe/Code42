from flask import render_template, request, redirect, session, flash,url_for,send_from_directory
from CV42 import app, db
from models import Personagens
from controlers import PersonagemForm

@app.route('/novo-personagem',methods=['GET', 'POST'])
def novo_personagem():
    form = PersonagemForm()

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo_personagem')))

    usuario_id = session.get('usuario_id')

    if request.method == 'POST' and form.validate_on_submit():
        nome = form.nome.data
        idade = form.idade.data
        classe =  form.classe.data
        raca =  form.raca.data
        personalidade =  form.personalidade.data
        backgraund = form.backgraund.data


        new_personagem = Personagens(nome = nome,idade = idade, classe=classe,raca=raca,personalidade = personalidade,backgraund= backgraund,usuario_id=usuario_id)

        db.session.add(new_personagem)
        db.session.commit()
        flash('Personagem criado com sucesso')

    return render_template('personagem.html', form=form) 
    
@app.route('/lista-personagens')
def lista_personagens():
    usuario_id = session.get('usuario_id')
    if usuario_id:
        personagens = Personagens.query.filter_by(usuario_id=usuario_id).order_by(Personagens.id)
        return render_template('lista.html', entidades=personagens, tipo_entidade='Personagens')
    else:
        flash('Faça login para visualizar sua lista de personagens.')
        return redirect(url_for('login'))