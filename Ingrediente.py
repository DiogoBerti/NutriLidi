#!/usr/bin/env python
# coding: utf-8 

class Ingrediente(object):
	
	ingrediente_id = 0
	titulo = ''
	quantidade = 0
	proteinas = 0
	gorduras = 0
	gorduras_saturadas = 0
	gorduras_trans = 0
	fibra = 0
	sodio = 0
	carboidrato = 0
	
	def __init__(self, titulo, proteinas, gorduras, gorduras_saturadas, gorduras_trans, fibra, sodio, carboidrato, ingrediente_id):
		self.titulo = titulo
		self.proteinas = proteinas
		self.gorduras = gorduras
		self.gorduras_saturadas = gorduras_saturadas
		self.gorduras_trans = gorduras_trans
		self.fibra = fibra
		self.sodio = sodio
		self.carboidrato = carboidrato
		self.ingrediente_id = ingrediente_id
	
	
	def to_string(self):
		print self.titulo, " :\nProteinas: ", self.proteinas, "\nGorduras: ", self.gorduras,"\nGorduras Saturadas: ", self.gorduras_saturadas
	
		

					
					
					