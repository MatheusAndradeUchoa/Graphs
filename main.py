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
        
        elif comando[1] == 'alcancaveis' and len(comando) == 3:
            partida = comando[2].split('=')[1]
            obter_alcancavel(partida)
            
        elif comando[1] == 'inalcancaveis' and len(comando) == 3:
            partida = comando[2].split('=')[1]
            obter_inalcancavel(partida)
        
        elif comando[1] == 'alcancaveis':
            id = int(comando[2].split('=')[1])
            partida = comando[3].split('=')[1]
            obter_alcancaveis_por_id_partida(id, partida)
        elif comando[1] == 'inalcancaveis':
            id = int(comando[2].split('=')[1])
            partida = comando[3].split('=')[1]
            obter_inalcancaveis_por_id_partida(id, partida)
        elif comando[1] == 'bfs' and len(comando) == 4:
            partida = comando[2].split('=')[1]
            chegada = comando[3].split('=')[1]
            buscar_caminho_bfs(partida, chegada)
        elif comando[1] == 'dfs' and len(comando) == 4:
            partida = comando[2].split('=')[1]
            chegada = comando[3].split('=')[1]
            buscar_caminho_dfs(partida, chegada)
        elif comando[1] == 'bfs':
            id = int(comando[2].split('=')[1])
            partida = comando[3].split('=')[1]
            chegada = comando[4].split('=')[1]
            bfs_por_id_partida(id, partida, chegada)

        elif comando[1] == 'dfs':
            id = int(comando[2].split('=')[1])
            partida = comando[3].split('=')[1]
            chegada = comando[4].split('=')[1]
            dfs_por_id_partida(id, partida, chegada)
        elif comando[1] == 'sair':
            print("Encerrando o programa...")
            return False
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