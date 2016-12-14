#!/usr/bin/env python
# coding: utf-8 

from Ingrediente import *
import csv


def load_ingredientes():
	
	ifile  = open('nutriLidiBase.csv', "rb")
	reader = csv.reader(ifile)

	lista_ingredientes = []
		
	
	
	for row in reader:
		# Save header row.
		params = []
		#params = row.split(";")
		params = str(next(reader)).split(";")
		lista_ingredientes.append(Ingrediente(params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8]))
		
		
	for ingr in lista_ingredientes:
		print ingr.titulo
								  
	ifile.close()

if __name__ == '__main__':
	load_ingredientes()
	
	print "OK"
		