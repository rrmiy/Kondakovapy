#Разработать программу с применением пакета tk. дано целое число. если оно является
# положительным, то добавить к нему 1;
# если отрицательным, вычесть из него 2; если нулевым, то просто заменить его на 10.
# вывести полученное число.


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Обработка числа")

tk.Label(root, text="Введите целое число:").pack()
entry = tk.Entry(root)
entry.pack()

process = lambda: (
    result.config(text=f"Результат: {(
        int(entry.get()) + 1 if int(entry.get()) > 0 else
        int(entry.get()) - 2 if int(entry.get()) < 0 else 10
    )}") if entry.get().lstrip('-').isdigit() else
    messagebox.showerror("Ошибка", "Введите целое число")
)

tk.Button(root, text="Обработать", command=process).pack()
result = tk.Label(root, text="Результат: ")
result.pack()

root.mainloop()