from collections import deque
from prueba.model import DBSession, Item, Relacion

class CalculoImpacto():
  def __init__(self,codItem):
	self.codItem= codItem
	self.cola = deque()
	self.cola.append(self.codItem)
	self.hash = {}
      	
  def calcular(self):
	self.hash[self.codItem]=self.codItem
	listaItemInicio = list()
	listaItemFin= list()
	aux = list()
	impacto = 0
	while(self.cola):
		coditemActual = self.cola.popleft()
		itemNuevo =  DBSession.query(Item).filter_by(coditem=coditemActual).one()
		print "calculando....................." + str(coditemActual) + " =========== " + str(itemNuevo.complejidad)
		impacto = impacto + itemNuevo.complejidad

		listaItemInicio = DBSession.query(Relacion).filter_by(coditeminicio=itemNuevo.coditem).all()
                for x in listaItemInicio:
			if not self.hash.has_key(x.coditemfin):
                    		#aux.append(x.coditemfin)
                		self.cola.append(x.coditemfin)
				self.hash[x.coditemfin]=x.coditemfin

                listaItemFin = DBSession.query(Relacion).filter_by(coditemfin=itemNuevo.coditem).all()
                for x in listaItemFin:
			if not self.hash.has_key(x.coditeminicio):
				#aux.append(x.coditemfin)
				self.cola.append(x.coditeminicio)
				self.hash[x.coditeminicio]=x.coditeminicio

	#	for coditem in aux:
	#		self.cola.append(coditem)
	#		self.hash[coditem]=coditem
	return (impacto)    
