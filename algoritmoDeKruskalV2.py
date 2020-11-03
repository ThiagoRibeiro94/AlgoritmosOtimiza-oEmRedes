
matriz = [
    [000,240,210,340,280,200,345,120],
    [000,000,265,175,215,180,185,155],
    [000,000,000,260,115,350,435,195],
    [000,000,000,000,160,330,295,230],
    [000,000,000,000,000,360,400,170],
    [000,000,000,000,000,000,175,205],
    [000,000,000,000,000,000,000,305],
    [000,000,000,000,000,000,000,000]
]


#Crio as arestas 
rawlistaL = {}

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            continue
        else:
            if matriz[i][j] != 0:
                rawlistaL[(i,j)] = matriz[i][j]
                


# Criar Et, V, listaL, sb e t

t = 0 
Et = []
sb = {}
V = len(matriz)
for i in range(len(matriz)):
    sb[(i,)] = [i] 
# Não faço com lista porque é impossível colocar uma lista como chave de um dicionário

#Ordenar o dicionário
listaL = {}
for item in sorted(rawlistaL, key = rawlistaL.get):
    listaL[item] = rawlistaL[item]

print('===================================')
print('Antes da 1 iteração')
print('')
print(f't = {t}')
print('')
print(f'Et = {Et}')
print('')
print(f'Sb = {sb}')
print('sb = subárvore')
print('')
print('ListaL')

for chave,valor in listaL.items():
    print(f'{chave} = {valor}')
iterador = 0 
while V-1 > t and listaL != {}:

    print('')
    print(f'{iterador} Iteração')
    iterador += 1
    for aresta in listaL:
        par = aresta
        break
    
    print(f'A aresta {par} é excluída da lista L.')

    del listaL[par]

    for chavesDict in sb.keys():
        # Para ver em qual subárvore os vértices estão
        if par[0] in chavesDict:
            indexChave0 = chavesDict
        else:
            None

        if par[1] in chavesDict:
            indexChave1 = chavesDict
        else:
            None
    
    if indexChave0 != indexChave1:
        print('')
        print(f'Como os vértices {par[0]} e {par[1]} não estão na mesma subárvore, atualizamos os valores de Et,t e sb:')
        print("")
        print(f'O valor de t era igual a {t}')
        t += 1
        print(f'O valor de t passou a ser de {t}')
        print('')
        del sb[indexChave0]
        del sb[indexChave1]

        aresta = []
        aresta.append(par[0])
        aresta.append(par[1])
        print(f'Et era igual a: {Et}')
        Et.append(aresta)
        print(f'Et passou a ser  = {Et}')
        print(" ")
        listaSbChave0 = list(indexChave0)
        listaSbChave1 = list(indexChave1)
   
        listaSb = listaSbChave0 + listaSbChave1
        tuplaSb = tuple(listaSb)
        
        sb[tuplaSb] = listaSb
        print('Novo sb:')
        for i in sb.values():
            print(i)
        print('')

    else:
        print(f'Os vértices {par[0]} e {par[1]} estão na mesma subárvore, então os valores de t,Et e sb não devem ser atualizados.')
        None

print('')

pesoTotal = 0 
for arest in Et:
    pesoTotal += matriz[arest[0]][arest[1]]

print(" ")
print(f'O algoritmo terminou porque t > |V| -1, a soma dos pesos da árvore geradora mínima é de {pesoTotal}')



        
