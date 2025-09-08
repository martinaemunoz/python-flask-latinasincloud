print("Ingresa un número entero positivo para ver su tabla de multiplicar:")
while True:
    try:
        num = int(input())
        if num < 0:
            print("El número debe ser positivo.")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
