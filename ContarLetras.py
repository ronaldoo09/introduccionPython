
# Pedir al usuario una palabra
palabra = input("Introduce una palabra: ")

# Contar las letras usando un bucle
contador = 0
for letra in palabra:
    contador += 1

# Mostrar el resultado
print(f"La palabra '{palabra}' tiene {contador} letras.")
