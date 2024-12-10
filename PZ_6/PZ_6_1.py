#Дан список A размера N. Вывести вначале его элементы с нечетными номерами в порядке возрастания номеров,
#а затем — элементы с четными номерами в порядке убывания номеров: A1, A3, А5, …, A6, A4, A2.
# Условный оператор не использовать.

# Исходный список
A = [10, 20, 30, 40, 50, 60, 70]
N = len(A)

# Создаем два списка для элементов с нечетными и четными индексами
odd_elements = A[0::2]   # Берем каждый элемент через один начиная с первого
even_elements = A[1::2][::-1]  # Берем каждый элемент через один начиная со второго и переворачиваем

# Объединяем результаты
result = odd_elements + even_elements
print(result)