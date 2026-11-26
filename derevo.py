class Uzel:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Derevo:
    def __init__(self, values=()):
        self.root = None
        self._size = 0
        for value in values:
            self.dobavit(value)

    def __len__(self):
        return self._size

    def dobavit(self, value):
        new_uzel = Uzel(value)

        if self.root is None:
            self.root = new_uzel
        else:
            now = self.root

            while True:
                if value <= now.value:
                    if now.left is None:
                        now.left = new_uzel
                        break
                    now = now.left
                else:
                    if now.right is None:
                        now.right = new_uzel
                        break
                    now = now.right

        self._size += 1

    def poisk(self, value):
        now = self.root

        while now is not None:
            if value == now.value:
                return True

            elif value < now.value:
                now = now.left

            else:
                now = now.right

        return False
    
    def __contains__(self, value): #in и ищет элемент
        return self.poisk(value)
    
    def inorder(self):  # сначала все левое, потом родитель и правая ветка
        result = []

        def obhod(now):
            if now is None:
                return

            obhod(now.left)
            result.append(now.value)
            obhod(now.right)

        obhod(self.root)
        return result

    def preorder(self):  # сначала записываем элемент, потом его потомков
        result = []

        def obhod(now):
            if now is None:
                return

            result.append(now.value)
            obhod(now.left)
            obhod(now.right)

        obhod(self.root)
        return result

    def postorder(self):  # сначала потомки, начиная с левого, потом предки
        result = []

        def obhod(now):
            if now is None:
                return

            obhod(now.left)
            obhod(now.right)
            result.append(now.value)

        obhod(self.root)
        return result

    def udalit(self, value):
        roditel = None
        now = self.root

        while now is not None and now.value != value:
            roditel = now

            if value < now.value:
                now = now.left
            else:
                now = now.right

        if now is None:
            return False

        if now.left is not None and now.right is not None:
            zamena_roditel = now
            zamena = now.left

            while zamena.right is not None:
                zamena_roditel = zamena
                zamena = zamena.right

            now.value = zamena.value

            roditel = zamena_roditel
            now = zamena

        potomok = now.left if now.left is not None else now.right

        if roditel is None:
            self.root = potomok

        elif roditel.left is now:
            roditel.left = potomok

        else:
            roditel.right = potomok

        self._size -= 1
        return True
    
    def minimum(self):
        if self.root is None:
            raise ValueError("Дерево пустое")

        now = self.root

        while now.left is not None:
            now = now.left

        return now.value    
    
    def maximum(self):
        if self.root is None:
            raise ValueError("Дерево пустое")

        now = self.root

        while now.right is not None:
            now = now.right

        return now.value 
    

if __name__ == "__main__":
    tree = Derevo([12, 6, 17, 3, 7, 15, 31, 9])

    print("Исходное дерево:")
    print("По возрастанию:", tree.inorder())
    print("Прямой обход:", tree.preorder())
    print("Обратный обход:", tree.postorder())

    print("\nПроверка поиска:")
    print("Есть 9:", tree.poisk(9))
    print("Есть 20:", tree.poisk(20))
    print("Есть 7 через in:", 7 in tree)
    print("Есть 100 через in:", 100 in tree)

    print("\nПроверка размера:")
    print("Количество элементов:", len(tree))

    print("\nМинимум и максимум:")
    print("Минимальный элемент:", tree.minimum())
    print("Максимальный элемент:", tree.maximum())

    print("\nДобавление элемента:")
    tree.dobavit(8)
    print("После добавления 8:", tree.inorder())
    print("Количество элементов:", len(tree))

    print("\nУдаление элементов:")

    print("Удаление 3 (лист):", tree.udalit(3))
    print("После удаления 3:", tree.inorder())

    print("Удаление 15 (узел с одним потомком):", tree.udalit(15))
    print("После удаления 15:", tree.inorder())

    print("Удаление 12 (узел с двумя потомками):", tree.udalit(12))
    print("После удаления 12:", tree.inorder())

    print("Удаление 100 (несуществующий элемент):", tree.udalit(100))

    print("\nИтоговое дерево:")
    print("По возрастанию:", tree.inorder())
    print("Прямой обход:", tree.preorder())
    print("Обратный обход:", tree.postorder())
    print("Количество элементов:", len(tree))

    print("\nМинимум:", tree.minimum())
    print("Максимум:", tree.maximum())
