
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


#ricorsione da baseball
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

#ricorsione con accesso particolare agli archi con funzione find bilancio annessa da Esame-del-29-06-2022-Turno-A
def getOptPath(self, partenza, destinazione, soglia):
    self.optPath = []
    self.optPathBilancio = 0
    bilancioPartenza = self.findBilancio(partenza)
    print(partenza.AlbumId)
    print(destinazione.AlbumId)

    self.recursion(
        node = partenza,
        destinazione = destinazione,
        soglia = soglia,
        partial=[partenza],
        bilancioPartenza = bilancioPartenza,
        optPathBilancioP=0

    )
    print(self.optPath)
    print(self.optPathBilancio)
    print("\nFINE\n")

    return self.optPath

def recursion(self, node, destinazione, soglia, partial, bilancioPartenza, optPathBilancioP):
    graph = self.graph

    if node.__eq__(destinazione):
        if optPathBilancioP > self.optPathBilancio:
            print("\n---------------------------------")
            print("aggiornamento self.optPathBilancio")
            print(optPathBilancioP)
            print(partial)
            self.optPathBilancio = optPathBilancioP
            self.optPath = copy.deepcopy(partial)

    for node, successor, data in graph.out_edges(node, data=True):
        if successor not in partial:
            weight = graph[node][successor]['weight']
            if weight > soglia:
                print("successore valido")
                bilancioSuccessor = self.findBilancio(successor)
                if bilancioSuccessor > bilancioPartenza:
                    partial.append(successor)
                    self.recursion(successor, destinazione, soglia, partial, bilancioPartenza, optPathBilancioP + 1)
                    print("NUOVA RICORSIONE con aggiornamento optPathBilancioP\n")
                    partial.pop()
                else:
                    partial.append(successor)
                    self.recursion(successor, destinazione, soglia, partial, bilancioPartenza, optPathBilancioP)
                    print("NUOVA RICORSIONE\n")
                    partial.pop()


def findBilancio(self, node):
    graph = self.graph
    weightOutEdge = 0
    weightInEdge = 0

    for u, v, data in graph.out_edges(node, data=True):
        weightOutEdge += data.get('weight', 1)

    for u, v, data in graph.in_edges(node, data=True):
        weightInEdge += data.get('weight', 1)

    bilancio = weightInEdge - weightOutEdge
    return bilancio



#esempio di ricorsione com connected_components da Esame-del-02-11-2022-appello-riservato
def getOptPath(self, dTot):
    self.optPath = []
    self.sumDuration = 0
    largest_cc = max(nx.connected_components(self.graph), key=len)

    for node in largest_cc:
        partial = [node]
        print("Inizio ricorsione")
        self.recursion(
            node=node,
            largest_cc=largest_cc,
            partial=partial,
            partialDuration=node.duration,
            dTot=dTot
        )
        partial.pop()
    print(self.sumDuration)
    print(self.optPath)
    print("\nFINE\n")

    return self.optPath

def recursion(self, node, largest_cc, partial, partialDuration, dTot):

    if len(partial) > len(self.optPath):
        print("\n---------------------------------")
        print("aggiornamento self.sumDuration")
        print(partial)
        self.sumDuration = partialDuration
        self.optPath = copy.deepcopy(partial)

    for node in largest_cc:
        durationN = node.duration
        if node not in partial and durationN + partialDuration <= (dTot * 60):
            print("node valido")
            partial.append(node)
            self.recursion(node, largest_cc, partial, durationN + partialDuration, dTot)
            print("NUOVA RICORSIONE")
            partial.pop()
        else:
            print("nodo non valido")
            return



#esempio di ricorsione con neighbor da Tema-d-esame-04-09-2020---IMDB
def getIncrementalPath(self, source):
    self.incrementalPath = []
    partial = [source]
    print("Inizio ricorsione")
    self.recursion(
        source= source,
        partial= partial,
        predWeight = 0
    )
    print(self.incrementalPath)
    print("\nFINE\n")

    return self.incrementalPath

def recursion(self, source, partial, predWeight):

    if len(partial) > len(self.incrementalPath):
        print("\n---------------------------------")
        print("aggiornamento self.incrementalPath")
        print(partial)
        self.incrementalPath = copy.deepcopy(partial)

    for neighbor in self.graph.neighbors(source):
        actualWeight = self.graph[source][neighbor]["weight"]
        if neighbor not in partial and actualWeight >= predWeight:
            print("node valido")
            partial.append(neighbor)
            self.recursion(neighbor, partial, actualWeight)
            print("NUOVA RICORSIONE")
            partial.pop()
        else:
            print("nodo non valido")
            return


#esempio di ricorsione con out_edges da Esame-del-30-06-2021-Mattino-
def getOptPath(self, soglia):
    self.optPath = []
    self.optPathLenght = 0

    for source in self.graph.nodes():
        partial = [source]
        self.recursion(
            source=source,
            partial=partial,
            partialLenght=0,
            soglia=soglia
        )
        print("\nENTRATO\n")
        partial.pop()
    print(self.optPath)
    print(self.optPathLenght)
    print("\nFINE\n")

    return self.optPath, self.optPathLenght

def recursion(self, source, partial, partialLenght, soglia):
    graph = self.graph

    if partialLenght > self.optPathLenght:
        print("\n---------------------------------")
        print(partialLenght)
        self.optPathLenght = partialLenght
        self.optPath = copy.deepcopy(partial)

    for source, successor, data in graph.out_edges(source, data=True):
        edgeLength = graph[source][successor]["weight"]
        if successor not in partial and edgeLength > soglia:
            print("vicino ammissibile")
            partial.append(successor)
            self.recursion(successor, partial, partialLenght + edgeLength, soglia)
            print("NUOVA RICORSIONE\n")
            partial.pop()