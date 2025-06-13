import sqlite3
from datetime import datetime


class TradingFirmDB:
    def __init__(self, db_name='firm.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Создание таблицы продаж"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            sale_date TEXT NOT NULL,
                            product TEXT NOT NULL,
                            amount REAL NOT NULL,
                            discount REAL DEFAULT 0,
                            branch TEXT NOT NULL,
                            manager TEXT NOT NULL)''')
        self.conn.commit()

    def add_sales(self):
        """Добавление 10 тестовых позиций в БД"""
        test_data = [
            ('2023-01-15 10:00:00', 'Ноутбук', 75000, 5, 'Центральный', 'Иванов'),
            ('2023-01-15 11:30:00', 'Смартфон', 45000, 0, 'Северный', 'Петрова'),
            ('2023-01-16 09:15:00', 'Планшет', 32000, 3, 'Центральный', 'Сидоров'),
            ('2023-01-16 14:20:00', 'Монитор', 18000, 0, 'Южный', 'Иванов'),
            ('2023-01-17 16:45:00', 'Принтер', 22000, 10, 'Западный', 'Кузнецова'),
            ('2023-01-18 10:30:00', 'Сканер', 15000, 0, 'Центральный', 'Петрова'),
            ('2023-01-19 12:00:00', 'Наушники', 8000, 5, 'Восточный', 'Сидоров'),
            ('2023-01-20 15:20:00', 'Клавиатура', 3500, 0, 'Южный', 'Иванов'),
            ('2023-01-21 11:10:00', 'Мышь', 2500, 2, 'Северный', 'Кузнецова'),
            ('2023-01-22 13:45:00', 'Колонки', 12000, 7, 'Центральный', 'Петрова')
        ]

        self.cursor.executemany('''INSERT INTO sales 
                               (sale_date, product, amount, discount, branch, manager)
                               VALUES (?, ?, ?, ?, ?, ?)''', test_data)
        self.conn.commit()
        print("!!! Добавлено 10 тестовых записей о продажах !!!")

    def search_sales(self):
        """Поиск продаж по различным критериям"""
        print("\nВарианты поиска:")
        print("1. По товару")
        print("2. По филиалу")
        print("3. По менеджеру и сумме (> 10000)")

        choice = input("Выберите вариант поиска (1-3): ")

        if choice == '1':
            product = input("Введите название товара: ")
            self.cursor.execute("SELECT * FROM sales WHERE product = ?", (product,))
        elif choice == '2':
            branch = input("Введите название филиала: ")
            self.cursor.execute("SELECT * FROM sales WHERE branch = ?", (branch,))
        elif choice == '3':
            manager = input("Введите фамилию менеджера: ")
            self.cursor.execute("SELECT * FROM sales WHERE manager = ? AND amount > 10000", (manager,))
        else:
            print("!!! Неверный выбор !!!")
            return

        results = self.cursor.fetchall()
        self.display_results(results)

    def delete_sales(self):
        """Удаление продаж по различным критериям"""
        print("\nВарианты удаления:")
        print("1. По ID продажи")
        print("2. По товару и дате")
        print("3. По филиалу с суммой < 5000")

        choice = input("Выберите вариант удаления (1-3): ")

        if choice == '1':
            sale_id = input("Введите ID продажи: ")
            self.cursor.execute("DELETE FROM sales WHERE id = ?", (sale_id,))
        elif choice == '2':
            product = input("Введите название товара: ")
            date = input("Введите дату (ГГГГ-ММ-ДД): ")
            self.cursor.execute("DELETE FROM sales WHERE product = ? AND date(sale_date) = ?",
                                (product, date))
        elif choice == '3':
            branch = input("Введите название филиала: ")
            self.cursor.execute("DELETE FROM sales WHERE branch = ? AND amount < 5000", (branch,))
        else:
            print("!!! Неверный выбор !!!")
            return

        self.conn.commit()
        print(f"Удалено записей: {self.cursor.rowcount}")

    def update_sales(self):
        """Редактирование продаж"""
        print("\nВарианты редактирования:")
        print("1. Изменение суммы по ID")
        print("2. Изменение скидки для товара")
        print("3. Изменение менеджера для филиала")

        choice = input("Выберите вариант редактирования (1-3): ")

        if choice == '1':
            sale_id = input("Введите ID продажи: ")
            new_amount = input("Введите новую сумму: ")
            self.cursor.execute("UPDATE sales SET amount = ? WHERE id = ?",
                                (new_amount, sale_id))
        elif choice == '2':
            product = input("Введите название товара: ")
            new_discount = input("Введите новую скидку (%): ")
            self.cursor.execute("UPDATE sales SET discount = ? WHERE product = ?",
                                (new_discount, product))
        elif choice == '3':
            branch = input("Введите название филиала: ")
            new_manager = input("Введите нового менеджера: ")
            self.cursor.execute("UPDATE sales SET manager = ? WHERE branch = ?",
                                (new_manager, branch))
        else:
            print("!!! Неверный выбор !!!")
            return

        self.conn.commit()
        print(f"Обновлено записей: {self.cursor.rowcount}")

    def display_results(self, results):
        if not results:
            print("!!!!️ Записи не найдены !!!")
            return

        # Заголовки таблицы
        headers = ["ID", "Дата", "Товар", "Сумма", "Скидка", "Филиал", "Менеджер"]

        # Вычисляем ширину колонок
        col_widths = [len(header) for header in headers]
        for row in results:
            for i, col in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(col)))

        # Печатаем заголовки
        header_line = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        print(header_line)
        print("-" * len(header_line))

        # Печатаем данные
        for row in results:
            row_line = " | ".join(f"{str(col):<{w}}" for col, w in zip(row, col_widths))
            print(row_line)

    def show_all_sales(self):
        #Показать все продажи
        self.cursor.execute("SELECT * FROM sales")
        results = self.cursor.fetchall()
        self.display_results(results)

    def close(self):
        #Закрытие соединения с БД
        self.conn.close()


def main():
    db = TradingFirmDB()

    # Добавляем тестовые данные при первом запуске
    db.cursor.execute("SELECT COUNT(*) FROM sales")
    if db.cursor.fetchone()[0] == 0:
        db.add_sales()

    while True:
        print("\n=== УПРАВЛЕНИЕ ПРОДАЖАМИ ===")
        print("1. Показать все продажи")
        print("2. Поиск продаж")
        print("3. Добавить новые продажи")
        print("4. Редактировать продажи")
        print("5. Удалить продажи")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            db.show_all_sales()
        elif choice == '2':
            db.search_sales()
        elif choice == '3':
            db.add_sales()
        elif choice == '4':
            db.update_sales()
        elif choice == '5':
            db.delete_sales()
        elif choice == '0':
            db.close()
            print("Работа завершена)))")
            break
        else:
            print("!!! Неверный ввод, попробуйте еще раз !!!")


if __name__ == "__main__":
    main()