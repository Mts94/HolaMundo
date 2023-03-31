animal = '  ceRdo rosado  '
# Un metodo es una funcion que se encuentra dentro de un objeto
print(animal.upper())
# el metodo upper() toma un string y lo transforma en el mayusculas
# El metodo lower(),conviente todas las letras de un string en minusculas
print(animal.lower())
# El metodo capitalize() toma la primera letra de la cadena en mayuscula
print(animal.strip().capitalize())
# toma la primera letra de cada palbara de la cadena la convientre en mayucula
print(animal.title())
# remueve todos los espaciosen blanco que tiene a la derecha y la izquiera
print(animal.strip())
# en este caso se muestra como es posible encadenar los meotodos de los strings
print(animal.strip().capitalize())
# El meotodo lstrip() remueve los espacios en blanco a la izquierda de la cadena
print(animal.lstrip())
# El motodo rstrip() remueve los espacios en blanco aa la derecha de la cadena
print(animal.rstrip())
# busca en la cadena y devuelve la poscion en la que esta esa cadena
print(animal.find('ro'))
# en caso de no exostir devolvera -1
# si o si debe recibir dos parametros,busca la cedena del primer parametro
print(animal.replace("ceR", "hola"))
# y reemplaza por la cadena del segundo ,en caso de no encontrarla no hace nada
# Esta funcion busca y devuelve True en caso de que encuentre la cadena o False si no la encuentra
print('ceR' in animal)
# con el operador not ,devuelve true si la cadena NO ESTA dentro de la cadena
print('asd' not in animal)
