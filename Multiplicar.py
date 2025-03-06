
# Pedir al usuario un número
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Mostrar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    