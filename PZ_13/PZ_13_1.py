#. Для каждого столбца матрицы с четным номером найти сумму ее элементов


import random

matrix = [[random.randint(1, 10) for i in range(3)] for i in range(3)]

print("Исходная матрица: ")
for strok in matrix:
    print(strok)


even_stolb = filter(lambda stolb: stolb % 2 == 0, range(len(matrix[0])))

result = list(
    map(
        lambda stolb: (f"Столбец {stolb}", sum(strok[stolb] for strok in matrix)),
        even_stolb
    )
)

for stolb_info, total in result:
    print(f"{stolb_info}: {total}")

from functools import reduce


