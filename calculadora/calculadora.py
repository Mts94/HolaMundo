n1 = input('Ingresa primero número: ')
n2 = input('Ingresa segundo número: ')

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de su suma es {suma}
el resultado de su resta es {resta}
el resultado de su multiplicación es {multiplicacion}
el resultado de su división es {division}
"""
print(mensaje)
