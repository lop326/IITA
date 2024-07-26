# EJERCICIO DE CALCULADORA 
## EXPLICACION GENERAL
> Se hizo un programa de calculadora que tenga operaciones basica entre dos numeros y que esta misma guarde los resultados.
## FUNCIONES
Se creo 4 funciones de las operaciones mas comunes de una calculadora. Esta mismas reciben dos numeros como parametro y devuelve dicho resultado.

```python
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
```

### MENU 
Se creo un menu principal con 5 opciones, 4 de tales operaciones y una para terminar el programa.
```python
    print('''
MENU CALCULADORA
    1. SUMA
    2. RESTA
    3. MULTIPLICACION
    4. DIVISION
    5. SALIR
      '''
)
```
## LLAMANDO FUNCIONES
Despues de ingresar alguna de las opciones del menu, este mismo se evaluara si pertenece a una operacion, la funcion de salir de programa o si es incorrecta.
 
Luego, si esta en el rango del 1 al 4, se evaluara nuevamente asi llamando a la funcion correspondiente a tal operacion. Esta misma devolvera un String con el resultado y posteriormente se mostrara.

Aparte de mostrar el resulatado, se abrira un archivo .txt para guardar dicha operacion, asi usado como una forma de *historial de operaciones*.
```python
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
```