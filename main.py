#!/usr/bin/env python
# coding: utf-8

from Ingrediente import *
import csv, codecs
from receita import *


def load_ingredientes():
	
	ifile  = codecs.open('nutriLidiBase.csv', 'r')
	reader = csv.reader(ifile)

	lista_ingredientes = []
			
	for row in reader:
		params = []
		params = str(row).split(";")
		
		
		lista_ingredientes.append(Ingrediente(params[1].decode('string_escape'),params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[0]))
			
	ifile.close()
	return lista_ingredientes
	
def load_receitas():
	pass


def gravar_receitas():
	pass


def adicionar_ingrediente(lista_ingredientes, titulo, proteinas, gorduras, gorduras_saturadas, gorduras_trans, fibra, sodio, carboidrato):
	ingr_id = len(lista_ingredientes) + 1
	return Ingrediente(titulo, proteinas, gorduras, gorduras_saturadas, gorduras_trans, fibra, sodio, carboidrato, ingr_id)
		


def gravar_ingredientes(lista_ingredientes):
	#ifile  = codecs.open('nutriLidiBase.csv', 'r')
	#reader = csv.reader(ifile)
	ofile = open('tempnutriLidiBase.txt', 'w')
	#writer = writer(ofile)
	
	for i in lista_ingredientes:
		ofile.write(i.ingrediente_id + ";" + i.titulo + ";" + i.proteinas + ";" + i.gorduras + ";" +
						 i.gorduras_saturadas + ";" + i.gorduras_trans + ";" + i.fibra + ";" + i.sodio +
						 ";" + i.carboidrato + "\n")
		
	
	

								 
		
	
	
if __name__ == '__main__':
	
	lista_ingredientes = load_ingredientes()
	
	novareceita = receita("receita teste",50)
	novareceita.adicionar_ingrediente(lista_ingredientes[1],150)
	novareceita.adicionar_ingrediente(lista_ingredientes[2],150)

	
	
	
	print novareceita.nome
	
	novareceita.atualizar_receita()
	
	for ingr in novareceita.ingredientes:
		print ingr[0].titulo
		print ingr[1]
	
	print novareceita.proteinas_receita
	print novareceita.gorduras_receita
	
	
	novareceita.calculo_calorias()
	
	print novareceita.calorias
	
	#for i in lista_ingredientes:
	#	print i.titulo
	print lista_ingredientes[2].to_string()
	#print lista_ingredientes[2].proteinas
	
	gravar_ingredientes(lista_ingredientes)
	print 'programa finalizado'
	
		