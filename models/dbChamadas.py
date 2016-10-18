from gluon.tools import Crud

crud = Crud(db) 
Chamadas = db.define_table('chamadas',
    auth.signature,
    Field('protocolo', 'string', label='Protocolo: ', default='', ),
    Field('data_acionamento', 'datetime', label='Acionado em:', default=datetime.datetime.today()),
    Field('atendente_acionamento', 'reference auth_user', label='Atendente acionado: ', default=auth.user_id),
    Field('data_protocolo', 'datetime', label='Protocolado em:', default=datetime.datetime.today()),
    Field('atendente_protocolo', 'reference auth_user', label='Atendente do protocolo: ', default=auth.user_id),
    Field('identificador', 'string', label='Identificador(CPF/CNPJ)'),
    Field('nome', 'string', label='Nome'),
    Field('email', 'string', label='Email'),
    Field('ddd', 'string', label='DDD'),
    Field('telefone', 'string', label='Telefone'),
    Field('cep', 'string', label='CEP/Município'),
    Field('estado', 'string'),
    #Field('cidade', 'string', label='Local (município, cidade, estado)'),
    Field('sistema', 'string', label='Sistema'),
    Field('demanda', 'text', label='Demanda'),
    Field('protocolado', 'boolean', default=False))

db.chamadas.id.writable=False
db.chamadas.id.readable=False

db.chamadas.protocolo.writable = False
db.chamadas.protocolo.readable = False

db.chamadas.data_acionamento.writable = False
db.chamadas.data_acionamento.readable = True

db.chamadas.data_protocolo.writable = False
db.chamadas.data_protocolo.readable = False

db.chamadas.atendente_protocolo.writable = False    
db.chamadas.atendente_protocolo.readable = False

db.chamadas.atendente_acionamento.writable = False
db.chamadas.atendente_acionamento.readable = True

db.chamadas.ddd.writable=False
db.chamadas.ddd.readable=False

db.chamadas.telefone.writable=False
db.chamadas.telefone.readable=False

db.chamadas.cep.writable=False
db.chamadas.cep.readable=False

db.chamadas.demanda.writable=True 
db.chamadas.demanda.readable=True

db.chamadas.protocolado.writable = True
db.chamadas.protocolado.readable = True

