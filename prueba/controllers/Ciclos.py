from prueba.model import DBSession, Item, Relacion

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
            relacionAux = DBSession.query(Relacion).filter_by(coditeminicio=x.coditem).all()
            for j in relacionAux:
                print j.coditeminicio
                print j.coditemfin
                if j.coditemfin in auxItemFase:
                    padres.append(j.coditeminicio)
                    listaItem.append(j.coditeminicio)
                    hijos.append(j.coditemfin)
        
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        print listaItem
        print "****************************************************************"
        print padres
        print "----------------------------------------------------------------"
        print hijos
        
        for inicio in padres:
            pila.append(inicio)
            while(pila and ciclo==0):
                origen = pila.pop()
                if not origen in visitados:
                    visitados.append(origen)
                while origen in listaItem:
                    i = listaItem.index(origen)
                    listaItem[i] = -1
                    print "nuevo index ====================================================================== " + str(i)
                    print "////////////////////////////lista de visitados //////////////////////////////////////////////////////////////////////////////"
                    print visitados
                    print "////////////////////////////lista de en Lista de _Item //////////////////////////////////////////////////////////////////////////////"
                    print listaItem
                    if hijos[i] in visitados:#mirar si no fue visistado.hay ciclo y se pasa al sgt valor en la lista padres
                        pila = list()
                        visitados = list()
                        listaItem = list()
                        print "hay ciclo en el proceso /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/"
                        print visitados
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