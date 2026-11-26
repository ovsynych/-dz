import json

class Graph:
    def __init__(self, napravlenie=False):
        self.vershini = []
        self.rebra = []
        self.napravlenie = napravlenie

    def dobavit_vershinu(self, vershina):
        if vershina not in self.vershini:
            self.vershini.append(vershina)

    def dobavit_rebro(self, vershina1, vershina2, ves=1):
        if vershina1 not in self.vershini or vershina2 not in self.vershini:
            raise ValueError("Одна или обе вершины не существуют")

        if not isinstance(ves, (int, float)) or isinstance(ves, bool):
            raise ValueError("Вес должен быть числом")

        if ves == 0:
            raise ValueError("Вес ребра не должен быть равен нулю")

        for v1, v2, w in self.rebra:
            if self.napravlenie:
                if v1 == vershina1 and v2 == vershina2:
                    raise ValueError("Такое ребро уже существует")
            else:
                if ((v1 == vershina1 and v2 == vershina2) or
                    (v1 == vershina2 and v2 == vershina1)):
                    raise ValueError("Такое ребро уже существует")

        self.rebra.append((vershina1, vershina2, ves))

    def matrica_smezhnosti(self):
        n = len(self.vershini)
        matrica = [[0] * n for _ in range(n)]

        for v1, v2, ves in self.rebra:
            i = self.vershini.index(v1)
            j = self.vershini.index(v2)

            matrica[i][j] = ves

            if not self.napravlenie:
                matrica[j][i] = ves

        return matrica

    def matrica_incidentnosti(self):
        n = len(self.vershini)
        m = len(self.rebra)

        matrica = [[0] * m for _ in range(n)]

        for j, (v1, v2, ves) in enumerate(self.rebra):
            i1 = self.vershini.index(v1)
            i2 = self.vershini.index(v2)

            if self.napravlenie:
                matrica[i1][j] = -1
                matrica[i2][j] = 1
            else:
                matrica[i1][j] = 1
                matrica[i2][j] = 1

                if i1 == i2:
                    matrica[i1][j] = 2

        return matrica

    def spisok_smezhnosti(self):
        spisok = {v: [] for v in self.vershini}

        for v1, v2, ves in self.rebra:
            spisok[v1].append((v2, ves))

            if not self.napravlenie and v1 != v2:
                spisok[v2].append((v1, ves))

        return spisok

    def spisok_reber(self):
        return self.rebra.copy()

    def save(self, filename):
        dannie = {
            "napravlenie": self.napravlenie,
            "vershini": self.vershini,
            "rebra": self.rebra
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(dannie, file, ensure_ascii=False, indent=4)

    @classmethod
    def load(cls, filename):
        with open(filename, "r", encoding="utf-8") as file:
            dannie = json.load(file)

        graph = cls(dannie["napravlenie"])

        for vershina in dannie["vershini"]:
            graph.dobavit_vershinu(vershina)

        for v1, v2, ves in dannie["rebra"]:
            graph.dobavit_rebro(v1, v2, ves)

        return graph


graph = Graph(napravlenie=False)


graph.dobavit_vershinu('A')
graph.dobavit_vershinu('B')
graph.dobavit_vershinu('C')
graph.dobavit_vershinu('D')


graph.dobavit_rebro('A', 'B', 5)
graph.dobavit_rebro('A', 'C', 10)
graph.dobavit_rebro('B', 'D', 3)
graph.dobavit_rebro('C', 'D', 7)




print("Вершины:")
print(graph.vershini)

print("\nРёбра:")
print(graph.spisok_reber())

print("\nМатрица смежности:")
for stroka in graph.matrica_smezhnosti():
    print(stroka)

print("\nМатрица инцидентности:")
for stroka in graph.matrica_incidentnosti():
    print(stroka)

print("\nСписок смежности:")
for vershina, sosedi in graph.spisok_smezhnosti().items():
    print(vershina, ":", sosedi)


graph.save("graph.json")

print("\nГраф сохранён в файл graph.json")



new_graph = Graph.load("graph.json")

print("\nПроверка загрузки:")
print("Вершины:", new_graph.vershini)
print("Рёбра:", new_graph.rebra)
print("Направленность:", new_graph.napravlenie)
  
