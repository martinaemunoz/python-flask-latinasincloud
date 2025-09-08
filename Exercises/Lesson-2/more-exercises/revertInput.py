print("Ingresa una palabra o frase para revertirla:")

while True:
    try:
        texto = input()
        if texto.strip() == "":
            print("La entrada no puede estar vacía. Intenta de nuevo:")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un texto válido.")

# revertido = texto[::-1] # slicing para revertir la cadena
revertido = ''
for char in texto:
    revertido = char + revertido
print(f"Texto revertido: {revertido}")