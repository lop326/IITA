# EJERCICIO 3: CRUD

## EXPLICACION GENERAL
> El programa es un gestor de cuentas de plataforma, guardando un nombre, email, y contraseña.

## LIBRERIAS
Para poder ejecutar el programa se usaron dos librerias
- Para poder manejar los archivos json.
```python
import json
```

- Para poder interactuar con el sistema operativo.
```python
import os
```

## MENU
Se hizo un menu basico con 3 opciones donde se podran agregar y buscar las cuentas, y otra donde se saldra del programa.

```python
    print('''
MENU
    1. agregar una cuenta 
    2. buscar una cuenta
    3. salir
          ''')
```

## VERIFICACION DE EXISTENCIA Y DE CONTENIDO DE ARCHIVO

Una vez elegida la opcion, se hace una verificacion de la existencia del archivo.

Si este existe se verifica si esta vacio o no, asi creando una lista llamada cuenta. 
```python
if os.path.exists("GESTOR.json"):
    if os.path.getsize('GESTOR.json') == 0:
        cuentas = []
        print("su gestor esta vacio\n")
    else:
        with open("GESTOR.json") as archivo:
            cuentas = json.load(archivo)
```
Si no existe, entonces crea dicho archivo, creando de igual manera una lista vacia.
```python
else:
    with open("GESTOR.json","w") as archivo:
        cuentas = []
        print("\nsu gestor esta vacio\n")
```

## CARGA DE CUENTA
La carga de cuenta consiste en pedir los tres datos para posteriormente crear un diccionario. Despues se lo agrega en la lista **cuentas** que despues sera ingresada al archivo json.
```python
print("INGRESAR NOMBRE DE PLATAFORMA")
nombre = input("_ ")
print("INGRESAR EMAIL")
email = input("_ ")
print("INGRESAR CONTRASEÑA")
contraseña = input("_ ")
datos = {'plataforma':nombre, 'email':email,'contrasena':contraseña}
cuentas.append(datos)
            
with open("GESTOR.json","w") as archivo:
    json.dump(cuentas,archivo,indent=4)
```
## BUSQUEDA DE CUENTA
Para la busqueda de plataforma solo se pide el nombre de la plataforma, este mismo se busca en la lista cuentas. Una vez encontrada se mostrara los datos completos.

```python
if os.path.getsize('GESTOR.json')!=0:
    print("INGRESAR NOMBRE DE PLATAFORMA")
    nombre = input("_ ")
    for cuenta in cuentas:
        if cuenta.get('plataforma','') == nombre:
            p=1
            print(f'''
    CUENTA:
        pltaforma: {cuenta.get('plataforma')}
        email: {cuenta.get('email')}
        contraseña: {cuenta.get('contrasena')}
                        '''
                    )
    if p==0:
        print("\nLa plataforma no fue encontrada\n")
```
