def suma(num1,num2):
    return (f"{num1} + {num2} = {num1+num2}")
    
def resta(num1,num2):
    return (f"{num1} - {num2} = {num1-num2}")
    
def multiplicacion(num1,num2):
    return (f"{num1} * {num2} = {num1*num2}")
    
def division(num1,num2):
    
    if num2 == 0:
        print("la division por cero no existe")
    else:
        return(f"{num1} / {num2} = {num1/num2}")
    

while True:
    print('''
MENU CALCULADORA
    1. SUMA
    2. RESTA
    3. MULTIPLICACION
    4. DIVISION
    5. SALIR
      '''
)
    opcion = int(input("opcion: "))
    if opcion in (1,2,3,4):
        num1 = int(input("ingresa numero 1: "))
        num2 = int(input("ingresa numero 2: "))
        if opcion== 1:
            op = suma(num1,num2)
        elif opcion ==2:
            op = resta(num1,num2)
        elif opcion ==3:
            op = multiplicacion(num1,num2)
        else:
            op = division(num1,num2)
        print(op)
        with open("EJERCICIO_2\historial.txt","a") as archivo:
            archivo.write(op)
    elif opcion== 5:
        print("FIN")
   
        break
    else:
        print("opcion incorrecta")