
class array(list):
    """Сложение, когда аргумент слева"""
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return array([x + other for x in self])
        elif isinstance(other, (array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Сложение векторов разной длины недопустимо')
            else:
                return array([x + y for x, y in zip(self, other)])
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
                return array([x - other for x in self])
            elif flag == 'right':
                return array([other - x for x in self])
        elif isinstance(other, (array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Вычитание векторов разной длины недопустимо')
            else:
                return array([x - y for x, y in zip(self, other)])
        else:
            raise TypeError(f"Вектор нельзя вычисть с {other}")

    """Умножение, когда аргумент слева"""
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return array([x * other for x in self])
        elif isinstance(other, (array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Умножение векторов разной длины недопустимо')
            else:
                return array([x * y for x, y in zip(self, other)])
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
                return array([x / other for x in self])
            elif flag == 'right':
                return array([other / x for x in self])
        elif isinstance(other, (array, list, tuple)):
            if len(self) != len(other):
                raise ValueError('Деление векторов разной длины недопустимо')
            else:
                return array([x / y for x, y in zip(self, other)])
        else:
            raise TypeError(f"Вектор нельзя разделить с {other}")