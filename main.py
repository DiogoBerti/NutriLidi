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
		# Save header row.
		params = []
		#params = row.split(";")
		params = str(next(reader)).split(";")
		lista_ingredientes.append(Ingrediente(params[1].decode('string_escape'),params[2],params[3],params[4],params[5],params[6],params[7],params[8]))
			
	'''for ingr in lista_ingredientes:
		print ingr.titulo
	'''
	
	ifile.close()
	return lista_ingredientes
	
	
if __name__ == '__main__':
	
	lista_ingredientes = load_ingredientes()
	
	novareceita = receita("receita teste",50)
	novareceita.adicionar_ingrediente(lista_ingredientes[1],150)
	novareceita.adicionar_ingrediente(lista_ingredientes[0],150)

	'''
	print novareceita.nome
	
	novareceita.atualizar_receita()
	
	for ingr in novareceita.ingredientes:
		print ingr[0].titulo
		print ingr[1]
	
	print novareceita.proteinas_receita
	print novareceita.gorduras_receita
	
	novareceita.to_string()
	'''
	for i in lista_ingredientes:
		print i.titulo
	
	
	print 'programa finalizado'
	
		