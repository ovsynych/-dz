class MyList:
    def __init__(self):
        self.data = []
        self.size = 0

    def append(self, value):
        self.data.append(value)
        self.size += 1

    def delit(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне списка")

        self.data.pop(index)
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне списка")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне списка")
        self.data[index] = value


    def razmer(self):
        return self.size

    def clear(self):
        self.data = []
        self.size = 0

    def vivod(self):
        print(self.data)

my_list = MyList()

my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list.vivod()

print("Элемент:", my_list.get(1))

my_list.set(1, 100)
my_list.vivod()

my_list.delit(0)
my_list.vivod()

print("Длина:", my_list.razmer())
