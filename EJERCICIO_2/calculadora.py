def suma(num1,num2):
    print(f"{num1} + {num2} = {num1+num2}")
    
def resta(num1,num2):
    print(f"{num1} - {num2} = {num1-num2}")
    
def multiplicacion(num1,num2):
    print(f"{num1} * {num2} = {num1*num2}")
    
def division(num1,num2):
    
    if num2 == 0:
        print("la division por cero no existe")
    else:
        print(f"{num1} / {num2} = {num1/num2}")
    



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
            suma(num1,num2)
        elif opcion ==2:
            resta(num1,num2)
        elif opcion ==3:
            multiplicacion(num1,num2)
        else:
            division(num1,num2)
    
    elif opcion== 5:
        print("FIN")
        break
    else:
        print("opcion incorrecta")