import os
from CV42 import app
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, validators, BooleanField,SelectField,TextAreaField,IntegerField, widgets,SelectMultipleField
from wtforms.validators import DataRequired


class GeekForm(FlaskForm):
    # Dados Demográficos
    idade = IntegerField('Idade', validators=[DataRequired()])
    genero = SelectField('Gênero', choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], validators=[DataRequired()])
    localizacao = SelectField('Estado', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
                                                 ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
                                                 ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
                                                 ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
                                                 ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
                                                 ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
                                                 ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], validators=[DataRequired()])

    # Hobbies e Interesses
    interesses = SelectMultipleField('Hobbies e Interesses',
                                            choices=[('rpg', 'Jogos de RPG'), ('anime', 'Anime e Mangá'),
                                                     ('boardgames', 'Boardgames'), ('esportes', 'Esportes'),
                                                     ('tecnologia', 'Tecnologia'), ('cinema', 'Cinema'),
                                                     ('livros', 'Livros'), ('musica', 'Música')],
                                            option_widget=widgets.CheckboxInput(),
                                            coerce=str)
    

    # Tecnologia e Gadgets
    dispositivos = SelectField('Dispositivos eletrônicos mais utilizados', choices=[('Mobile','Mobile'), ('PC','PC'), ('console','Console')], validators=[DataRequired()])
    sistema_operacional = SelectField('Sistema operacional preferido',
                                      choices=[('iOS', 'iOS'), ('Android', 'Android'), ('Windows', 'Windows'),
                                               ('macOS', 'macOS'), ('Linux', 'Linux')],
                                      validators=[DataRequired()])
    # Eventos e Convenções Geek
    eventos_geek = SelectField('Voçê tem costume de pariticipar em eventos de cultura pop na sua cidade?',
                                              choices=[('sim', 'Sim'), ('nao', 'Não'), ('interesse', 'Não tenho interesse'),('interresse2','Não, mas tenho interresse'), ('eventos', 'Não cosutma ter eventos na minha cidade')],
                                              option_widget=widgets.CheckboxInput(),
                                              validators=[DataRequired()])
   

   

    # Compras e Produtos Geek
    itens_colecionaveis = SelectField('Voçê tem costume de colecionar itens como card games e Action figures?',
                                              choices=[('sim', 'Sim'), ('nao', 'Não'), ('interesse', 'Não tenho interesse'),('interresse2','Não, mas tenho interresse')],
                                              option_widget=widgets.CheckboxInput(),
                                              validators=[DataRequired()])
    


    submit = SubmitField('Enviar')

class ComidasForm(FlaskForm):
    qtd_pessoas = IntegerField('Quantidade de pessoas', validators=[DataRequired()])
    duracao = IntegerField('Duração da Sessão', validators=[DataRequired()])


class PersonagemForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired()])
    classe = SelectField('Classe', choices=[
    ('guerreiro', 'Guerreiro'),
    ('mago', 'Mago'),
    ('ladino', 'Ladino'),
    ('clérigo', 'Clérigo'),
    ('ranger', 'Ranger'),
    ('feiticeiro', 'Feiticeiro'),
    ('bárbaro', 'Bárbaro'),
    ('druida', 'Druida'),
    ('paladino', 'Paladino'),
    ('monge', 'Monge')
], validators=[DataRequired()])
    raca = SelectField('Raça', choices=[
    ('humano', 'Humano'),
    ('elfo', 'Elfo'),
    ('anão', 'Anão'),
    ('orc', 'Orc'),
    ('halfling', 'Halfling'),
    ('gnomo', 'Gnomo'),
    ('meio-elfo', 'Meio-Elfo'),
    ('meio-orc', 'Meio-Orc'),
    ('tiefling', 'Tiefling'),
    ('aarakocra', 'Aarakocra')
], validators=[DataRequired()])
    personalidade = TextAreaField('Personalidade', validators=[DataRequired()])
    backgraund = TextAreaField('Background', validators=[DataRequired()])



class NovaHistoriaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    genero = SelectField('Gênero', choices=[
        ('Ação', 'Ação'),
        ('Aventura', 'Aventura'),
        ('Comédia', 'Comédia'),
        ('Faroeste', 'Faroeste'),
        ('Ficção C', 'Ficção C'),
        ('Fantasia', 'Fantasia'),
        ('RPG', 'RPG'),
        ('Terror', 'Terror'),
        ('Lenda', 'Lenda'),
        ('Outro', 'Outro'),
    ], validators=[DataRequired()])
    conteudo = TextAreaField('Conteúdo(3500 caracteres)', validators=[DataRequired()])


class FormularioJogo(FlaskForm):
    nome= StringField('Nome do jogo', [validators.DataRequired(), validators.length(min=1,max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.length(min=1,max=30)])
    console =StringField('Console', [validators.DataRequired(), validators.length(min=1,max=20)])
    salvar = SubmitField('Salvar')

class LoginUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)], 
                           render_kw={"class": "input", "placeholder": "nickname"})
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)], 
                         render_kw={"class": "input", "placeholder": "senha"})
    login = SubmitField('Login', render_kw={"class": "input"})



class CadastroUsuario(FlaskForm):
    nome = StringField('Nome de Usuário', [validators.Length(min=4, max=25)], render_kw={"class": "input","placeholder": "nome"})
    nickname = StringField('Nickname (Será usado para login)', [validators.DataRequired(), validators.Length(min=1, max=8)], render_kw={"class": "input","placeholder": "nickname"})
    email = StringField('Email', [validators.Length(min=6, max=35)], render_kw={"class": "input","placeholder": "email"})
    senha = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirmacao', message='As senhas devem corresponder')
    ], render_kw={"class": "input","placeholder": "senha"})
    confirmacao = PasswordField('Confirmação de Senha', render_kw={"class": "input","placeholder": "confirmação"})
    cadastrar = SubmitField('Cadastrar', render_kw={"class": "input"})

def id_image(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
    
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = id_image(id)
    if arquivo != 'capa_padrão.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))