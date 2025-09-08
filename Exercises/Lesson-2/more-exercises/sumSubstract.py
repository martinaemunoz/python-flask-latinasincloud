print("Ingresa dos números enteros: ")
num1 = int(input())
num2 = int(input())

print("Deseas sumar, restar, multiplicar o dividir? (s/r/m/d): ")
operacion = input().lower()
if operacion == 's':
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es {resultado}.")    
elif operacion == 'r':
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es {resultado}.")
elif operacion == 'm':
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es {resultado}.")
elif operacion == 'd':
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división de {num1} entre {num2} es {resultado}.")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida. Por favor elige s, r, m o d.")


