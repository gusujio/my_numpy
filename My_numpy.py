
class Array(list):
    """Сложение, когда аргумент слева"""
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Array([x + other for x in self])
        elif isinstance(other, (Array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Сложение векторов разной длины недопустимо')
            else:
                return Array([x + y for x, y in zip(self, other)])
        else:
            raise TypeError(f"Вектор нельзя сложить с {other}")
    """Сложение, когда аргумент справа"""
    def __radd__(self, other):
        return self + other

    """Вычитание, когда аргумент слева"""
    def __sub__(self, other):
        return self.sub(other, 'left')
    """Вычитание, когда аргумент справа"""
    def __rsub__(self, other):
        return self.sub(other, 'right')

    def sub(self, other, flag):
        if isinstance(other, (int, float)):
            if flag == 'left':
                return Array([x - other for x in self])
            elif flag == 'right':
                return Array([other - x for x in self])
        elif isinstance(other, (Array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Вычитание векторов разной длины недопустимо')
            else:
                return Array([x - y for x, y in zip(self, other)])
        else:
            raise TypeError(f"Вектор нельзя вычисть с {other}")

    """Умножение, когда аргумент слева"""
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Array([x * other for x in self])
        elif isinstance(other, (Array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Умножение векторов разной длины недопустимо')
            else:
                return Array([x * y for x, y in zip(self, other)])
        else:
            raise TypeError(f"Вектор нельзя умножить с {other}")
    """Умножение, когда аргумент справа"""
    def __rmul__(self, other):
        return self * other

    """Деление, когда аргумент слева"""
    def __truediv__(self, other):
        return self.truediv(other, 'left')
    """Деление, когда аргумент справа"""
    def __rtruediv__(self, other):
        return self.truediv(other, 'right')

    def truediv(self, other, flag):
        if isinstance(other, (int, float)):
            if flag == 'left':
                return Array([x / other for x in self])
            elif flag == 'right':
                return Array([other / x for x in self])
        elif isinstance(other, (Array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Деление векторов разной длины недопустимо')
            else:
                return Array([x / y for x, y in zip(self, other)])
        else:
            raise TypeError(f"Вектор нельзя разделить с {other}")
            
    """Добавление функционала слайсинга"""
    def __getitem__(self, item):
        if type(item) != tuple:
            item = super().__getitem__(item)
            if isinstance(item, (float, int)):
                return item
            return Array(item)
        else:
            if type(item[0]) == slice:
                return Array([i[item[1]] for i in self[item[0]]])
            else:
                while len(item) > 0:
                    if isinstance(self, (int, float)):
                        raise IndexError('Слишком много индексов для массива этого пространства')
                    self = self[item[0]]
                    item = item[1:]
                return self

    """Находит min число в Array"""
    def min(self):
        while not isinstance(self, (int, float)):
            self = min(self)
        return self
    """Находит max число в Array"""
    def max(self):
        while not isinstance(self, (int, float)):
            self = max(self)
        return self
    """Считает сумму всех чисел в Array"""
    def sum(self):
        sums = 0
        for i in self:
            if isinstance(i, (int, float)):
                sums += i
            else:
                sums += summ(i)
        return sums
    """Считает кол-во всех элементов в Array"""
    def count(self):
        counts = 0
        for i in self:
            if isinstance(i[0], (int, float)):
                counts += len(i)
            else:
                counts += count(i)
        return counts
    """Считает сумму и кол-во всех элементов в Array"""
    def sum_count(self):
        counts = 0
        sums = 0
        for i in self:
            if isinstance(i, (int, float)):
                counts += 1
                sums += i
            else:
                s, c = Array(i).sum_count()
                sums += s
                counts += c
                
        return sums, counts
    """Считает среднее значение элементов в Array"""
    def mean(self):
        s, c = self.sum_count()
        return s / c