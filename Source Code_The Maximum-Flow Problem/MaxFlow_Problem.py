from collections import defaultdict

class Graf:

    def __init__(self, graf):
        self.graf = graf 
        self.BARIS = len(graf)

    def BFS(self, s, t, parent):
        dikunjungi = [False]*(self.BARIS)
        antrian = []
        antrian.append(s)
        dikunjungi[s] = True
        while antrian:
            u = antrian.pop(0)
            for ind, val in enumerate(self.graf[u]):
                if not dikunjungi[ind] and val > 0:
                    antrian.append(ind)
                    dikunjungi[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def FordFulkerson(self, sumber, tujuan):
        parent = [-1]*(self.BARIS)
        max_aliran = 0
        while self.BFS(sumber, tujuan, parent):
            aliran_path = float("Inf")
            s = tujuan
            while(s != sumber):
                aliran_path = min(aliran_path, self.graf[parent[s]][s])
                s = parent[s]
            max_aliran += aliran_path
            v = tujuan
            while(v != sumber):
                u = parent[v]
                self.graf[u][v] -= aliran_path
                self.graf[v][u] += aliran_path
                v = parent[v]
        return max_aliran

graf = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graf(graf)

sumber = 0
tujuan = 5

print("\nAliran maksimum yang mungkin adalah %d\n" % g.FordFulkerson(sumber, tujuan))
