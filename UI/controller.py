import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleBuildGraph(self, e):
        year1 = self._view._ddYear1.value
        if year1 == "":
            self._view._txtGraphDetails.controls.clear()
            self._view._txtGraphDetails.controls.append(ft.Text("Per favore, inserire un valore di year1", color="red"))
            self._view.update_page()
            return
        try:
            year1Int = int(year1)
        except ValueError:
            self._view._txtGraphDetails.controls.clear()
            self._view._txtGraphDetails.controls.append(
                ft.Text("Per favore, inserire un valore intero di year1", color="red"))
            self._view.update_page()
            return

        year2 = self._view._ddYear2.value
        if year2 == "":
            self._view._txtGraphDetails.controls.clear()
            self._view._txtGraphDetails.controls.append(ft.Text("Per favore, inserire un valore di year2", color="red"))
            self._view.update_page()
            return
        try:
            year2Int = int(year2)
        except ValueError:
            self._view._txtGraphDetails.controls.clear()
            self._view._txtGraphDetails.controls.append(
                ft.Text("Per favore, inserire un valore intero di year2", color="red"))
            self._view.update_page()
            return
        self._model.buildGraph(year2Int, year1Int)
        n, archi = self._model.getGraphDetails()
        self._view._txtGraphDetails.controls.clear()
        self._view._txtGraphDetails.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txtGraphDetails.controls.append(ft.Text(f"Il grafo contiene {n} nodi e {archi} archi."))
        self._view.update_page()


    def handlePrintDetails(self, e):



        lista_max_conn = self._model.maxComponenteConnessa()
        self._view._txtGraphDetails.controls.clear()
        self._view._txtGraphDetails.controls.append(ft.Text("Stampa dettagli: "))
        for l in lista_max_conn:
            self._view._txtGraphDetails.controls.append(ft.Text(f'{l[0]} -- {l[1]}'))
        self._view.update_page()

    def handleCercaDreamChampionship(self, e):
        pass

    def fillYears(self):
        years=self._model.getYears()
        for y in years:
            self._view._ddYear1.options.append(ft.dropdown.Option(y["year"]))
            self._view._ddYear2.options.append(ft.dropdown.Option(y["year"]))
        self._view.update_page()



