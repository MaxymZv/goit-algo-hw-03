import random

def get_numbers_ticket(min, max, quantity):
    range_choice = random.sample(range(min, max), quantity)
    print(range_choice)


get_numbers_ticket(1, 49, 6)