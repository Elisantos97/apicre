from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://eli_santosdatabase:Benfica#1904@creproject.database.windows.net/basedadoscre?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)

app.app_context().push()



class Categorias(db.Model):
    idCategoria = db.Column(db.Integer, primary_key=True)
    nomeCategoria = db.Column(db.String(80), unique=True, nullable=False)
    produtos = db.relationship('Produtos', backref='categorias')
    subcategorias = db.relationship('Subcategorias', backref='categorias')

class Subcategorias(db.Model):
    idSubcategoria = db.Column(db.Integer, primary_key=True)
    nomeSubcategoria = db.Column(db.String(80), unique=True, nullable=False)
    produtos = db.relationship('Produtos', backref='subcategorias')
    idCategoria = db.Column(db.Integer, db.ForeignKey('categorias.idCategoria'))

class Produtos(db.Model):
    idProduto = db.Column(db.Integer, primary_key=True)
    nomeProduto = db.Column(db.String(20))
    descricaoProduto = db.Column(db.String(80))
    imagemProduto = db.Column(db.String)
    corProduto = db.Column(db.String(20))
    precoProduto = db.Column(db.Float)
    tipoProduto = db.Column(db.String(20))  ### Interior ou exterior
    especieProduto = db.Column(db.String(20))
    materialProduto = db.Column(db.String)
    tamanhoProduto = db.Column(db.String)
    quantidadeProduto = db.Column(db.Integer)
    marcaProduto = db.Column(db.String)
    referenciaProduto = db.Column(db.String)
    idcategoria = db.Column(db.Integer, db.ForeignKey('categorias.idCategoria'))
    idsubcategoria = db.Column(db.Integer, db.ForeignKey('subcategorias.idSubcategoria'))
    inventarios = db.relationship('Inventarios', backref='produtos')
    galeria_imagens = db.relationship('Galeria_imagens', backref='produtos')


class Inventarios(db.Model):
    idInventario = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    dataEntrada = db.Column(db.DateTime)
    fornecedor = db.Column(db.String(20))
    idproduto = db.Column(db.Integer, db.ForeignKey('produtos.idProduto'))


class Vendas(db.Model):
    idVenda = db.Column(db.Integer, primary_key=True)
    idProduto = db.Column(db.Integer, nullable=False)
    idCliente= db.Column(db.Integer, nullable=False)
    quantidade= db.Column(db.Integer, nullable=False)
    precototal= db.Column(db.Integer, nullable=False)
    iva = db.Column(db.Integer)
    dataVenda = db.Column(db.DateTime)
    nomeEntrega = db.Column(db.String(80))
    moradaEntrega = db.Column(db.String(80))
    nifEntrega = db.Column(db.String(20))
    codigopostalEntrega = db.Column(db.String(80))
    cidadeEntrega = db.Column(db.String(80))

class Carrinho(db.Model):
    idCarrinho = db.Column(db.Integer, primary_key=True)
    idProduto = db.Column(db.Integer, nullable=False)
    idCliente= db.Column(db.Integer, nullable=False)
    quantidade= db.Column(db.Integer, nullable=False)
    precoUnitario = db.Column(db.Integer, nullable=False)
    precoTotal= db.Column(db.Integer, nullable=False)
    

class Produto_relacionado(db.Model):
    idTabela = db.Column(db.Integer, primary_key=True)
    idProduto = db.Column(db.Integer, nullable=False)
    idProduto_relacionado = db.Column(db.Integer)

class Galeria_imagens(db.Model):
    idGaleria = db.Column(db.Integer, primary_key=True)
    imagem = db.Column(db.String)
    idproduto = db.Column(db.Integer, db.ForeignKey('produtos.idProduto'))


class Tipoutilizadores(db.Model):
    idTipoUtilizador = db.Column(db.Integer, primary_key=True)
    nomeTipoUtilizador = db.Column(db.String(80), nullable=False)
    codigoTipoUtilizador = db.Column(db.String(80), nullable=False)
    utilizadores = db.relationship('Utilizadores', backref='tipoutilizadores')


class Utilizadores(db.Model):
    idUtilizador = db.Column(db.Integer, primary_key=True)
    nomeUtilizador = db.Column(db.String(80), nullable=False)
    emailUtilizador = db.Column(db.String(20), unique=True, nullable=False)
    passwordUtilizador = db.Column(db.String(80), nullable=False)
    data_registo_Utilizador = db.Column(db.DateTime)
    data_ultima_entrada_Utilizador = db.Column(db.DateTime)
    telefoneUtilizador = db.Column(db.String(80))
    telemovelUtilizador = db.Column(db.String(80))
    idtipoUtilizador = db.Column(db.Integer, db.ForeignKey('tipoutilizadores.idTipoUtilizador'))


class Clientes(db.Model):
    idCliente = db.Column(db.Integer, primary_key=True)
    nomeCliente = db.Column(db.String(80), nullable=False)
    emailCliente = db.Column(db.String(20), unique=True, nullable=False)
    passwordCliente = db.Column(db.String(80), nullable=False)
    data_registo_Cliente = db.Column(db.DateTime)
    data_ultima_entrada_Cliente = db.Column(db.DateTime)
    telefoneCliente = db.Column(db.String(80))
    telemovelCliente = db.Column(db.String(80))
    nifCliente = db.Column(db.String(80))
    moradaCliente = db.Column(db.String(80))
    codigopostalCliente = db.Column(db.String(80))
    cidadeCliente = db.Column(db.String(80))



class Conta_bancaria(db.Model):
    idConta_bancaria = db.Column(db.Integer, primary_key=True)
    numeroCartao = db.Column(db.String(80), unique=True, nullable=False)
    ccv = db.Column(db.Integer)
    saldo = db.Column(db.Integer)