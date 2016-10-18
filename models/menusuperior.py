# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menusuperior = [
    (T('Início'), False, URL('inicio', 'index'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menusuperior += [
        (T('Registros'), False, URL('usuario', 'index')),
        (T('Chamadas'), False, '#', [
            (T('Nova Chamada'), False, URL('chamada', 'nova_chamada')),
            LI(_class="divider"),
            (T('Ver Chamadas'), False,
             URL(
                 'chamada', 'ver_chamada'))
        ]),
        ('Ferramentas', False, '#', [
            (T('Spekx'), False,
             'http://192.168.202.48/'),
            (T('SCCD'), False,
             'http://192.168.202.48/maximo/ui/login'),
            (T('Script'), False, 'http://192.168.202.48:82')
        ]),
        (T('Clientes'), False, '#', [
            (T('Telefones'), False, 'http://www.web2py.com/book'),
            LI(_class="divider"),
            (T('MRE - Acionamento Eletrônico Internacional'), False,
             'http://www.web2py.com/book/default/chapter/00'),
            (T('Ministério da Justiça - Sinesp e Sisdepen'), False,
             'http://www.web2py.com/book/default/chapter/01'),
            (T('Serviços Renavam, Renach, Renainf, Simrav e Renajud'), False,
             'http://www.web2py.com/book/default/chapter/02'),
            (T('Portal do Empreendedor – Empreendedor Individual'), False,
             'http://www.web2py.com/book/default/chapter/03'),
            (T('Rais - Relação Anual de Informações Sociais'), False,
             'http://www.web2py.com/book/default/chapter/04'),
            (T('Cliente Ministério do Planejamento/Sispac'), False,
             'http://www.web2py.com/book/default/chapter/05'),
            (T('Serviços da Segrt / Seges - MPOG (Siape, Siapenet, Sigepe, Siorg e outros)'), False,
             'http://www.web2py.com/book/default/chapter/06'),
            (T('Serviços ComprasNet e Siasg'), False,
             'http://www.web2py.com/book/default/chapter/07'),
            (T('Cliente Dnit - Depto Nacional de Infra. de Transportes'), False,
             'http://www.web2py.com/book/default/chapter/08'),
            (T('Serviços do Comércio Exterior / Mercante'), False,
             'http://www.web2py.com/book/default/chapter/09'),
            (T('Cliente Ministério da Fazenda'), False,
             'http://www.web2py.com/book/default/chapter/10'),
            (T('Cliente PGFN - Procuradoria Geral da Fazenda Nacional'), False,
             'http://www.web2py.com/book/default/chapter/11'),
            (T('Serviço de Gestão de Margem Consignável'), False,
             'http://www.web2py.com/book/default/chapter/12'),
            (T('Rede Infovia'), False,
             'http://www.web2py.com/book/default/chapter/13'),
            (T('SPED  -  Sistema Público de Escrituração Digital e seus Módulos'), False,
             'http://www.web2py.com/book/default/chapter/14'),
            (T('Porto sem Papel'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T('Departamento de Polícia Federal - Ministério da Justiça',), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T('Programa Serpro de Inclusão Digital'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T('Secretaria da Micro e Pequena Empresa - SMPE'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T('Certificação Digital, Correio Eletrônico - Expresso, SUFRAMA, demais serviços e clientes'), False,
             'http://stores.lulu.com/web2py'),
        ]),
        (T('Arquivos'), False, None, [
            (T('Groups'), False,
             'http://www.web2py.com/examples/default/usergroups'),
            (T('Twitter'), False, 'http://twitter.com/web2py'),
            (T('Live Chat'), False,
             'http://webchat.freenode.net/?channels=web2py'),
        ]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
