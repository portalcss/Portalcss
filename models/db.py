    # -*- coding: utf-8 -*-
import datetime
# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")


# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = [Field('cpf', 'string',requires=IS_MATCH('\d{11}'), unique=True)]
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.create_user_groups = False







# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)

'''Tabela estados foi criada assim para permitir o Atendente o registro apartir de seu conhecimento tácito.'''

Sistemas = db.define_table('sistemas',
    Field('nome', 'string', label='Sistema'))

estados = ('Acre/AC','Alagoas/AL','Amapá/AP','Amazonas/AM','Bahia/BA','Ceará/CE','Distrito Federal/DF','Espírito Santo/ES','Goiás/GO','Maranhão/MA','Mato Grosso/MT','Mato Grosso do Sul/MS','Minas Gerais/MG','Pará/PA','Paraíba/PB','Paraná/PR','Pernambuco/PE','Piauí/PI','Rio de Janeiro/RJ','Rio Grande do Norte/RN','Rio Grande do Sul/RS','Rondônia/RO','Roraima/RR','Santa Catarina/SC','São Paulo/SP','Sergipe/SE','Tocantins/TO')
sistemas = (
    'MRE - Acionamento Eletrônico Internacional',
    'Ministério da Justiça - Sinesp e Sisdepen',
    'Serviços Renavam, Renach, Renainf, Simrav e Renajud',
    'Portal do Empreendedor – Empreendedor Individual',
    'Rais - Relação Anual de Informações Sociais',
    'Cliente Ministério do Planejamento/Sispac',
    'Serviços da Segrt / Seges - MPOG (Siape, Siapenet, Sigepe, Siorg e outros)',
    'Serviços ComprasNet e Siasg',
    'Cliente Dnit - Depto Nacional de Infra. de Transportes',
    'Serviços do Comércio Exterior / Mercante',
    'Cliente Ministério da Fazenda',
    'Cliente PGFN - Procuradoria Geral da Fazenda Nacional',
    'Serviço de Gestão de Margem Consignável',
    'Rede Infovia',
    'SPED  -  Sistema Público de Escrituração Digital e seus Módulos',
    'Porto sem Papel',
    'Departamento de Polícia Federal - Ministério da Justiça',
    'Programa Serpro de Inclusão Digital',
    'Secretaria da Micro e Pequena Empresa - SMPE',
    'Certificação Digital, Correio Eletrônico - Expresso, SUFRAMA, demais serviços e clientes')

ddd = ('11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99')

#('Acre/AC','Alagoas/AL','Amapá/AP','Amazonas/AM','Bahia/BA','Ceará/CE','Distrito Federal/DF','Espírito Santo/ES','Goiás/GO','Maranhão/MA','Mato Grosso/MT','Mato Grosso do Sul/MS','Minas Gerais/MG','Pará/PA','Paraíba/PB','Paraná/PR','Pernambuco/PE','Piauí/PI','Rio de Janeiro/RJ','Rio Grande do Norte/RN','Rio Grande do Sul/RS','Rondônia/RO','Roraima/RR','Santa Catarina/SC','São Paulo/SP','Sergipe/SE','Tocantins/TO'))]