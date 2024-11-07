#даны три целых числа. найти количество положительных и количество
# отрицательных чисел в исходном наборе

def count_pos_neg(): #переменные для хранения
    pos_count = 0 #положительных
    neg_count = 0 #отрицательных

    for _ in range(3):
        try:
            num = int(input("Введите целое число: "))
            if num > 0:
                pos_count += 1
            elif num < 0:
                neg_count += 1
        except ValueError:  #Обработка ошибки
            print("Ошибка!")

    return pos_count, neg_count #возвращает кортеж двух значений

#вызываем функцию и выводим результат
pos, neg = count_pos_neg()
print(f"Положительных чисел: {pos}")
print(f"Отрицательных чисел: {neg}")