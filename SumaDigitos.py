
# Pedir al usuario un número
numero = input("Introduce un número: ")

# Inicializar la variable que almacenará la suma
suma = 0

# Usar un bucle para recorrer cada dígito y sumarlo
for digito in numero:
    suma += int(digito)

# Mostrar el resultado
print(f"La suma de los dígitos de {numero} es {suma}.")