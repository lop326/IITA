import json 
import os

while True:
    p=0
    print('''
MENU
    1. agregar una cuenta 
    2. buscar una cuenta
    3. salir
          ''')
    
    opcion = int(input("opcion: "))
    
    if opcion==1 or opcion==2:
        
        if os.path.exists("GESTOR.json"):
            if os.path.getsize('GESTOR.json') == 0:
                cuentas = []
                print("su gestor esta vacio\n")
            else:
                with open("GESTOR.json") as archivo:
                    cuentas = json.load(archivo)
        else:
            with open("GESTOR.json","w") as archivo:
                cuentas = []
                print("\nsu gestor esta vacio\n")
        

        if opcion ==1:
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
        
        else:
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
                
                
    elif opcion==3:
        print("FIN")
        break
    else:
        print("OPCION INVALIDA")