from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

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

VALID_STATUSES = ['pending', 'in progress', 'completed']

def validate_task(data, existing_task):
    errors = []

    # Validar ID
    if 'id' not in data:
        errors.append('El campo "id" es obligatorio.')
    else:
        # Verificar ID duplicado
        for t in existing_task:
            if t['id'] == data['id']:
                errors.append('Ya existe una tarea con ese ID.')
                break
    
    # Validar titulo
    if 'title' not in data or not data['title']:
        errors.append('El campo "title" es obligatorio.')
    
    # Validar descripcion
    if 'description' not in data or not data['description']:
        errors.append('El campo "description" es obligatorio.')
    
    # Validar status
    if 'status' not in data or not data['status']:
        errors.append('El campo "status" es obligatorio.')
    elif data['status'] not in VALID_STATUSES:
        errors.append(f'El campo "status" debe ser uno de los siguientes: {", ".join(VALID_STATUSES)}.')
    
    return errors


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Obtiene todas las tareas
    """
    tasks = load_tasks()

    # Leer query parameters
    status = request.args.get('status')

    if status:
        tasks = [t for t in tasks if t.get('status') == status]

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


@app.route('/tasks/<int:task_id>', methods= ['PUT'])
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
    errors = []

    if 'title' not in data or not data['title']:
        errors.append('El campo "title" es obligatorio.')
    
    if 'description' not in data or not data['description']:
        errors.append('El campo "description" es obligatorio.')
    
    if 'status' not in data or not data['status']:
        errors.append('El campo "status" es obligatorio.')
    elif data['status'] not in VALID_STATUSES:
        errors.append(f'El campo "status" debe ser uno de los siguientes: {", ".join(VALID_STATUSES)}.')
    
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Actualizar la tarea
    task['title'] = data['title']
    task['description'] = data['description']
    task['status'] = data['status']

    save_tasks(tasks)

    return jsonify({'message': 'Tarea actualizada exitosamente.', 'task': task}), 200


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