#   Ejercicio 1
print("Hola Mundo!")
#   Ejercicio 2
nombre = input("Ingrese su nombre: ")
print("Hola "+nombre+"!")
#   Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#   Ejercicio 4
radio = input("Ingrese el radio del circulo: ")
radio = int(radio)
pi = 3.14
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"El area es {area} y el perimetro es {perimetro} ")
#   Ejercicio 5
segundos = int(input("Ingrese los segundos "))
horas = segundos / 3600
print (f"Equivale a {horas} horas. ")
#   Ejercicio 6
num = int(input("Ingrese un numero entero "))
print (f"La tabla de multiplicar de {num} es: ")
print (f"1x{num} = {num * 1}")
print (f"2x{num} = {num * 2}")
print (f"3x{num} = {num * 3}")
print (f"4x{num} = {num * 4}")
print (f"5x{num} = {num * 5}")
print (f"6x{num} = {num * 6}")
print (f"7x{num} = {num * 7}")
print (f"8x{num} = {num * 8}")
print (f"9x{num} = {num * 9}")
print (f"10x{num} = {num * 10}")
#   Ejercicio 7
num1 = int(input("Ingrese un numero entero que no sea 0: "))
num2 = int(input("Ingrese un segundo numero entero que no sea 0: "))
print (f"La suma de ambos numeros es: {num1 + num2} ")
print (f"La resta de ambos numeros es: {num1 - num2} ")
print (f"La multiplicacion de ambos numeros es: {num1 * num2} ")
print (f"La division de ambos numeros es: {num1 / num2} ")
#   Ejercicio 8
peso = float(input("Ingrese su peso en Kilogramos: "))
altura = float(input("Ingrese su altura en Metros: "))
imc = peso / (altura)**2
print (f"Su indice de masa corporal es {imc} ")
#   Ejercicio 9
tempC = int(input("Ingrese la temperatura en Celsius: "))
tempF = 9.5 * tempC + 32
print (f"El equivalente en grados Fahrenheit es {tempF}°F")
#   Ejercicio 10
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
prom = (num1 + num2 + num3) / 3
print (f"Su promedio es de: {prom} ")