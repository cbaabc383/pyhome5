# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def Deg(a, b):
    if b == 1:
        return a
    return Deg(a,b-1) * a

A = int(input('Enter A: '))
B = int(input('Enter B: '))
print(f"A^B = {Deg(A,B)}")
