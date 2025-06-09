#Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
#унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
#вычисления площади и периметра.

import math

class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type

class Krug(Shape):
    def __init__(self, color, radius):
        super().__init__(color, "Круг")
        self.radius = radius

    def ploshad(self):
        return  math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

krug = Krug('Красный', 5)

print(f"Форма: {krug.shape_type}, Цвет: {krug.color}, Радиус: {krug.radius}" )
print(f"Площадь: {krug.ploshad():.2f}")
print(f"Периметр: {krug.perimeter():.2f}")