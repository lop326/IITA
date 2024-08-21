from flask import Flask, render_template,request 
import json
app = Flask('__name__')

@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/busqueda', methods=['GET'])
def busqueda():
    with open('CUENTAS/entretenimiento.json', encoding="utf-8") as f:
        data = json.load(f)
 
    if request.args:
        nombre = request.args.get('nombre')
        plataforma = request.args.get('plataforma')
        if nombre in data and plataforma in data[nombre]:
            usuario = data[nombre][plataforma]
            return render_template('busqueda.html', user=usuario, plataforma = plataforma, nombre=nombre)
        else:
            return render_template('busqueda.html')
            
    else:
        return render_template('busqueda.html')


@app.route('/gestor', methods=['GET','POST'])
def gestor():
    with open("CUENTAS/entretenimiento.json", encoding="UTF-8") as f:
        data = json.load(f)

    if request.method =='POST':
        nombre = request.form['nombre']
        plataforma = request.form['plataforma']
        
        if nombre in data:
            if plataforma in data[nombre]:
                return render_template('gestor.html', mensaje = 'cuenta ya existente')
            
            else:
                data[nombre][plataforma] = {
                    'email': request.form['correo'],
                    'password': request.form['password']
                }
                with open("CUENTAS/entretenimiento.json",'w', encoding="UTF-8") as f:
                    json.dump(data,f,indent=4)
                return render_template('gestor.html', mensaje = f'cuenta de {plataforma} se agrego correctamente')
        else:
            data[nombre] = {plataforma: {
                'email': request.form['correo'],
                'password': request.form['password']
            }}
            with open("CUENTAS/entretenimiento.json",'w', encoding="UTF-8") as f:
                json.dump(data,f,indent=4)
            return render_template('gestor.html', mensaje = f'cuenta de {plataforma} se agrego correctamente, Bienvenido {nombre}')
    else:
        return render_template('gestor.html', mensaje = '')
               
   
if __name__ == '__main__':
    app.run(debug=True)