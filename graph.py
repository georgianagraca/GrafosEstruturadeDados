# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [ [] for _ in range(n)]

    def print(self):
        print("Número de Vértices: " + str(self.num_vertices))
        print("Matriz de adjacência:")
        for row in self.M:
            print(row)
        print("Lista de Adjacência:")
        for i, adj in enumerate(self.L):
            print(f"{i}: {adj}")
    
    def num_comp(self):
        pred = self.dfs()
        num = 0
        for v in range(self.num_vertices):
            if(pred[v] == -1):
                num += 1
        return num
    
    def dfs(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            if(visitados[v] == False):
                self.dfs_rec(v, visitados, pred)
        return pred
        
    def dfs_rec(self, v, visitados, pred):
        visitados[v] = True
        for u in self.L[v]:
            if(visitados[u] == False):
                pred[u] = v
                self.dfs_rec(u, visitados, pred)
    
    def dfs_iterative(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        stack = []
        
        for v in range(self.num_vertices):
            if not visitados[v]:
                stack.append(v)
                visitados[v] = True
                
                while stack:
                    current = stack.pop()
                    for u in reversed(self.L[current]):  # reversed to maintain same order as recursive
                        if not visitados[u]:
                            visitados[u] = True
                            pred[u] = current
                            stack.append(u)
        return pred
    
    def bfs(self, source):
        visitados = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        D = [-1 for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        visitados[source] = True
        D[source] = 0
        
        while(Q.empty() == False):
            v = Q.get()
            for u in self.L[v]:
                if(visitados[u] == False):
                    Q.put(u)
                    visitados[u] = True
                    D[u] = D[v] + 1
                    pred[u] = v
        
        return D, pred
    
    def bfs_path(self, s, t):
        _, pred = self.bfs(s)
        path = []
        current = t
        
        if pred[current] == -1 and s != t:
            print(f"Não há caminho entre os vértices {s} e {t}")
            return
        
        while current != -1:
            path.append(current)
            current = pred[current]
        
        path.reverse()
        
        if path[0] != s:
            print(f"Não há caminho entre os vértices {s} e {t}")
        else:
            print("Caminho encontrado:")
            print(" -> ".join(map(str, path)))