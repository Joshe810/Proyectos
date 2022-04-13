# Ejercicio
# Calculadora basica de 2 numeros
import time
a = float(input("Numero 1: "))
b = float(input ("Numero 2: "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print()
print(" Calculadora ")
print("---------------")
time.sleep(1.0)
print("Suma: ",round(suma,2))
time.sleep(1.0)
print("Resta: ",round(resta,2))
time.sleep(1.0)
print("Multiplicacion: ",round(multiplicacion,2))
time.sleep(1.0)
print("Division: ",round(division,2))
print()