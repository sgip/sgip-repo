from prueba.model import DBSession, Item, Relacion,Fase
from sqlalchemy import or_,and_

class Ciclos:
  def __init__(self,codItem,itemFin):
      self.codItem= codItem
      self.itemFin = itemFin
      
  def calcular(self):
        item = DBSession.query(Item).filter_by(coditem=self.codItem).one()
        itemFase = item.fase.items
        auxItemFase = list()
        padres = list()
        hijos = list()
        relacion_act = list() 
        listaItem = list()
        pila = list() 
        visitados = list()
        ciclo = 0
        
        padres.append(self.codItem)
        hijos.append(self.itemFin)
        listaItem.append(self.codItem)
        
        for i in itemFase:   
            auxItemFase.append(i.coditem)
           
        for x in itemFase:
            relacionAux = DBSession.query(Relacion).filter_by(coditeminicio=x.coditem).filter_by(tipo='padre-hijo').all()
            for j in relacionAux:
            #    print j.coditeminicio
             #   print j.coditemfin
              #   if j.coditemfin in auxItemFase:
                padres.append(j.coditeminicio)
                listaItem.append(j.coditeminicio)
                hijos.append(j.coditemfin)
        
      # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
       # print listaItem
        #print "****************************************************************"
       # print padres
       # print "----------------------------------------------------------------"
        #print hijos
        
        for inicio in padres:
            pila.append(inicio)
            while(pila and ciclo==0):
                origen = pila.pop()
                if not origen in visitados:
                    visitados.append(origen)
                while origen in listaItem:
                    i = listaItem.index(origen)
                    listaItem[i] = -1
              #  print "nuevo index ====================================================================== " + str(i)
               #     print "////////////////////////////lista de visitados //////////////////////////////////////////////////////////////////////////////"
                #    print visitados
                 #   print "////////////////////////////lista de en Lista de _Item //////////////////////////////////////////////////////////////////////////////"
                  #  print listaItem """
                    if hijos[i] in visitados:#mirar si no fue visistado.hay ciclo y se pasa al sgt valor en la lista padres
                        pila = list()
                        visitados = list()
                        listaItem = list()
                       # print "hay ciclo en el proceso /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/"
                        #print visitados"""
                        ciclo = 1
                        return ciclo 
                        break
                    else:
                        pila.append(hijos[i])
                        visitados.append(hijos[i])
            if ciclo==1:
                break
            listaItem=list()
            visitados=list()
            for x in padres:
                listaItem.append(x)
                
        return ciclo

  def tieneAntecesor(self):
        #trae el item correspondiente
        item = DBSession.query(Item).filter_by(coditem=self.codItem).one() 
        # los items de la fase actual
        itemFase = item.fase.items 
        faseItemAnt = int(item.fase.codfase) -1  
        #los antecesores y sucesores del item dado
        antecesores = DBSession.query(Relacion).filter_by(coditemfin=self.codItem).filter_by(tipo='antecesor-sucesor').all()
        #fase anterior a la actual 
        faseAnt = DBSession.query(Fase).filter_by(codfase=faseItemAnt).one()
        #items de la fase anterior
        itemFaseAnt = DBSession.query(Item).filter_by(fase=faseAnt).all()
        
        itemFaseAnterior = list()
        pila = list()
          
        print "########################### items fase anterior ####################################### ", self.codItem 
        for h in itemFaseAnt:
            itemFaseAnterior.append(h.coditem)
            print h.coditem
        print "//////////////////////////"
            
        #si tiene una antecesor directo, retorna que tiene antecesor    
        for j in antecesores:
            if j.coditeminicio in auxItemFaseAnterior:
                return 1   
        
        #los items que son padres del actual
        padres = DBSession.query(Relacion).filter_by(coditemfin=self.codItem).filter_by(tipo='padre-hijo').all()
        for i in padres:
            pila.append(i.coditeminicio)  
          
        while(pila):
            x = pila.pop()
            antecesores = DBSession.query(Relacion).filter_by(coditemfin=x).filter_by(tipo='antecesor-sucesor').all()
            cantidad=0
            print "###################################################################"
            for m in antecesores:
                cantidad = cantidad + 1
                m.coditeminicio
            print "###################################################################"
            if cantidad == 0:
                print "nulooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
                antecesores = DBSession.query(Relacion).filter_by(coditemfin=x).filter_by(tipo='padre-hijo').all()
                for i in antecesores:   
                    pila.append(i.coditeminicio)
            else:
                for j in antecesores:
                    if j.coditeminicio in itemFaseAnterior:
                        return 1
        return 0
                    