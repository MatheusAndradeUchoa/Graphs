import json
class Grafo:
    def __init__(self, id, vertices, arestas):
        self.id = id
        self.vertices = vertices
        self.arestas = arestas

# Variável global para armazenar os grafos carregados
grafos = []

# Função para carregar grafos a partir de um arquivo JSON
def carregar_grafos(arquivo):
    global grafos
    with open(arquivo, 'r') as file:
        data = json.load(file)
        for grafo_data in data['graphs']:
            grafo = Grafo(grafo_data['id'], grafo_data['vertices'], grafo_data['edges'])
            grafos.append(grafo)
    print("Grafos carregados com sucesso.")

# Função para verificar se um grafo é multigrafo
def is_multigrafo(grafo):
    for aresta in grafo.arestas:
        if grafo.arestas.count(aresta) > 1:
            return True
    return False

# Função para verificar se um grafo é pseudografo
def is_pseudografo(grafo):
    contador = {}
    for aresta in grafo.arestas:
        tupla_aresta = tuple(aresta)
        if tupla_aresta in contador:
            contador[tupla_aresta] += 1
        else:
            contador[tupla_aresta] = 1
    
    for count in contador.values():
        if count > 2:
            return True
    
    for aresta in grafo.arestas:
        if aresta[0] == aresta[1]:
            return True
    
    return False




