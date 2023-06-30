# Comandos da ferramenta "grafos"

A ferramenta "grafos" oferece funcionalidades relacionadas a grafos por meio de uma interface de linha de comando.

* As verificações para imprimir os grafos estão implementadas no arquivo util.py.

* As funcionalidades para definir e buscar vértices estão no arquivo grafo.py.

* O arquivo main.py executa os comandos da ferramenta.

## Comandos disponíveis

<span style="color:green"> ✔ = Finalizado </span>

> - ✔  `grafos carregar arquivo.json:` carrega os grafos contidos no arquivo `arquivo.json`.

> - ✔  `grafos multigrafos: `informa quais grafos do arquivo carregado são multigrafos.

> - ✔  `grafos pseudografos: ` informa quais grafos do arquivo carregado são pseudografos.

> - ✔  `grafos desconexos:` informa quais grafos do arquivo carregado são desconexos.

> - ✔  `grafos completos: ` informa quais grafos do arquivo carregado são completos.

> - ✔  `grafos graus id=1: ` informa os graus dos vértices do grafo de `id=1`.

> - ✔  `grafos grau id=1 vertice="A":`informa o grau do vértice `"A"` do grafo de `id=1`.

> - ✔  `grafos alcancaveis partida="A": `  informa quais vértices do grafo são alcançáveis a partir do vértice `"A"`.

> - ✔  ` grafos inalcancaveis partida="A": ` informa quais vértices do grafo são inalcançáveis a partir do vértice `"A"`.

> - ✔  `grafos bfs partida="A" chegada="B": ` informa o caminho partindo do vértice `"A"` até chegar no vértice `"B"` usando o algoritmo BFS.

> - ✔  `grafos dfs partida="A" chegada="B": ` informa o caminho partindo do vértice `"A"` até chegar no vértice `"B"` usando o algoritmo DFS.

> - ✔ `grafos sair:` finaliza a execução da ferramenta.


# extras:


> ✔ `grafos alcancaveis id=2 partida=A `

> ✔ `grafos inalcancaveis id=2 partida=A `

> ✔  `grafos alcancaveis id=2 partida=A chegada=C`

> ✔ `grafos alcancaveis id=2 partida=A chegada=C`





