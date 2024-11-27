"""
    3. Make a program that receive a integer and tell whether this number is even or odd.

    PT-BR

    3. Faça um programa que recebe um número inteiro e informe se este número é par ou impar.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")

print("\n\n*********************************************** PT - BR **********************************************************\n\n")

print(f"Digite um número: {num}")

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é impar.")