from datetime import datetime

def get_days_from_today(date):
    try: #перевіряє коректність введених даних
       date_from = datetime.strptime(date, "%Y-%m-%d") #Перетворюємо в зручний формат
       today_date = datetime.now() #Отримуємо сьогоднішню дату
       days_difference = (today_date - date_from).days #Бере різницю між датами
       return int(days_difference) #Повертає результат та Перетворює в ціле число
    except ValueError: #Перевіряє чи введена дата у правильному форматі
        return "Некоректний формат дати. Використовуйте YYYY-MM-DD."
    except TypeError:  #Перевіряє чи введена дата є рядком
        return "Некоректний тип даних. Використовуйте рядок."



print(f"різниця днів складає: {get_days_from_today("2023-10-01")}") #Викликликає функцію та виводе на екран резултат
