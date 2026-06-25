from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Estados validos para las tareas
VALID_STATUSES = ['pending', 'in progress', 'completed']

TASK_FILE = 'tasks.json'

#Carga las tareas desde el archivo JSON
def load_tasks():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)

    with open(TASK_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


# Garda las tareas en el archivo JSON
def save_tasks(tasks):
    with open(TASK_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def validate_task(data, existing_tasks, check_id=True):
    errors = []

    # Validar ID
    if check_id:
        if 'id' not in data:
            errors.append('El campo "id" es obligatorio.')
        else:
            for t in existing_tasks:
                if t['id'] == data['id']:
                    errors.append('Ya existe una tarea con ese ID.')
                    break

    # Validar title
    if 'title' not in data or not data['title']:
        errors.append('El campo "title" es obligatorio.')

    # Validar description
    if 'description' not in data or not data['description']:
        errors.append('El campo "description" es obligatorio.')

    # Validar status
    if 'status' not in data or not data['status']:
        errors.append('El campo "status" es obligatorio.')
    elif data['status'] not in VALID_STATUSES:
        errors.append(f'El campo "status" debe ser uno de los siguientes: {", ".join(VALID_STATUSES)}.')

    return errors


# def validate_task(data, existing_task):
#     errors = []

#     # Validar ID
#     if 'id' not in data:
#         errors.append('El campo "id" es obligatorio.')
#     else:
#         # Verificar ID duplicado
#         for t in existing_task:
#             if t['id'] == data['id']:
#                 errors.append('Ya existe una tarea con ese ID.')
#                 break
    
#     # Validar titulo
#     if 'title' not in data or not data['title']:
#         errors.append('El campo "title" es obligatorio.')
    
#     # Validar descripcion
#     if 'description' not in data or not data['description']:
#         errors.append('El campo "description" es obligatorio.')
    
#     # Validar status
#     if 'status' not in data or not data['status']:
#         errors.append('El campo "status" es obligatorio.')
#     elif data['status'] not in VALID_STATUSES:
#         errors.append(f'El campo "status" debe ser uno de los siguientes: {", ".join(VALID_STATUSES)}.')
    
#     return errors


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()

    # Leer query parameters
    status = request.args.get('status')

    # Validar que el status sea valido si viene en el query
    if status:
        if status not in VALID_STATUSES:
            return jsonify({'error': f'El parámetro "status" debe ser uno de los siguientes: {", ".join(VALID_STATUSES)}.'}), 400
        
        # Filtrar solo si es valido
        tasks = [t for t in tasks if t.get('status') == status]
    
    # Si no hay tasks
    if not tasks:
        return jsonify({'message': 'No hay tareas con el status especificado.'}), 200

    return jsonify(tasks), 200


@app.route('/tasks', methods=['POST'])
def create_task():
    tasks = load_tasks()
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Se requiere un cuerpo JSON.'}), 400
    
    # Validar los datos
    errors = validate_task(data, tasks)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Crear la nueva tarea
    new_task = {
        'id': data['id'],
        'title': data['title'],
        'description': data['description'],
        'status': data['status']
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify({'message': 'Tarea creada exitosamente.', 'task': new_task}), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Se requiere un cuerpo JSON.'}), 400
    
    # Buscar la tarea por ID
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Tarea no encontrada.'}), 404
    
    # Validar los datos (sin verificar ID duplicado)
    errors = validate_task(data, tasks, check_id=False)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Actualizar
    task['title'] = data['title']
    task['description'] = data['description']
    task['status'] = data['status']

    save_tasks(tasks)

    return jsonify({'message': 'Tarea actualizada exitosamente.', 'task': task}), 200


# @app.route('/tasks/<int:task_id>', methods= ['PUT'])
# def update_task(task_id):
#     tasks = load_tasks()
#     data = request.get_json()

#     if not data:
#         return jsonify({'error': 'Se requiere un cuerpo JSON.'}), 400
    
#     # Buscar la tarea por ID
#     task = next((t for t in tasks if t['id'] == task_id), None)
#     if not task:
#         return jsonify({'error': 'Tarea no encontrada.'}), 404
    
#     # Validar los datos (sin verificar ID duplicado)
#     errors = []

#     if 'title' not in data or not data['title']:
#         errors.append('El campo "title" es obligatorio.')
    
#     if 'description' not in data or not data['description']:
#         errors.append('El campo "description" es obligatorio.')
    
#     if 'status' not in data or not data['status']:
#         errors.append('El campo "status" es obligatorio.')
#     elif data['status'] not in VALID_STATUSES:
#         errors.append(f'El campo "status" debe ser uno de los siguientes: {", ".join(VALID_STATUSES)}.')
    
#     if errors:
#         return jsonify({'errors': errors}), 400
    
#     # Actualizar la tarea
#     task['title'] = data['title']
#     task['description'] = data['description']
#     task['status'] = data['status']

#     save_tasks(tasks)

#     return jsonify({'message': 'Tarea actualizada exitosamente.', 'task': task}), 200


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()

    task = next((t for t in tasks if t['id'] == task_id), None)

    if not task:
        return jsonify({'error': 'Tarea no encontrada.'}), 404
    
    # Eliminar la tarea
    tasks.remove(task)

    # Guardar los cambios
    save_tasks(tasks)

    return jsonify({'message': 'Tarea eliminada exitosamente.'}), 200


@app.route("/")
def home():
    return jsonify({"message": "API de Ejercicio de Flask"})


if __name__ == "__main__":
    app.run(host="localhost", debug=True)