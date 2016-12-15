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
	
	#variaveis usadas para incluir os resultados dos calculos em uma lista e fazer a soma final dos valores
	tmp_proteinas = []
	tmp_gorduras = []
	
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
			
			
		self.proteinas_receita = sum(self.tmp_proteinas)
		self.gorduras_receita = sum(self.tmp_gorduras)			
		
		
		
			#self.gorduras_receita = ((i[1] * i[0].gorduras)/self.qtd_total)/self.porcao
			
#qtd*(valor_ingred/total)*porcao)/100									  
	
		
	
	
