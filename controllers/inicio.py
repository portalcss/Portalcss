@auth.requires_login()
def index():
	PROTOCOLADO = True
	export_classes = dict(csv=False	, json=False, html=False,
                          tsv=False, xml=False, csv_with_hidden_cols=False,
                          tsv_with_hidden_cols=False)
	msg = T('Sistema de Contigência de Chamadas')
	chamada.total = db(Chamadas).count()
	chamada.acionamento_total = db(Chamadas.protocolado == False).count()
#	chamada.acionamento_tabela = crud.select(db.chamadas, db.chamadas.protocolado == False, fields=['data_acionamento', 'sistema', 'email', 'estado'])
	query=(db.chamadas.protocolado != PROTOCOLADO)
	chamada.acionamento_tabela = SQLFORM.grid(query, searchable=False, deletable=False, editable=False, create=False,paginate=5,  exportclasses=export_classes)
	chamada.protocolomento_total = db(Chamadas.protocolado == True).count()
	#chamada.protocolamento_tabela = crud.select(db.chamadas, db.chamadas.protocolado == True, fields=['data_acionamento', 'data_protocolo', 'sistema', 'email', 'estado'])
	db.chamadas.atendente_protocolo.writable = False
	db.chamadas.atendente_protocolo.readable = True
	db.chamadas.atendente_acionamento.writable = False	
	db.chamadas.atendente_acionamento.readable = False
	db.chamadas.data_acionamento.writable = False
	db.chamadas.data_acionamento.readable = True
	db.chamadas.data_protocolo.writable = False
	db.chamadas.data_protocolo.readable = True
	query = (db.chamadas.protocolado == PROTOCOLADO)

	chamada.protocolamento_tabela = DIV(DIV('Chamadas Protocoladas', _class='panel-heading'), SQLFORM.grid(query,  searchable=False, deletable=False, editable=False, create=False, paginate=5, exportclasses=export_classes), _class='panel panel-primary')
	nome = auth.user.first_name
	return dict(msg=msg, chamada=chamada, nome=nome)

def chamada():
	msg = T('Chamada')

	return dict(msg=msg)

def protocolo():
	msg = T('Protocolo')	
	return dict(msg=msg)


@auth.requires_login()
def manage():
    table = request.args(0)
    if not table in db.tables(): redirect(URL('error'))
    grid = SQLFORM.grid(db[table],args=request.args[:1])
    return locals()

def list_items():
    if len(request.args):
    	page=int(request.args[0])
    else:
    	page=0
    items_per_page=2
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    query=(db.chamadas.ALL)
    rows=db().select(query,limitby=limitby)
    return dict(rows=rows,page=page,items_per_page=items_per_page)