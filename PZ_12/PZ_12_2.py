#Составить генератор (yield), который выводит из строки только цифры.

def extract_digits(text):
    for char in text:
        if char.isdigit():
            yield char

text = 'abc123dfe456' #исп генератор
digits = ''.join(extract_digits(text))
print(digits) #только цифры