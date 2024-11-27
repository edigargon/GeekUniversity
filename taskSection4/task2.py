"""
    2. Make a program that reads a integer provided by the user.
    If this number is positive, calculate the square root of the number.
    If the number is negative, show a message saying that the number is invalid.

    PT-BR

    2. Faça um programa que leia um número inteiro fornecido pelo usuário.
    Se esse número for positivo, calcule a raiz quadrada do npumero e apresente-a.
    Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
from math import sqrt

num = int(input("Enter a number: "))

if num > 0:
    print(f"\nThe number is positive.")
    print(f"The square root of number {num} is {sqrt(num)}.\n")
else:
    print(f"The number {num} is invalid.\n")

print("\n\n*********************************************** PT - BR **********************************************************\n\n")

print(f"Digite um número: {num}")

if num > 0:
    print(f"O número é positivo")
    print(f"A raiz quadrada do númeroo {num} é {sqrt(num)}.\n")
else:
    print(f"O número {num} é invalido.\n")
