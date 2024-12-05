#С помощью функций получить вертикальную и горизонтальную линии. Линия
#проводится многократной печатью символа. Заключить слово в рамку из
#полученных линий

def horizontal_line(length):
    #Функция для горизонтальной линии
    print('-' * length)

def vertical_line(word_length):
   #Функция для вертикальной линии
    print('|', ' ' * (word_length + 2), '|', sep='')

def word_in_frame(word):
    #Функция для заключения слова в рамку.
    word_length = len(word) #возвращает длину

    # Рисуем верхнюю линию рамки
    horizontal_line(word_length + 3)

    # Рисуем вертикальные линии с пробелами
    vertical_line(word_length)

    # Печатаем слово по центру
    print('|', word, '|')

    # Рисуем нижнюю линию рамки
    vertical_line(word_length)
    horizontal_line(word_length + 3)

# Пример
word_in_frame("Привет")