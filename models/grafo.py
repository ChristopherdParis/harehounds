class Grafo:
    def __init__(self):
        self.nodos = {
            1: (100, 100),
            2: (200, 100),
            3: (300, 100),
            4: (400, 100),
            5: (500, 100),
            6: (100, 200),
            7: (200, 200),
            8: (300, 200),
            9: (400, 200),
            10: (500, 200),
            11: (100, 300),
            12: (200, 300),
            13: (300, 300),
            14: (400, 300),
            15: (500, 300),
        }

        self.relaciones = [
            (2, 3), (2, 6), (2, 7), (2, 8),
            (3, 4), (3, 8),
            (4, 8), (4, 9), (4, 10),
            (6, 7), (6, 12),
            (7, 12), (7, 8),
            (8, 12), (8, 13), (8, 14), (8, 9),
            (9, 10), (9, 14),
            (10, 14),
            (12, 13),
            (13, 14)
        ]

        self.grafo = self.crear_grafo()

    def crear_grafo(self):
        grafo = {}
        for nodo1, nodo2 in self.relaciones:
            if nodo1 not in grafo:
                grafo[nodo1] = set()
            if nodo2 not in grafo:
                grafo[nodo2] = set()
            grafo[nodo1].add(nodo2)
            grafo[nodo2].add(nodo1)
        return grafo

    def estan_conectados(self, nodo1, nodo2):
        return nodo2 in self.grafo.get(nodo1, set())
