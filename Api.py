from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para almacenar usuarios
usuarios = []

@app.route('/usuario', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route('/usuario', methods=['POST'])
def agregar_usuario():
    # Obtener datos del cuerpo de la solicitud
    datos = request.get_json()
    
    # Validar que los datos contengan 'Nombre', 'Edad' y 'Sexo'
    if 'Nombre' not in datos or 'Edad' not in datos or 'Sexo' not in datos:
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    # Agregar el nuevo usuario a la lista
    usuarios.append(datos)
    
    return jsonify(datos), 201

if __name__ == '__main__':
    app.run(debug=True)