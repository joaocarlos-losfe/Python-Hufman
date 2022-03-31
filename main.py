codigos = {}

class No:
    def __init__(self, frequencia, caractere, esquerda=None, direita=None):
        self.frequencia = frequencia
        self.caractere = caractere
        self.esquerda = esquerda
        self.direita = direita
        self.codigo = ''

def contarFrequencias(texto):
    caracteres = {}
    for ch in texto:
        if caracteres.get(ch) == None:
            caracteres[ch] = 1
        else: 
            caracteres[ch] += 1     
    return caracteres

def capturarCodigoAscii(no, valor=''):
    novo_valor = valor + str(no.codigo)

    if(no.esquerda):
        capturarCodigoAscii(no.esquerda, novo_valor)
    if(no.direita):
        capturarCodigoAscii(no.direita, novo_valor)

    if(not no.esquerda and not no.direita):
        codigos[no.caractere] = novo_valor
         
    return codigos        

def textoCodificado(dados, codigos):
    texto_codificado = []
    for c in dados:
        texto_codificado.append(codigos[c])
        
    string = ''.join([str(item) for item in texto_codificado])    
    return string

def totalBits(texto, bits_texto_codificado):

    total_texto = len(texto) * 8
    total_bits_texto_comprimido = 0
    caracteres = bits_texto_codificado.keys()

    for ch in caracteres:
        count = texto.count(ch)
        total_bits_texto_comprimido += count * len(bits_texto_codificado[ch])

    print(f"Antes da compressão: {total_texto} bits")    
    print(f"Depois da compressão: {total_bits_texto_comprimido} bits")  

    print(f"ganho de {int((total_bits_texto_comprimido * 100) / total_texto) }%")

          
def comprimir(texto):
    caracteres_e_frequencias = contarFrequencias(texto)
    caracteres = caracteres_e_frequencias.keys()
    frequencias = caracteres_e_frequencias.values()

    print(f"\ncaracteres: {list(caracteres)}")
    print(f"frequencia: {list(frequencias)}")
    nos = []
    
    for caractere in caracteres:
        nos.append(No(caracteres_e_frequencias.get(caractere), caractere))
    
    while len(nos) > 1:
        nos = sorted(nos, key=lambda x: x.frequencia)
        direita = nos[0]
        esquerda = nos[1]
    
        esquerda.codigo = 0
        direita.codigo = 1
    
        novo_no = No(esquerda.frequencia + direita.frequencia, esquerda.caractere + direita.caractere, esquerda, direita)
    
        nos.remove(esquerda)
        nos.remove(direita)
        nos.append(novo_no)
            
    codigos = capturarCodigoAscii(nos[0])
    print("\ncaracteres e seus codigos: ", codigos)
    totalBits(texto, codigos)
    saida_codificada = textoCodificado(texto, codigos)
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

    texto = "CASA_PAPEL_HOTEL_PASTEL"
    texto_codificado, arvore = comprimir(texto)
    print(f"\ntexto original: {texto}")
    print(f"Texto codificado: {texto_codificado}")
    print(f"Texto decodificado: {descomprimir(texto_codificado, arvore)}\n")