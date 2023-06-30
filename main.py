from util import bfs_por_id_partida, dfs_por_id_partida
from util import buscar_caminho_bfs, buscar_caminho_dfs,obter_alcancavel,obter_inalcancavel, obter_alcancaveis_por_id_partida, obter_grau_por_id_vertice, obter_graus_por_id, obter_inalcancaveis_por_id_partida, verificar_completos, verificar_desconexos, verificar_multigrafos, verificar_pseudografos
from grafo import carregar_grafos

def processar_comando(comando):
    comando = comando.split(' ')
    if comando[0] == 'grafos':
        if comando[1] == 'carregar':
            carregar_grafos(comando[2])
        elif comando[1] == 'multigrafos':
            verificar_multigrafos()
        elif comando[1] == 'pseudografos':
            verificar_pseudografos()
        elif comando[1] == 'desconexos':
            verificar_desconexos()
        elif comando[1] == 'completos':
            verificar_completos()
        elif comando[1] == 'graus':
            if comando[2] == 'id':
                id = int(comando[3])
                obter_graus_por_id(id)
        elif comando[1] == 'grau':
            id = int(comando[2].split('=')[1])
            vertice = comando[3].split('=')[1]
            obter_grau_por_id_vertice(id, vertice)
        
    subcomando = comando[1]
    switch = {
        'carregar': lambda: carregar_grafos(comando[2]),
        'multigrafos': verificar_multigrafos,
        'pseudografos': verificar_pseudografos,
        'desconexos': verificar_desconexos,
        'completos': verificar_completos,
        'graus': lambda: obter_graus_por_id(int(comando[3])) if comando[2] == 'id' else None,
        'grau': lambda: obter_grau_por_id_vertice(int(comando[2].split('=')[1]), comando[3].split('=')[1]),
       'alcancaveis': lambda: obter_alcancavel(comando[2].split('=')[1]) 
                 if len(comando) == 3 
                 else 
                    obter_alcancaveis_por_id_partida(int(comando[2].split('=')[1]), comando[3].split('=')[1]),
        'inalcancaveis': lambda: obter_inalcancavel(comando[2].split('=')[1]) 
                 if len(comando) == 3 
                 else obter_inalcancaveis_por_id_partida(int(comando[2].split('=')[1]), comando[3].split('=')[1]),
        'bfs': lambda: buscar_caminho_bfs(comando[2].split('=')[1], comando[3].split('=')[1]) 
                 if len(comando) == 4 
                 else bfs_por_id_partida(int(comando[2].split('=')[1]), comando[3].split('=')[1], comando[4].split('=')[1]),
        'dfs': lambda: buscar_caminho_dfs(comando[2].split('=')[1], comando[3].split('=')[1]) 
                 if len(comando) == 4 
                 else dfs_por_id_partida(int(comando[2].split('=')[1]), comando[3].split('=')[1], comando[4].split('=')[1]),
        'sair': lambda: print("Encerrando o programa...")
    }
    
    func = switch.get(subcomando)
    if func:
        func()
    else:
        print("Comando inválido.")
    else:
        print("Comando inválido.")
    return True

def main():
    continuar = True
    while continuar:
        comando = input("")
        continuar = processar_comando(comando)

if __name__ == '__main__':
    main()