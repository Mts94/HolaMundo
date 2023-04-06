#and, or ,not

#and : siempre que las condiciones retirnen true el operador logico devolvera True
#or :  siempre que auqnue sea una de las condiciones devuelva true ,el operador devolvera true
#not : el operador not niega el resultado de un aoperacion



gas = True
encendidio = False
edad = 18

if gas and encendidio:
    print('Puedes avanzar')
    
    
if gas or (encendidio and edad > 17):#puedes separar con parentecis para decidir que evaluar primero,sigue la misma logica que las matematicas
    print('Puedes avanzar eres mayor')


if  not gas or encendidio:
    print('Puedes avanzar')
    
    
    