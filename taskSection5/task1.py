"""
    1. Make a program that find and show the first five multiples of 3, considering number greater than 0.

    PT-BR

    1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.

"""

number = 1
count = 0

while count < 5:
    if number % 3 == 0:
        print(number)
        count += 1
    number += 1

