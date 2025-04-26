from random import randint
from time import sleep

def generate(value1, value2):
    return randint(value1, value2)

a = int(input('Введит число от:'))
b = int(input('Введит число до:'))

result = generate(a, b)

print(f'подбираем число в диапзоне от {a} до {b}...')
sleep(2)
print(f'Случайное число: {result}')
