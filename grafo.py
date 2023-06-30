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

