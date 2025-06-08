#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:
#Количество элементов:
#Индекс первого минимального элемента:
#Умножаем все элементы на минимальный элемент:

with open('input.txt', 'w', encoding='utf-8') as file:
    file.write('3 -5 2 8 -1 4')

with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.read().split()
    numbers = list(map(int, data))

count = len(numbers)
min_zn = min(numbers)
first_min_index = numbers.index(min_zn)
result_numbers = [num * min_zn for num in numbers]

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(f'Исходные данные: {', '.join(data)}\n')
    file.write(f'Количество элеметов: {count}\n')
    file.write(f'Индекс первого мин значения: {first_min_index}\n')
    file.write(f'Умножаем все элементы на мин элемент: {', '.join(map(str, result_numbers))}\n')