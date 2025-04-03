import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max or quantity > (max - min):
        return []
    range_choice = random.sample(range(min, max + 1), quantity)
    return sorted(range_choice)
    


print(get_numbers_ticket(0, 1000, 6))