'''Ejercicio 5: '''

A = int(input("Introduzca el primer número: "))
B = int(input("Introduzaca el segundo número: "))
C = int(input("Introduzca el tercer número: "))
if A > B and A > C and B > C:
    print("El número más grande es:", A)
if B > A and B > C and A > C:
    print("El número más grande es:", B)
if C > A and C > B and B > A:
    print("El número más grande es:", C)
input()
