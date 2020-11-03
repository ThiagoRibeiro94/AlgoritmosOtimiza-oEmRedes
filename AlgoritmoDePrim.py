
matriz = [
    [0,240,210,340,280,200,345,120],
    [0,0,265,175,215,180,185,155],
    [0,0,0,260,115,350,435,195],
    [0,0,0,0,160,330,295,230],
    [0,0,0,0,0,360,400,170],
    [0,0,0,0,0,0,175,205],
    [0,0,0,0,0,0,0,305],
    [0,0,0,0,0,0,0,0]
]


arestas = {}

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            continue
        else:
            if matriz[i][j] != 0:
                arestas[(i,j)] = matriz[i][j]
                arestas[(j,i)] = matriz[i][j]
            


vertices = [ i for i in range(len(matriz))]
V = [i for i in range(len(matriz))]
Vt = [vertices[0]]
i = 0 
Et = []
print('Antes da iteração 0')
print('')
print(f'Vt = {Vt}')
print('')
print(f'i = {i}')
print('')
print(f'Et = {Et}')

def AcharArestaDeMenorPeso(arestas,Vt,V):
    
    ArestaMenorValor = tuple()
    ArestaMenorValorPeso = float('inf')

    for chave,valor in arestas.items():

        if chave[1] in Vt and chave[0] not in Vt and chave[0] in V:

            if valor < ArestaMenorValorPeso:
                ArestaMenorValor = chave
                ArestaMenorValorPeso = valor
            else:
                None
        else:
            None

    return ArestaMenorValor,ArestaMenorValorPeso


pesoDaArvore = 0 
iterador = 0 
while i < len(V)-1:
    print(f'{iterador} iteração')
    iterador += 1
    peso = AcharArestaDeMenorPeso(arestas,Vt,V)[1]
    print('')
    MenorAresta = AcharArestaDeMenorPeso(arestas,Vt,V)[0]
    print(f'A menor aresta é {MenorAresta}')
    print('')
    print(f'O Vt antigo era: {Vt}')
    Vt.append(MenorAresta[0])
    print(f'Novo Vt é: {Vt}')
    print(f'O Et antigo era: {Et}')
    Et.append(MenorAresta)
    print(f'Novo Et é: {Et}')
    pesoDaArvore += peso
    print(f'i era igual a {i} e agora é igual a {i+1}')
    i += 1
    print('')

print(f'O algoritmo terminou porque t > |V| -1, a soma dos pesos da árvore geradora mínima é de {pesoDaArvore}')



