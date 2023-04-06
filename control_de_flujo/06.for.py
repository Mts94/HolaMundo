buscar = 10

for numero in range(5):  # range nos crea una secuencia de numeros que comenzara desde el 0 al 4
    print(numero)
    if numero == buscar:
        print('encontrado', buscar)
        break  # esta sentencia lo que hace es detener la ejecucuon del codigo
else:
        print('No encontre el numero buscado!')
        
        
cadena = 'Ultimate python'  
for char in cadena: 
    print(char)