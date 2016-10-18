
def index():
	response.flash = T('Acionamentos')
	return dict(message=T('Cadastre novos acionamentos'))
#,fields=['protocolo','identificador','nome','email','telefone','cep','estado','sistema', 'data_acionamento', 'atendente_acionamento', 'atendente_protocolo', 'data_protocolo','demanda'],submit_button='Salvar'



@auth.requires_login()
def nova_chamada():
	form = SQLFORM(Chamadas, submit_button='Enviar', reset_button='Limpar', separator=': ')
	#form.add_button(type='reset')
	#form.add_button('Limpar', type='reset')
	if form.process().accepted:
		session.flash = 'Novo acionamento registrado: %s' % form.vars.identificador
		#redirect(URL('nova_chamada'))
		redirect(URL(request.application, c='inicio', f='index'))		
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if  not response.flash:
			response.flash = 'Preencha o formulário!'
	return dict(form=form)

@auth.requires_login()
def meus_chamados():
	if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
	return dict(total=total, form=container)
	PROTOCOLADO = True
	query=(Chamadas.atendente_acionamento == auth.user_id)
	total = db(query).count()
	#form = crud.select(db.chamadas == auth.user_id, fields=['data_acionamento', 'sistema', 'email', 'estado'])
	form = DIV(DIV(DIV('Atendimento ', SPAN('Total: %s'%total, _class='badge')), _class='panel-heading'),DIV(SQLFORM.grid(query, deletable=False, create=False, paginate=5), _class='panel-body'), _class='panel panel-primary')
	container = DIV(DIV(DIV(form), _class='row'), _class='container-fluid')


@auth.requires_login()
def ver_chamados():
	PROTOCOLADO = True
	query=(Chamadas.atendente_acionamento)
	total = db(query).count()
	#form = crud.select(db.chamadas == auth.user_id, fields=['data_acionamento', 'sistema', 'email', 'estado'])
	form = DIV(DIV(DIV('Atendimento ', SPAN('Total: %s'%total, _class='badge')), _class='panel-heading'),DIV(SQLFORM.grid(query, deletable=False, create=False, editable=False, paginate=5), _class='panel-body'), _class='panel panel-primary')
	container = DIV(DIV(DIV(form), _class='row'), _class='container-fluid')
	return dict(total=total, form=container)


'''
@auth.requires_membership('atendimento2')
def nova_chamada():
	form = SQLFORM.grid(Chamadas)
	if form.process().accepted:
		session.flash = 'Novo acionamento registrado: %s' % form.vars.identificador
		redirect(URL('nova_chamada'))
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if  not response.flash:
			response.flash = 'Preencha o formulário!'
	return dict(form=form)
'''

 
def ver_chamada():
	grid = SQLFORM.grid(Chamadas)
	return dict(grid=grid)

@auth.requires_membership('atendente')
def ver_protocolos():
	db.chamadas.id.readable=True
	db.chamadas.protocolo.writable = db.chamadas.protocolo.readable = True
	db.chamadas.data_protocolo.readable = True
	db.chamadas.atendente_protocolo.writable = False
	db.chamadas.atendente_protocolo.readable = False
	query=(db.chamadas.protocolado == False)
	form = SQLFORM.grid(query, selectable= lambda ids : redirect(URL('chamada', 'protocolar_chamada', vars=dict(id=ids))))
	return dict(form=form)

def protocolar_chamada():
	db.chamadas.protocolo.writable = db.chamadas.protocolo.readable = True
	db.chamadas.atendente_protocolo.writable = False
	db.chamadas.atendente_protocolo.readable = True
	db.chamadas.data_acionamento.writable = False
	db.chamadas.data_acionamento.readable = True
	db.chamadas.data_protocolo.writable = False
	db.chamadas.data_protocolo.readable = True
	db.chamadas.identificador.writable = False	
	db.chamadas.identificador.readable = True
	db.chamadas.nome.writable = False	
	db.chamadas.nome.readable = True
	db.chamadas.email.writable = False	
	db.chamadas.email.readable = True
	db.chamadas.estado.writable = False	
	db.chamadas.estado.readable = True
	db.chamadas.sistema.writable = False	
	db.chamadas.sistema.readable = True
	db.chamadas.demanda.writable = False	
	db.chamadas.demanda.readable = True
	db.chamadas.cep.writable = False	
	db.chamadas.cep.readable = True
	db.chamadas.ddd.writable = False	
	db.chamadas.ddd.readable = True
	db.chamadas.telefone.writable = False	
	db.chamadas.telefone.readable = True
	record = db.chamadas(request.vars.id)
	form = SQLFORM(db.chamadas, record)
   	if form.process().accepted:
   		db(db.chamadas == record).update(protocolado=True)
   		response.flash = 'form accepted'
   	elif form.errors:
   		response.flash = 'form has errors'	
	return dict(form=form)


def relatorio():
	form = SQLFORM(chamadas)
	return dict(form=form)



'''weekdays =("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
form = SQLFORM.factory(
Field('data_acionamento', default=datetime.datetime.today(), readable=True, writable=False),
Field('atendente_acionamento', default=auth.user.first_name+auth.user.last_name,  readable=True, writable=False),
Field('data_protocolo', default=datetime.datetime.today(), readable=True, writable=False),
Field('atendente_protocolo', default=auth.user.first_name+auth.user.last_name, readable=True, writable=False),
Field('protocolo', default='0000/000000000', readable=True, writable=False),
Field('identificador', requires=IS_NOT_EMPTY('Preencha com CPF/CNPJ')),
Field('nome'),
Field('email', requires=IS_EMAIL()),
Field('telefone', requires=''),
Field('cep', requires=''),
Field('estado', requires=IS_IN_SET(range(1,8), labels=weekdays, multiple=False)),
Field('data_protocolo', requires=''),
Field('demanda', 'text', requires='')
)
'''
	