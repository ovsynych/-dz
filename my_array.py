class Array:
    def __init__(self):
        self.data = []
        self.size = 0

    def append(self, value):
        self.data.append(value)
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне массива")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне массива")
        self.data[index] = value

    def delit(self):
        if self.size == 0:
            raise IndexError("Массив пустой")
        self.size -= 1
        return self.data.pop()

    def razmer(self):
        return self.size

    def vivod(self):
        print(self.data)


arr = Array()

arr.append(10)
arr.append(20)
arr.append(30)

arr.vivod()

print(arr.get(1))

arr.set(1, 50)

arr.vivod()

arr.delit()

arr.vivod()

print("Размер:", arr.razmer())
