import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        range_choice = random.sample(range(min, max), quantity)#Генерує послідовність чисел у вказаному діапазоні без повторень
        sorted_choice = sorted(range_choice)#Сортує числа у зростаючому порядку
        return sorted_choice #Повертає результат 
    elif min <= 0 and max >= 1001:
        return list()#В разі некоректності генерує пустий список
    


print(get_numbers_ticket(1, 1000, 6))
