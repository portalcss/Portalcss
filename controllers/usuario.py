@auth.requires(auth.user_id==auth.user_id or request.client=='127.0.0.1', requires_login=True)
def index():	
	msg = T('Index')
	#form = DIV(DIV(DIV('Atendimento ', SPAN('Total: %s'%total, _class='badge')), _class='panel-heading'),DIV(SQLFORM.grid(query, deletable=False, create=False, paginate=5), _class='panel-body'), _class='panel panel-primary')
	chamada = DIV(DIV('Chamadas', _class='panel-heading'),DIV('Chamada', _class='panel-body'), _class='panel panel-primary')
	protocolo = DIV(DIV('Protocolo', _class='panel-heading'),DIV('Chamada', _class='panel-body'), _class='panel panel-primary')
	
	return dict(msg=msg, chamada=chamada, protocolo=protocolo)



def relatorio():
	msg = T('Relatório')
	total_dia = crud.select(db.chamada)
	return  dict(msg=msg)

def documentos():
	msg = T('Documentos')
	return  dict(msg=msg)

