"""
3. Make a program that receives three integer values and presents the sum of the squares of the values read.

PT-BR

3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""

num1 = int(input("Enter 1º Number: "))
num2 = int(input("Enter 2º Number: "))
num3 = int(input("Enter 3º Number: "))

square_num1 = num1 * num1
square_num2 = num2 * num2
square_num3 = num3 * num3

sum_num = square_num1 + square_num2 + square_num3

print(sum_num)