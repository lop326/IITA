from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Ejemplo de datos simulados
datos = {
    1: {'nombre': 'Usuario1', 'email': 'user1@example.com'},
    2: {'nombre': 'Usuario2', 'email': 'user2@example.com'}
}

@app.route('/update/<int:id>', methods=['GET', 'PUT'])
def update(id):
    if request.method == 'PUT':
        data = request.json
        nuevo_nombre = data.get('nombre')
        nuevo_email = data.get('email')

        # Actualizar los datos (en este caso en un diccionario)
        if id in datos:
            datos[id]['nombre'] = nuevo_nombre
            datos[id]['email'] = nuevo_email
            return jsonify({"message": "Datos actualizados con éxito"}), 200

        return jsonify({"message": "ID no encontrado"}), 404

    # Para manejar la solicitud GET y enviar los datos al formulario
    return render_template('update.html', datos=datos[id])

if __name__=='__main__':
    app.run()