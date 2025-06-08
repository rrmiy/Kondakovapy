# Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив символы третей строки их числовыми кодами

with open('filee.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print('Содержимое:')
print(text)

probels = text.count(' ') + text.count('\n')
print('Пробелы:', probels)

stroki = text.split('\n')
if len(stroki) > 2:
    tretya = stroki[2]
    new_tretya = []
    for i in range(len(tretya)):
        new_tretya.append(str(ord(tretya[i]))) #код символов
stroki[2] = ' '.join(new_tretya)

with open('stix.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(stroki))
print('Результат в файле stix.txt')
