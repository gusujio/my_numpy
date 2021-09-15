# %%pycodestyle
class Null(float):
    def __repr__(self):
        return 'Null'
    def __add__(self, other):
        return Null()
    def __radd__(self, other):
        return Null()
    def __sub__(self, other):
        return Null()
    def __rsub__(self, other):
        return Null()
    def __mul__(self, other):
        return Null()
    def __rmul__(self, other):
        return Null()
    def __truediv__(self, other):
        return Null()
    def __rtruediv__(self, other):
        return Null()
    def __eq__(self, other):
        return False
    def __ne__(self, other):
        return True
    def __lt__(self, other):
        return False
    def __le__(self, other):
        return False
    def __gt__(self, other):
        return False
    def __ge__(self, other):
        return False
    
# %%pycodestyle

class Array(list):
    
    def __repr__(self):
        return super().__repr__()

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
            if isinstance(item, (float, int, str)) or item == None :
                return item
            return Array(item)
        else:
            if type(item[0]) == slice:
                return Array([i[item[1]] for i in self[item[0]]])
            else:
                while len(item) > 0:
                    if isinstance(self, (int, float)) or item == None :
                        raise IndexError('Слишком много индексов для массива этого пространства')
                    self = self[item[0]]
                    item = item[1:]
                return self
    """Добавление функционала итерирования в цикле"""
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self):
            raise StopIteration
        letter = self[self.index]
        self.index += 1 
        return letter

    def __eq__(self, other):
        if isinstance(other, (list, Array, tuple)) and len(self) == len(other):
            mas = []
            for i, j in zip(self, other):
                mas += [i == j]
            return Array(mas)
        elif isinstance(other, (int, float, Null, str)):
            mas = []
            for i in self:
                mas += [i == other]
            return Array(mas)
        else:
            return super().__eq__(other)
                

    """Находит min число в Array"""
    def min(self):
        mins = float('inf')
        for i in self:
            if not isinstance(i, (int, float)):
                i = Array(i).min()
            if i < mins:
                mins = i
        return mins
    """Находит max число в Array"""
    def max(self):
        maxs = float('-inf')
        for i in self:
            if not isinstance(i, (int, float)):
                i = Array(i).max()
            if i > maxs:
                maxs = i
        return maxs
            
                
    """Считает сумму всех чисел в Array"""
    def sum(self):
        sums = 0
        for i in self:
            if isinstance(i, (int, float)):
                sums += i
            else:
                sums += Array(i).sum()
        return sums
    """Считает кол-во всех элементов в Array"""
    def count_el(self):
        counts = 0
        for i in self:
            if isinstance(i, (int, float)):
                counts += 1
            else:
                counts += Array(i).count_el()
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
    
    def std(self):
        return (((self - self.mean()) * (self - self.mean())).sum() / self.count_el() )** 0.5
    
    """в оригинальном np его нет, но что бы работал pandas нужен"""
    def dropna(self):
        mas = []
        for i in self:
            if not isinstance(i, Null) and i != None:
                mas += [i]
        return Array(mas)
    
    """округляет все числа в массиве"""
    def round(self, lens = 1):
        mas = []
        for i in range(len(self)):
            mas.append(round(self[i], lens))
        return mas