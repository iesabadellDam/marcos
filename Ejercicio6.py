'''Ejercicio 6: '''

A = int(input("Introduzca el primer número: "))
B = int(input("Introduzaca el segundo número: "))
C = int(input("Introduzca el tercer número: "))

if A > B and A > C and B > C:
    print(A, B, C)
if B < A and B < C and A > C:
    print(A, C, B)
if C < A and C < B and B > A:
    print(B, A, C)
if A < B and A < C and B > C:
    print(B, C, A)
if A > B and A < C and B < C:
    print(C, A, B)
if A < B and A < C and B < C:
    print(C, B, A)
input()
