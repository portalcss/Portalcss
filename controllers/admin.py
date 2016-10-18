def index():
	msg = T('Sistema de Contigência de Chamadas')
	total = db(Chamadas.protocolado == False).count()
	form = crud.select(db.chamadas, fields=['data_acionamento', 'sistema', 'email', 'estado'])
	return dict(msg=msg, total=total, form=form)

def chamada():
	msg = T('Chamada')
	return dict(msg=msg)

def protocolo():
	msg = T('Protocolo')
	return dict(msg=msg)

def relatorio():
	msg = T('Relatório')
	total_dia = crud.select(db.chamada)
	return  dict(msg=msg)

def documentos():
	msg = T('Documentos')
	return  dict(msg=msg)


