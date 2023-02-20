import random
import time

def random_number_1_to_5():
    random.seed(time.time())  # inicializa la semilla de random con la hora actual
    return random.randint(1, 5)  # devuelve un número entero aleatorio entre 1 y 5

def random_number_1_to_7():
    num1 = random_number_1_to_5() -1
    num2 = random_number_1_to_5() -1
    result = (num1 + num2) % 7 +1
    return result

print(random_number_1_to_7())

