import psycopg2

#CONEXION DESDE PYTHON
try:
    connection = psycopg2.connect(
                                    user='postgres',
                                    password = 'contraseña',
                                    database = 'alumnos',
                                    host = 'localhost',
                                    port = '5432'
    )
    print("database connected successfully")
    
except:
    print("database not connect successfully")
    
# CREANDO TABLAS

cur = connection.cursor()

cur.execute('''CREATE TABLE datos (ID SERIAL PRIMARY KEY,NAME VARCHAR(50),DOMICILIO VARCHAR(60))''')

cur.execute('''CREATE TABLE notas (ID SERIAL PRIMARY KEY, nota1 INT,nota2 INT)''')

connection.commit()

print("table created successfully")

# INSERTANDO DATOS

cur.execute('''
            INSERT INTO datos (NAME,DOMICILIO) VALUES 
            ('alvaro','itunzago 1234'),
            ('jose','nicolas 1244'),
            ('maria','catamarca 342'),
            ('alberto','jujuy 234'),
            ('pedro','belgrano 220'),
            ('carolina','avellaneda 607'),
            ('juan','cordoba 325'),
            ('claudia','tucuman 234'),
            ('leonel','florida 233'),
            ('antonella','alberdi 231')
            ''')

cur.execute('''
            INSERT INTO notas (nota1,nota2) VALUES 
            (9,4),
            (5,6),
            (9,8),
            (8,8),
            (2,6),
            (10,7),
            (5,8),
            (9,4),
            (7,7),
            (3,7)
            ''')

connection.commit()


# SE CONSULTA LOS DATOS
cur.execute('SELECT * FROM datos')

rows = cur.fetchall()

for datos in rows:
    
    print (f'''
        id = {datos[0]} 
        nombre = {datos[1]}
        domicilio = {datos[2]}
           ''')

# SE MODIFICAN LOS DATOS

cur.execute('UPDATE notas set nota1 = 6 WHERE nota1 = 5')

connection.commit()

# SE MUESTRAN CAMBIOS
cur.execute('SELECT * FROM notas')

rows = cur.fetchall()

for datos in rows:
    
    print (f'''
        id = {datos[0]} 
        nota 1 = {datos[1]}
        nota 2 = {datos[2]}
           ''')
cur.close()
connection.close()

print("conexion cerrada")