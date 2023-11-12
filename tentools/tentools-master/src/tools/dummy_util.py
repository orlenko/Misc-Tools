import random


def some_dummy_calculation():
    answer = 42
    first_half = random.randint(-answer, answer)
    result = first_half
    while result < answer:
        result += 1
    return result
