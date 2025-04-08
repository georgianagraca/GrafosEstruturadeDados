# -*- coding: utf-8 -*-
from graph import Graph
import sys

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == n):
                break
            g.M[l][c] = int(i)
            if int(i) != 0:
                g.L[l].append(c)
            c += 1
        l += 1
    
    return g

def test_graph(file_name):
    print(f"\n[DEBUG] Iniciando testes com: {file_name}")
    print(f"\n=== Testando com arquivo {file_name} ===")
    g = load_from(file_name)

    # Definir se é grafo grande
    grafo_grande = "pcv50" in file_name or "pcv177" in file_name

    if not grafo_grande:
        g.print()
    else:
        print(f"Número de Vértices: {g.num_vertices}")
        print("(Matriz e lista de adjacência omitidas por serem muito grandes)")

    # Testando número de componentes
    n = g.num_comp()
    print("\nNúmero de Componentes: " + str(n))

    # Testando BFS
    print("\nTestando BFS a partir do vértice 0:")
    D, pred = g.bfs(0)
    print("Distâncias:", D[:10], "..." if grafo_grande else "")
    print("Predecessores:", pred[:10], "..." if grafo_grande else "")

    # Testando caminho BFS
    if grafo_grande:
        target = g.num_vertices - 1  # Último vértice
    else:
        target = 3
    print(f"\nTestando caminho BFS entre 0 e {target}:")
    g.bfs_path(0, target)

    # Testando DFS recursivo
    print("\nTestando DFS recursivo:")
    pred_rec = g.dfs()
    print("Predecessores (recursivo):", pred_rec[:10], "..." if grafo_grande else "")

    # Testando DFS iterativo
    print("\nTestando DFS iterativo:")
    pred_iter = g.dfs_iterative()
    print("Predecessores (iterativo):", pred_iter[:10], "..." if grafo_grande else "")

    # Verificando se os resultados são iguais
    print("\nDFS recursivo e iterativo produzem o mesmo resultado?", pred_rec == pred_iter)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for file_name in sys.argv[1:]:
            test_graph(file_name)
    else:
        # Testa os arquivos padrão se nenhum for fornecido
        test_files = ["pcv4.txt", "pcv10.txt", "pcv50.txt", "pcv177.txt"]
        for file_name in test_files:
            try:
                test_graph(file_name)
            except FileNotFoundError as e:
                print(f"\n[ERRO] Arquivo {file_name} não encontrado. Detalhes: {e}")