codigos = {}

class Node:
    def __init__(self, frequencia, caractere, esquerda=None, direita=None):
        self.frequencia = frequencia
        self.caractere = caractere
        self.esquerda = esquerda
        self.direita = direita
        self.codigo = ''

def contarFrequencias(dados):
    caracteres = {}
    for element in dados:
        if caracteres.get(element) == None:
            caracteres[element] = 1
        else: 
            caracteres[element] += 1     
    return caracteres

def calcularCodigos(no, valor=''):
    novo_valor = valor + str(no.codigo)

    if(no.esquerda):
        calcularCodigos(no.esquerda, novo_valor)
    if(no.direita):
        calcularCodigos(no.direita, novo_valor)

    if(not no.esquerda and not no.direita):
        codigos[no.caractere] = novo_valor
         
    return codigos        

def textoCodificado(dados, codigos):
    texto_codificado = []
    for c in dados:
        texto_codificado.append(codigos[c])
        
    string = ''.join([str(item) for item in texto_codificado])    
    return string
          
          
def comprimir(dados):
    caracteres_e_frequencias = contarFrequencias(dados)
    caracteres = caracteres_e_frequencias.keys()
    frequencias = caracteres_e_frequencias.values()

    print(f"\ncaracteres: {list(caracteres)}")
    print(f"frequencia: {list(frequencias)}")
    nos = []
    
    for caractere in caracteres:
        nos.append(Node(caracteres_e_frequencias.get(caractere), caractere))
    
    while len(nos) > 1:
        nos = sorted(nos, key=lambda x: x.frequencia)
        direita = nos[0]
        esquerda = nos[1]
    
        esquerda.codigo = 0
        direita.codigo = 1
    
        novo_no = Node(esquerda.frequencia + direita.frequencia, esquerda.caractere + direita.caractere, esquerda, direita)
    
        nos.remove(esquerda)
        nos.remove(direita)
        nos.append(novo_no)
            
    codigos = calcularCodigos(nos[0])
    print("\ncaracteres e seus codigos: ", codigos)
    saida_codificada = textoCodificado(dados, codigos)

    return saida_codificada, nos[0]  
    
 
def descomprimir(dados_codificados, huffman_arvore):
    arvore_head = huffman_arvore
    saida = []

    for x in dados_codificados:
        if x == '1':
            huffman_arvore = huffman_arvore.direita   
        elif x == '0':
            huffman_arvore = huffman_arvore.esquerda
        try:
            if huffman_arvore.esquerda.caractere == None and huffman_arvore.direita.caractere == None:
                pass
        except AttributeError:
            saida.append(huffman_arvore.caractere)
            huffman_arvore = arvore_head
        
    string = ''.join([str(item) for item in saida])
    return string        

if __name__=='__main__':

    texto = "CASA PAPEL HOTEL PASTEL"
    texto_codificado, arvore = comprimir(texto)
    print(f"\ntexto original: {texto}")
    print(f"Texto codificado: {texto_codificado}")
    print(f"Texto decodificado: {descomprimir(texto_codificado, arvore)}\n")