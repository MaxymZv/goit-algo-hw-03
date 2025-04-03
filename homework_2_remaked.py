import random

def get_numbers_ticket(min, max, quantity):# Оголошення функції
    if min < 1 or max > 1000 or min >= max or quantity > (max - min): # Перевірка коректності данних
        return [] #Повертає порожній список, при некоректному вводі
    range_choice = random.sample(range(min, max + 1), quantity) #Випадковий вибір чисел
    return sorted(range_choice) #Повертає відсортований список в порядку зростання
    


print(get_numbers_ticket(10, 15, 9)) # Виклклик функції з перевіркою умови і виводом результату
