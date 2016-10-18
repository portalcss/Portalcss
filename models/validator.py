#-*- coding: utf-8 -*-

Chamadas.identificador.requires = IS_NOT_EMPTY('Informe o identificador(CPF). Ex.: 000.000.000-00') and IS_CPF_OR_CNPJ()
Chamadas.atendente_acionamento.requires = IS_NOT_EMPTY('Logue-se no sistema!')	
Chamadas.nome.requires = IS_NOT_EMPTY('Informe o nome!')
Chamadas.email.requires = IS_NOT_EMPTY('Informe o email!')  and IS_EMAIL(error_message=T('Informe um email válido'))
Chamadas.ddd.requires = IS_NOT_EMPTY('Informe o DDD!') and IS_MATCH('[0-9]{2}', 'Formato inválido! Ex.: 00') and IS_IN_SET(range(1,67), labels=ddd, multiple=False, zero=T('DDD'), error_message='Escolha o ddd!')
Chamadas.telefone.requires = [IS_NOT_EMPTY('Informe o telefone!') and IS_MATCH('[0-9]{8,10}$', 'Formato inválido! Ex.: 00000000 ou 0000000000')]
Chamadas.cep.requires = IS_NOT_EMPTY('Informe o CEP ou município')
Chamadas.estado.requires = IS_IN_SET(estados, labels=estados, multiple=False, zero=T('Selecione'), error_message='Escolha um estado!')
Chamadas.sistema.requires = IS_IN_SET(sistemas, labels=sistemas, multiple=False, zero=T('Selecione'), error_message='Escolha o sistema!')
Chamadas.demanda.requires = IS_NOT_EMPTY('É necessário informar a demanda!')
Chamadas.data_acionamento.requires = IS_DATETIME(format='%d/%m/%Y %H:%M:%S')
Chamadas.data_protocolo.requires = IS_DATETIME(format='%d/%m/%Y %H:%M:%S')