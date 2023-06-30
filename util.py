
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


