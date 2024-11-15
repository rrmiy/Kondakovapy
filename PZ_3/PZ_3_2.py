#даны три целых числа. найти количество положительных и количество
# отрицательных чисел в исходном наборе

def count_pos_neg(): #переменные для хранения
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        num3 = int(input("Введите третье число: "))

        positive_count = 0
        negative_count = 0

        for num in [num1, num2, num3]:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1

        print(f"Положительных чисел: {positive_count}, Отрицательных чисел: {negative_count}")

    except ValueError as e:
        print("Ошибка при вводе данных:", e)

count_pos_neg()
