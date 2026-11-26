
class Deque:
    def __init__(self):
        self.data = []

    def appendleft(self, value):
        self.data.insert(0, value)

    def appendright(self, value):
        self.data.append(value)

    def delitleft(self):
        if self.if_pusto():
            raise IndexError("пусто")
        return self.data.pop(0)

    def delitright(self):
        if self.if_pusto():
            raise IndexError("пусто")
        return self.data.pop()

    def if_pusto(self):
        return len(self.data) == 0

    def razmer(self):
        return len(self.data)

    def perviy(self):
        if self.if_pusto():
            raise IndexError("пусто")
        return self.data[0]

    def posledniy(self):
        if self.if_pusto():
            raise IndexError("пусто")
        return self.data[-1]

    def vivod(self):
        print(self.data)


deque = Deque()

print("Проверка пустоты:")
print(deque.if_pusto()) 

print("Добавление справа:")
deque.appendright(10)
deque.appendright(20)
deque.appendright(30)
deque.vivod()  

print("Добавление слева:")
deque.appendleft(5)
deque.appendleft(1)
deque.vivod()  

print("Размер:")
print(deque.razmer())  

print("Первый элемент:")
print(deque.perviy())  

print("Последний элемент:")
print(deque.posledniy())  

print("Удаление слева:")
print(deque.delitleft())  
deque.vivod()  

print("Удаление справа:")
print(deque.delitright())  
deque.vivod()  

print("Размер после удаления:")
print(deque.razmer())  

print("Проверка границ:")
print(deque.perviy())  
print(deque.posledniy())  

print("Полная очистка через удаление:")
deque.delitleft()
deque.delitright()
deque.delitright()
deque.vivod()  

print("Проверка пустоты:")
print(deque.if_pusto())  # True

print("Проверка ошибок:")

try:
    deque.delitleft()
except IndexError:
    print("Удаление слева: ошибка обработана")

try:
    deque.delitright()
except IndexError:
    print("Удаление справа: ошибка обработана")

try:
    deque.perviy()
except IndexError:
    print("Получение первого элемента: ошибка обработана")

try:
    deque.posledniy()
except IndexError:
    print("Получение последнего элемента: ошибка обработана")
