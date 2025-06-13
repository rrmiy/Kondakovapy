#В соответствии с номером варианта перешла по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk

import tkinter as tk
from tkinter import ttk

# Основное окно
root = tk.Tk()
root.title("Registration Details")
root.geometry("800x520")
root.configure(bg='#336699')  #синий фон

# Шрифт и цвета
label_font = ("Times New Roman", 14)
entry_font = ("Times New Roman", 14)
label_fg = "white"
entry_bg = "white"

# Рамка вокруг формы
frame = tk.LabelFrame(root, text="Registration Details", font=("Times New Roman", 14), fg="white", bg='#336699', bd=3, highlightbackground='white', labelanchor='nw')
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)


# Университет
tk.Label(frame, text="University :", font=label_font, fg=label_fg, bg='#336699').place(x=120, y=30)
univ_entry = tk.Entry(frame, font=entry_font, bg=entry_bg, width=35)
univ_entry.place(x=230, y=30)



# Институт
tk.Label(frame, text="Institute :", font=label_font, fg=label_fg, bg='#336699').place(x=135, y=80)
inst_entry = tk.Entry(frame, font=entry_font, bg=entry_bg, width=35)
inst_entry.place(x=230, y=80)

# Branch (Combobox)
tk.Label(frame, text="Branch :", font=label_font, fg=label_fg, bg='#336699').place(x=140, y=130)
branch_cb = ttk.Combobox(frame, values=["- - select - -", "Computer Science", "Electrical", "Mechanical", "Civil", "Chemical"], state="readonly", width=23, font=entry_font)
branch_cb.current(0)
branch_cb.place(x=230, y=130)

# Degree (Combobox + Radiobuttons)
tk.Label(frame, text="Degree :", font=label_font, fg=label_fg, bg='#336699').place(x=140, y=180)
degree_cb = ttk.Combobox(frame, values=["- - select - -", "Bachelors", "Masters", "PhD"], state="readonly", width=15, font=entry_font)
degree_cb.current(0)
degree_cb.place(x=230, y=180)

degree_status = tk.StringVar(value="Pursuing")
rb_pursuing = tk.Radiobutton(frame, text="Pursuing", variable=degree_status, value="Pursuing", bg='#336699', fg=label_fg, font=label_font, selectcolor='grey', activebackground='#336699')
rb_completed = tk.Radiobutton(frame, text="Completed", variable=degree_status, value="Completed", bg='#336699', fg=label_fg, font=label_font, selectcolor='grey', activebackground='#336699')
rb_pursuing.place(x=400, y=180)
rb_completed.place(x=500, y=180)

# Average CPI (Spinbox) и Semester (Spinbox)
tk.Label(frame, text="Avarage CPI :", font=label_font, fg=label_fg, bg='#336699').place(x=95, y=230)
cpi_spin = tk.Spinbox(frame, from_=0, to=10, increment=0.01, width=5, font=entry_font)
cpi_spin.place(x=230, y=230)

tk.Label(frame, text="Upto", font=label_font, fg=label_fg, bg='#336699').place(x=300, y=230)
semester_spin = tk.Spinbox(frame, from_=1, to=12, width=5, font=entry_font)
semester_spin.place(x=345, y=230)

tk.Label(frame, text="Th Semester", font=label_font, fg=label_fg, bg='#336699').place(x=405, y=230)

# Experience (Spinbox)
tk.Label(frame, text="Experience :", font=label_font, fg=label_fg, bg='#336699').place(x=110, y=280)
exp_spin = tk.Spinbox(frame, from_=0, to=50, width=5, font=entry_font)
exp_spin.place(x=230, y=280)
tk.Label(frame, text="Years", font=label_font, fg=label_fg, bg='#336699').place(x=290, y=280)

# Website or Blog (Entry)
tk.Label(frame, text="Your Website Or Blog :", font=label_font, fg=label_fg, bg='#336699').place(x=25, y=330)
website_entry = tk.Entry(frame, font=entry_font, bg=entry_bg, width=35)
website_entry.insert(0, "http://")
website_entry.place(x=230, y=330)

# Кнопки Step 2 с зелёными стрелками
def on_step2():
    print("Step 2 clicked")

btn_prev = tk.Button(root, text="◀", bg="#669933", fg="white", font=("Times New Roman", 12, "bold"), width=2, command=lambda: print("Step 1 clicked"))
btn_prev.place(relx=0.39, rely=0.89)

btn_next = tk.Button(root, text="▶", bg="#669933", fg="white", font=("Times New Roman", 12, "bold"), width=2, command=on_step2)
btn_next.place(relx=0.52, rely=0.89)

step_label = tk.Label(root, text="Step 2", font=("Times New Roman", 14), fg="white", bg='#336699')
step_label.place(relx=0.44, rely=0.89)

root.mainloop()
