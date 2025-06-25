
#da lab 12
def getOptPath(self, length):
    self.optPath = []
    self.optPathWeight = 0
    graph = self.graphMO

    for node in graph.nodes:
        self.recursion(
            node=node,
            partial=[node],
            partialWeight=0,
            level=0,
            length=length
        )

    return self.optPath, self.optPathWeight


def recursion(self, node, partial, partialWeight, level, length):
    graph = self.graphMO

    if level == length:
        if partial[-1] == partial[0]:  # ciclo chiuso
            if partialWeight > self.optPathWeight:
                self.optPathWeight = partialWeight
                self.optPath = list(partial)  # copia della lista
        return

    for successor in graph.neighbors(node):
        # Permetti di tornare al nodo iniziale solo alla fine
        if successor == partial[0] and level == length - 1:
            weight = graph.get_edge_data(node, successor).get('weight', 1)
            partial.append(successor)
            self.recursion(successor, partial, partialWeight + weight, level + 1, length)
            partial.pop()
        elif successor not in partial:
            weight = graph.get_edge_data(node, successor).get('weight', 1)
            partial.append(successor)
            self.recursion(successor, partial, partialWeight + weight, level + 1, length)
            partial.pop()

    def getOptPath(self, sourceId):
        self.optPath = []
        self.optPathPoints = 0
        source = self.idMapTeams[sourceId]

        self.recursion(
            source=source,
            partial=[source],
            partialPoints=0,
            weightPrec=0
        )
        print("\nENTRATO\n")
        print(self.optPath)
        print(self.optPathPoints)
        print("\nFINE\n")

        return self.optPath, self.optPathPoints


#ricorsione da baseballe
def recursion(self, source, partial, partialPoints, weightPrec):
    graph = self.graph

    if partialPoints > self.optPathPoints:
        print("\n---------------------------------")
        print(partialPoints)
        self.optPathPoints = partialPoints
        self.optPath = copy.deepcopy(partial)

    for successor in graph.neighbors(source):
        if successor not in partial:
            weightActual = graph.get_edge_data(source, successor).get('weight', 0)
            if weightPrec == 0:
                print("Prima iterazione")
                partial.append(successor)
                self.recursion(successor, partial, partialPoints + weightActual, weightActual)
                print("NUOVA RICORSIONE\n")
                partial.pop()
            elif weightActual < weightPrec:
                print("successore ha peso decrescente")
                partial.append(successor)
                self.recursion(successor, partial, partialPoints + weightActual, weightActual)
                print("NUOVA RICORSIONE\n")
                partial.pop()

#ricorsione con gradi dei nodi e grafo direzionato da Esame-24-01-2024-Turno-unico
def getOptPath(self):
    self.optPath = []
    graph = self.graph

    for node in graph.nodes:
        print("Il nodo esaminato non ha archi entranti\n")
        if graph.in_degree(node) == 0:
            self.recursion(
                source=node,
                partial=[node],
            )
        print("\nENTRATO\n")
    print(self.optPath)
    print("\nFINE\n")

    return self.optPath

def recursion(self, source, partial):
    graph = self.graph

    if graph.out_degree(source) == 0:
        print("Il nodo esaminato non ha archi uscenti\n")
        if len(partial) > len(self.optPath):
            print("\n---------------------------------")
            print(f"La lunghezza massima ora è {len(partial)}")
            self.optPath = copy.deepcopy(partial)  # copia della lista

    for source, successor in graph.out_edges(source):
        if successor not in partial:
            print("successore non in parziale")
            partial.append(successor)
            self.recursion(successor, partial)
            print("NUOVA RICORSIONE\n")
            partial.pop()