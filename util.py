
from grafo import bfs, dfs, grafos, is_completo, is_desconexo, is_multigrafo, is_pseudografo, obter_alcancaveis, obter_grau, obter_graus, obter_inalcancaveis


def verificar_multigrafos():
    for grafo in grafos:
        if is_multigrafo(grafo):
            print(f"Grafo {grafo.id} é um multigrafo.")
            

def verificar_pseudografos():
    for grafo in grafos:
        if is_pseudografo(grafo):
            print(f"Grafo {grafo.id} é um pseudografo.")

def verificar_desconexos():
    for grafo in grafos:
        if is_desconexo(grafo):
            print(f"Grafo {grafo.id} é desconexo.")

def verificar_completos():
    for grafo in grafos:
        if is_completo(grafo):
            print(f"Grafo {grafo.id} é completo.")

def obter_graus_por_id(id):
    grafo = next((grafo for grafo in grafos if grafo.id == id), None)
    if grafo:
        graus = obter_graus(grafo)
        print(f"Graus dos vértices do grafo {id}:")
        for vertice, grau in graus.items():
            print(f"Vértice {vertice}: {grau}")
    else:
        print(f"Grafo de ID {id} não encontrado.")

def obter_grau_por_id_vertice(id, vertice):
    grafo = next((grafo for grafo in grafos if grafo.id == id), None)
    if grafo:
        grau = obter_grau(grafo, vertice)
        print(f"Grau do vértice {vertice} do grafo {id}: {grau}")
    else:
        print(f"Grafo de ID {id} não encontrado.")

def obter_alcancaveis_por_id_partida(id, partida):
    grafo = next((grafo for grafo in grafos if grafo.id == id), None)
    if grafo:
        alcancaveis = obter_alcancaveis(grafo, partida)
        print(f"Vértices alcançáveis a partir do vértice {partida} do grafo {grafo.id}:")
        print(alcancaveis)
    else:
        print(f"Grafo de ID {id} não encontrado.")

def obter_inalcancaveis_por_id_partida(id, partida):
    grafo = next((grafo for grafo in grafos if grafo.id == id), None)
    if grafo:
        inalcancaveis = obter_inalcancaveis(grafo, partida)
        print(f"Vértices inalcançáveis a partir do vértice {partida} do grafo {grafo.id}:")
        print(inalcancaveis)
    else:
        print(f"Grafo de ID {id} não encontrado.")

def buscar_caminho_bfs(partida, chegada):
    for grafo in grafos:
        caminho = bfs(grafo, partida, chegada)
        if caminho:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} (BFS):")
            print(caminho)
        else:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} não encontrado.")

def buscar_caminho_dfs(partida, chegada):
    for grafo in grafos:
        caminho = dfs(grafo, partida, chegada)
        if caminho:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} (DFS):")
            print(caminho)
        else:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} não encontrado.")
            
            
def bfs_por_id_partida(id, partida, chegada):
    grafo = next((grafo for grafo in grafos if grafo.id == id), None)
    if grafo:
        caminho = bfs(grafo, partida, chegada)
        if caminho:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} (BFS):")
            print(caminho)
        else:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} não encontrado.")
    else:
        print(f"Grafo de ID {id} não encontrado.")
        
        
def dfs_por_id_partida(id, partida, chegada):
    grafo = next((grafo for grafo in grafos if grafo.id == id), None)
    if grafo:
        caminho = dfs(grafo, partida, chegada)
        if caminho:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} (DFS):")
            print(caminho)
        else:
            print(f"Caminho entre o vértice {partida} e o vértice {chegada} do grafo {grafo.id} não encontrado.")
    else:
        print(f"Grafo de ID {id} não encontrado.")
        
        
        
def obter_alcancavel(partida):
    for grafo in grafos:
        alcancaveis = obter_alcancaveis(grafo, partida)
        print(f"Vértices alcançáveis a partir do vértice {partida} do grafo {grafo.id}:")
        print(alcancaveis)
        
def obter_inalcancavel(partida):
    for grafo in grafos:
        inalcancaveis = obter_inalcancaveis(grafo, partida)
        print(f"Vértices inalcançáveis a partir do vértice {partida} do grafo {grafo.id}:")
        print(inalcancaveis)
