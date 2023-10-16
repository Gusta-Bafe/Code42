from CV42 import db

class Usuarios(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(8), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    jogos = db.relationship('Jogos', backref='usuario', lazy=True)
    historias = db.relationship('Historias', backref='usuario', lazy=True)
    personagens = db.relationship('Personagens', backref='usuario', lazy=True)
    PerfilUsuario = db.relationship('PerfilUsuario', backref='usuario', lazy=True)
    
    def __repr__(self):
        return '<Name %r>' % self.nome
    
class PerfilUsuario(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    localizacao = db.Column(db.String(50), nullable=False)
    interesse = db.Column(db.Text(), nullable=False)
    dispositivos = db.Column(db.Text)
    sistema_operacional = db.Column(db.String(20), nullable=False)
    evento_geek = db.Column(db.String(255), nullable=False)
    item_colecionavel = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    def __repr__(self):
        return '<PerfilUsuario %r>' % self.id


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)
    publico = db.Column(db.Boolean, default=False, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    publico = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return '<Name %r>' % self.nome

    
class Historias(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(30), nullable=False)
    genero = db.Column(db.String(15), nullable=False)
    publico = db.Column(db.Boolean, default=False, nullable=False)
    conteudo = db.Column(db.String(1000), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    publico = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Title %r>' % self.titulo

class Personagens(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    classe = db.Column(db.String(20), nullable=False)
    raca = db.Column(db.String(15), nullable=False)
    publico = db.Column(db.Boolean, default=False, nullable=False)
    personalidade = db.Column(db.String(60), nullable=False)
    backgraund = db.Column(db.String(300), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome