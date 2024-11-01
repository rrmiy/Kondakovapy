#Дано трехзначное число. Используя одну операцию
#деления нацело вывести сотни
number = int(input("введите число:"))

try:
  if number >= 100 and number <= 999: #проверка трехзнач
    first_digit = number // 100 #деление без остатка
    print(f"сотни: {first_digit}")
  else:
    raise ValueError("неправильное значение")
except ValueError as e:
  print(e)