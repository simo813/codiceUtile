#id map da esami/2024-07-18-A
self.idMapGenes = {}
        for g in self.listGenes:
            identity = g.GeneID + g.Function
            self.idMapGenes[identity] = g

#esempio di creazione mappa in metodo da 2024-07-04-B
def passStates(self, year):
    listIdStates = self.DAO.getStatesOfYear(year)
    listStates = []
    for id in listIdStates:
        state = self.idMapStates[id]
        listStates.append(state)
    return listStates

#gestione grafo con particolare accesso agli archi  e uso di lambda functions da esami/2024-07-18-A
def handle_graph(self, e):
    self.view.txt_result1.clean()
    if self.view.dd_min_chValue is None or self.view.dd_max_chValue is None:
        self.view.txt_result1.controls.append(
            ft.Text(f"Seleziona i valori"))
    else:
        self.model.createGraph(int(self.view.dd_min_chValue), int(self.view.dd_max_chValue))
        graph = self.model.graph
        self.view.txt_result1.controls.append(
            ft.Text(f"Creato grafo con {graph.number_of_nodes()} nodi e {graph.number_of_edges()} archi"))
        listOfNodesAndTotalWeight = []
        for source in graph.nodes():
            sumEdges = 0
            sumEdgesWeight = 0
            for u, v, data in graph.out_edges(source, data=True):  # attenzine
                sumEdges += 1
                sumEdgesWeight += data.get('weight', 1)
            listOfNodesAndTotalWeight.append((source, sumEdges, sumEdgesWeight))
        sortedListOfNodesAndTotalWeight = sorted(listOfNodesAndTotalWeight, key=lambda x: x[1], reverse=True)
        for i in range(0, 5):
            self.view.txt_result1.controls.append(
                ft.Text(
                    f"{sortedListOfNodesAndTotalWeight[i][0].__str__()} | {sortedListOfNodesAndTotalWeight[i][1]} | {sortedListOfNodesAndTotalWeight[i][2]}"))

    self.view.update_page()

#gestione del grafo con componenti connesse e massima componente connessa da  2024-07-04-B

def handle_graph(self, e):
    self.view.txt_result1.clean()
    if self.view.ddYearValue is not None and self.view.ddStateValue is not None:
        self.model.createGraph(int(self.view.ddYearValue), self.view.ddStateValue)
        graph = self.model.graph
        listOfConnected = sorted(nx.connected_components(graph), key=len, reverse=True)
        largest_cc = max(nx.connected_components(graph), key=len)
        self.view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {graph.number_of_nodes()}\n"
                                                      f"Numero di archi: {graph.number_of_edges()}\n"
                                                      f"Il grafo ha {len(list(listOfConnected))} componenti connesse\n"
                                                      f"La componente connessa più grande è costituita da {len(largest_cc)} nodi:\n"))

        for node in list(largest_cc):
            self.view.txt_result1.controls.append(ft.Text(f"{node.__str__()}\n"))

        self.view.btn_path.disabled = False
    else:
        self.view.txt_result1.controls.append(ft.Text(f"Seleziona i valori della ricerca"))
    self.view.update_page()


#creazione di un grafo con self.graph.add_edge particolare da Esame-del-29-06-2022-Turno-A
def createGraph(self, canzoniN):
    self.idMapAlbum = {}
    self.listNodes = self.DAO.getNodes(canzoniN)
    self.graph = nx.DiGraph()
    self.graph.add_nodes_from(self.listNodes)
    for node in list(self.listNodes):
        self.idMapAlbum[node.AlbumId] = node

    for album1 in self.listNodes:
        for album2 in self.listNodes:
            difference = album2.ncanzoni - album1.ncanzoni
            if album1.ncanzoni < album2.ncanzoni and difference != 0:
                self.graph.add_edge(album1, album2, weight=difference)

#esempio di lista tuple ordinata da Esame-del-29-06-2022-Turno-A
listSuccessors = sorted(listSuccessors, key=lambda x: x[1], reverse = True)


#creazione di grafo con iterazione su connected_components da Esame-del-02-11-2022-appello-riservato
def handleCreaGrafo(self, e):
    if self.view.txtInMin.value is not None and self.view.txtInMax.value is not None and self.view.ddGenreValue is not None:
        try:
            tMin = int(self.view.txtInMin.value)
            tMax = int(self.view.txtInMax.value)
            genreId = int(self.view.ddGenreValue)
            genre = self.model.idMapGenres[genreId]
            if tMin >= genre.minD:
                self.view.txt_result.clean()
                self.model.createGraph(genreId, tMin, tMax)
                graph = self.model.graph
                self.view.txt_result.controls.append(ft.Text(
                    f"Grafo creato!\n"
                    f"# Vertici: {graph.number_of_nodes()}\n"
                    f"# Archi: {graph.number_of_edges()}\n"))
                listConnectedComp = nx.connected_components(graph)
                for connectedComp in listConnectedComp:
                    nPlaylist = 0
                    number = 0
                    for node in connectedComp:
                        nPlaylist = node.nPlaylist
                        number += 1
                    self.view.txt_result.controls.append(ft.Text(
                        f"Componente con {number} vertici, inseriti in {nPlaylist} playlist"))

            else:
                self.view.txt_result.clean()
                self.view.txt_result.controls.append(ft.Text(
                    f"Inserisci un valore di minimo più grande di {genre.minD}"))

        except ValueError:
            self.view.txt_result.clean()
            self.view.txt_result.controls.append(ft.Text(
                f"Inserisci un valore di minimo in formato secondi di tipo numerico"))
    else:
        self.view.txt_result.clean()
        self.view.txt_result.controls.append(ft.Text(
            f"Seleziona genere, tMin e tMax per creare un grafo"))

    self.view.update_page()

#aggiunta di archi con peso da Esame-del-30-06-2021-Pomeriggio
self.graph.add_weighted_edges_from(listEdges, weight='weight')
