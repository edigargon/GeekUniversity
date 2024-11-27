"""
    1. Make a program that receives two integer and show which one is the biggest

    PT-BR

    1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior
"""


num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))

if num1 > num2:
    print(f"Number {num1} is bigger")
elif num1 == num2:
    print(f"The numbers are the same ")
else:
    print(f"Number {num2} is bigger")