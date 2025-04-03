from datetime import datetime, timedelta

def get_days_from_today(date):
    try: #перевіряє коректність введених даних
       date_insert = "date" #Преретворює в рядок
       date_from = datetime.strptime(date, "%Y-%m-%d") #Перетворюємо в зручний формат
       today_date = datetime.now() #Отримуємо сьогоднішню дату
       days_difference = (today_date - date_from).days #Бере різницю між датами
       change_to_integer = int(days_difference) #Перетворює в ціле число
       return f"Різниця між датами складає {days_difference} днів" #Повертає результат
    except ValueError: #Перевіряє чи введена дата у правильному форматі
        return "Некоректний формат дати. Використовуйте YYYY-MM-DD."
    except TypeError:  #Перевіряє чи введена дата є рядком
        return "Некоректний тип даних. Використовуйте рядок."

#Викликликає функцію та виводе на екран резултат
print(get_days_from_today("2023-10-01")) 