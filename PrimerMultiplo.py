
# Inicializamos el número en 101 (ya que buscamos el primero mayor que 100)
numero = 101

# Usamos un bucle while para encontrar el primer múltiplo de 7 mayor que 100
while numero % 7 != 0:
    numero += 1

# Mostrar el resultado
print(f"El primer número mayor que 100 que es múltiplo de 7 es {numero}.")
