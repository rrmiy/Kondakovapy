#В двумерном списке найти минимальный элемент в предпоследнем столбце.

import random

matrix = [[random.randint(1, 10) for i in range(3)] for i in range(3)]

print("Исходная матрица: ")
for strok in matrix:
    print(strok)

# матрица не пустая и имеет хотя бы 2 столбца
if not matrix or len(matrix[0]) < 2:
    print("Матрица мала для предпоследнего столбца!!!")
else:
    # индекс предпоследнего столбца
    pre_last_stolb = len(matrix[0]) - 2

    # минимальный элемент в этом столбце
    min_element = min(stroka[pre_last_stolb] for stroka in matrix)

    print(f"Минимальный элемент в предпоследнем столбце: {min_element}")

    from functools import reduce





    def format_likes(names):
        # Матрица шаблонов для разных количеств лайков
        templates = [
            ["нет лайков"],
            ["лайк поставил {}", "{}"],
            ["лайк поставили {} и {}", "{}", "{}"],
            ["лайк поставили {}, {} и еще {}", "{}", "{}", "{}"]
        ]

        n = len(names)

        # Выбираем подходящий шаблон
        template_idx = min(n, 3)  # Ограничиваем индекс 3 для случаев 3+ лайков

        # Форматируем строку
        if n == 0:
            return templates[0][0]
        elif n == 1:
            return templates[1][0].format(names[0])
        elif n == 2:
            return templates[2][0].format(names[0], names[1])
        else:
            return templates[3][0].format(names[0], names[1], n - 2)


    # Функциональный подход для обработки списка тестовых случаев
    test_cases = [
        [],
        ["Alex"],
        ["Mark", "Jakob"],
        ["Mark", "Alex", "Don"],
        ["Alice", "Bob", "Charlie", "David"]
    ]

    # Применяем функцию format_likes ко всем тестовым случаям
    results = list(map(format_likes, test_cases))

    # Выводим результаты
    for case, result in zip(test_cases, results):
        print(f"{result}")
#{case}