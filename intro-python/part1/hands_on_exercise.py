"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(pi)
print(type(pi))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("i es menor que 50")
else:
    print("i es mayor que 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print("el color de la naranja es naranja")
elif picked_fruit == 'strawberry':
    print("el color de la fresa es rojo")
else:
    print("el color del platano es amarillo")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiplicacion(num1, num2):
    num3 = num1 * num2
    return(num3)

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiplicacion(12,96))

print("48 x 17 =",multiplicacion(48,17))

print("196523 x 87323 =",multiplicacion(196523,87323))
