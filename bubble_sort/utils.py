import random


def generate_random_values(length, range_: tuple):
    lst = [random.randint(range_[0], range_[1]) for _ in range(length)]
    return lst
