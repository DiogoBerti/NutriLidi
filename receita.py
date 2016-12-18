#!/usr/bin/env python
# coding: utf-8

class receita(object):
	
	nome = ''
	ingredientes = []
	proteinas_receita = 0
	gorduras_receita = 0
	gorduras_saturadas_receita = 0
	gorduras_trans_receita = 0
	fibra_receita = 0
	sodio_receita = 0
	carboidrato_receita = 0
	porcao = 0
	qtd_total = 0
	calorias = 0
	
	
	#variaveis usadas para incluir os resultados dos calculos em uma lista e fazer a soma final dos valores
	tmp_proteinas = []
	tmp_gorduras = []
	tmp_gorduras_sat = []
	tmp_fibra = []
	tmp_sodio = []
	tmp_carbo = []
	
	
	def __init__(self, nome, porcao):
		self.nome = nome
		self.ingredientes = []
		self.porcao = porcao
		self.tmp_proteinas = []
		
	def adicionar_ingrediente(self, ingrediente, qtd):
		self.ingredientes.append([ingrediente,qtd])
		self.qtd_total = self.qtd_total + qtd
		print 'quantidade total = ' ,self.qtd_total
		
	#deve ser chamado após a adição de todos os itens da receita, para fazer o calculo do total.
	def atualizar_receita(self):
		
		for i in self.ingredientes:
			#calcula proteinas
			calc_prot = ((i[1] * (float(i[0].proteinas)/self.qtd_total)*self.porcao)/100)
			self.tmp_proteinas.append(calc_prot)
			#calcula gorduras
			calc_gord = ((i[1] * (float(i[0].gorduras)/self.qtd_total)*self.porcao)/100)
			self.tmp_gorduras.append(calc_gord)
			#calcula gorduras_saturadas
			calc_gord_sat = ((i[1] * (float(i[0].gorduras_saturadas)/self.qtd_total)*self.porcao)/100)
			self.tmp_gorduras_sat.append(calc_gord_sat)
			# e assim sucessivamente.
			calc_fibra = ((i[1] * (float(i[0].fibra)/self.qtd_total)*self.porcao)/100)
			self.tmp_fibra.append(calc_fibra)
			calc_sodio = ((i[1] * (float(i[0].sodio)/self.qtd_total)*self.porcao)/100)
			self.tmp_sodio.append(calc_sodio)
			calc_carbo = ((i[1] * (float(i[0].carboidrato)/self.qtd_total)*self.porcao)/100)
			self.tmp_carbo.append(calc_carbo)
			
		self.proteinas_receita = sum(self.tmp_proteinas)
		self.gorduras_receita = sum(self.tmp_gorduras)			
		self.gorduras_saturadas_receita = sum(self.tmp_gorduras_sat)			
		self.fibra_receita = sum(self.tmp_fibra)
		self.sodio_receita = sum(self.tmp_sodio)
		self.carboidrato_receita = sum(self.tmp_carbo)

	def to_string(self):
		print 'Nome da receita: %s\n Quantidade total: %s\n'%(self.nome,self.qtd_total) 
		
		
	def calculo_calorias(self):
		#aqui é feito o calculo de calorias para a receita.
		#Deve ser realizado ao final da receita.
		tempGord = (self.proteinas_receita * 4) + (self.carboidrato_receita * 4) + (self.gorduras_receita * 9)
		if tempGord >= 100:
			self.calorias = int(tempGord)
		elif tempGord >= 10:
			self.calorias = int(tempGord)
		else:
			self.calorias = round(tempGord, 1)
		
		
		
		
		
		
		
		
		
		
	
