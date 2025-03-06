
import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

# Inicializar el intento del usuario
intento = None

# Usar un bucle while para que el usuario siga intentando
while intento != numero_aleatorio:
    # Pedir al usuario que ingrese su intento
    intento = int(input("Adivina el número entre 1 y 100: "))
    
    # Dar pistas sobre si el número es más alto o más bajo
    if intento < numero_aleatorio:
        print("Es más alto, intenta de nuevo.")
    elif intento > numero_aleatorio:
        print("Es más bajo, intenta de nuevo.")

# Cuando el usuario adivine el número
print(f"¡Felicidades! Adivinaste el número {numero_aleatorio}.")
