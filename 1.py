from random import randint
from time import sleep

a = int(input('Введит число от:'))
b = int(input('Введит число до:'))

result = randint(a, b)

print(f'подбираем число в диапзоне от {a} до {b}...')
sleep(2)
print(f'Случайное число: {result}')
