#Дана строка. Подсчитать количество содержащихся в ней прописных
# латинских букв.

def count_uppercase_latin_letters(text):
  """Подсчитывает количество прописных латинских букв в строке.

  Returns:
      Количество прописных латинских букв в строке.
  """
  count = 0
  for char in text:
      if 'a' <= char <= 'z':  # Проверяем, находится ли символ в диапазоне прописных латинских букв
          count += 1
  return count
text = "Hello, WORLD!"
count1 = count_uppercase_latin_letters(text)
print(f"Строка: '{text}', Количество прописных латинских букв: {count1}")