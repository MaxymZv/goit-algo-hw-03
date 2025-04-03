from datetime import datetime, timedelta

def get_days_from_today(date):
    date_insert = "date" #Преретворює в рядок
    date_from = datetime.strptime(date, "%Y-%m-%d") #Перетворюємо в зручний формат
    today_date = datetime.now() #Отримуємо сьогоднішню дату
    days_difference = (today_date - date_from).days #Бере різницю між датами
    print(f"Різниця між датами складає {days_difference} днів") #Друкує результат
    

#Виклик функції
get_days_from_today("2023-10-01")