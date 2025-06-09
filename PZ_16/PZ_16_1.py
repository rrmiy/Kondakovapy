#Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
#Напишите метод, который выводит информацию о машине в формате "Марка:
#марка, Модель: модель, Год выпуска: год".

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")


car1 = Car("Toyota", "Corolla", 2022)
car1.info()

car2 = Car("Tesla", "Model S", 2023)
car2.info()

car3 = Car("Audu","RS6", "2013")
car3.info()

car4 = Car("Toyota", "Mark 2", "1980")
car4.info()

car5 = Car("Honda", "NSX", "1992")
car5.info()