class No:
     def __init__(self, key, dir, esq):
          self.item = key
          self.dir = dir
          self.esq = esq

class Tree:
    def __init__(self):
         self.root = No(None,None,None)
         self.root = None

    def inserir(self, v):
         novo = No(v,None,None)
         
         if self.root == None:
              self.root = novo
         else:
              atual = self.root
              while True:
                   anterior = atual
                   if v <= atual.item:
                        atual = atual.esq
                        if atual == None:
                               anterior.esq = novo
                               return
                   else:
                        atual = atual.dir
                        if atual == None:
                                anterior.dir = novo
                                return
      
    def inOrder(self, atual):
        if atual != None:
             self.inOrder(atual.esq)
             print(atual.item,end=" ")
             self.inOrder(atual.dir)
  
    def preOrder(self, atual):
        if atual != None:
             print(atual.item,end=" ")
             self.preOrder(atual.esq)
             self.preOrder(atual.dir)
      
    def posOrder(self, atual):
        if atual != None:
             self.posOrder(atual.esq)
             self.posOrder(atual.dir)
             print(atual.item,end=" ")

def letraExisteNoArray(letra:str, array) -> bool:
    for ch in array:
        if ch == letra:
            return True
    return False

def separarCaracteres(frase:str) -> []:
    caracteresSeparados = []
    for letra in frase:
        if not letraExisteNoArray(letra, caracteresSeparados):
            caracteresSeparados.append(letra)
    return caracteresSeparados

def contarFrequencia(frase:str) -> []:
    caracteresSeparados = separarCaracteres(frase)
    frequencias = []
    contador = 0

    caractesEFrequencias = {}
    
    for ch in caracteresSeparados:
        for letra in frase:
            if letra == ch:
                contador+=1
                
        frequencias.append(contador)
        caractesEFrequencias[ch] = contador
        contador = 0
    
    return [frequencias, caracteresSeparados, caractesEFrequencias]


if __name__ == '__main__':
    
    #https://pt.wikipedia.org/wiki/Codifica%C3%A7%C3%A3o_de_Huffman

    arv = Tree()
   
    frase:str = "CASA PAPEL HOTEL PASTEL" 
    [frequencias, caracteresSeparados, caracteresEfrequencias] = contarFrequencia(frase)

    print("------\n")

    for freq in caracteresEfrequencias:
        print(freq, caracteresEfrequencias[freq])
    
    frequencias.sort()

    print(f"\nfrequencias ordenadas: {frequencias}\n")

