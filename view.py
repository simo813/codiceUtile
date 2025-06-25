#cambio elemento da dropdawn da iTunes
def on_ddAlbum_change(self, e):
    self.ddAlbumValue = self.ddAlbum.value
    self.update_page()

#reset dropdown da iTunes
def reset_dropdown_album(self):
    self.ddAlbum.value = None
    self.ddAlbum.options = []
    self.update_page()


#esempio di gestione grafo con try except value error, self.view.txt_result.controls.append da Esame-24-01-2024-Turno-unico
def handle_graph(self, e):
    self.view.txt_result.clean()
    if self.view.ddMethodValue is not None and self.view.ddYearValue is not None and self.view._txtInS is not None:
        try:
            method = int(self.view.ddMethodValue)
            year = int(self.view.ddYearValue)
            s = float(self.view._txtInS.value)
            self.model.createGraph(method, year, s)
            graph = self.model.graph
            self.view.txt_result.controls.append(
                ft.Text(f"Grafo creato\n"
                        f"Ci sono {graph.number_of_nodes()} vertici\n"
                        f"Ci sono {graph.number_of_edges()} archi\n"))
        except ValueError:
            self.view.txt_result.controls.append(ft.Text(f"Inserisci un float in s"))


    else:
        self.view.txt_result.controls.append(ft.Text(f"Inserisci i valori correttamente"))
    self.view.update_page()