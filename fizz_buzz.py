# -*- coding: utf-8 -*-
"""Fizz_Buzz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E3FLFUlHU4UaNPlARVkjXCLWCr39XTv-
"""

a = int(input("Ingresa el número a recorrer: "))
b = int(input("El límite a recorrer: "))

for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)