import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph=nx.Graph()
        self._idMap={}
        self._circuito=[]


    def getYears(self):
        return DAO.getYears()


    def buildGraph(self, annoMax, annoMin):
        self._graph.clear()
        self._circuito = DAO.getAllNodes()
        for i in self._circuito:
            self._idMap[i.circuitId] = i

        self._graph.add_nodes_from(self._circuito)

        allEdges = DAO.getAllEges(annoMax, annoMin, self._idMap)
        for e in allEdges:
            self._graph.add_edge(e.circuito1, e.circuito2, weight=e.peso)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def maxComponenteConnessa(self):
        max_conn = max(nx.connected_components(self._graph), key=len)
        lista_max_conn = []
        for u in max_conn:
            pesi = [d["weight"] for _, _, d in self._graph.edges(u, data=True)]
            peso_min = max(pesi) if pesi else 0
            lista_max_conn.append((u, peso_min))
        lista_max_conn.sort(key=lambda x: x[1], reverse=True)
        return lista_max_conn

    def getmaxComponenteConnessa(self):
        max_conn = max(nx.connected_components(self._graph), key=len)
        self.lista_max = []
        for u in max_conn:
            self.lista_max.append(u)
        return self.lista_max


