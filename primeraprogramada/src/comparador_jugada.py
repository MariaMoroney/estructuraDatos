class Comparador_Jugada:
    def comparar(self, a, b):
        if a.fecha < b.fecha: return -1
        if a.fecha > b.fecha: return 1

        if a.trimestre < b.trimestre: return -1
        if a.trimestre > b.trimestre: return 1

        if a.yardas < b.yardas: return -1
        if a.yardas > b.yardas: return 1

        if a.tiempo < b.tiempo: return -1
        if a.tiempo > b.tiempo: return 1

        return 0