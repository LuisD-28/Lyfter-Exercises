from flask import Flask, jsonify, request
from pg_manager import PgManager
from user_repo import UserRepository
from rental_repo import RentalRepository
from car_repo import CarRepository

app = Flask(__name__)

db = PgManager(
    dbname="postgres",
    user="postgres",
    password="280596",
    host="localhost"
)

user_repo = UserRepository(db)
rental_repo = RentalRepository(db)
car_repo = CarRepository(db)

# Create a new user
@app.route('/users', methods=['POST']) 
def create_user():
    data = request.json
    user_repo.create_user(
        data['full_name'],
        data['email'],
        data['username'],
        data['password'],
        data['birth_date']
    )
    return jsonify({"message": "User created successfully"}), 201

# Update user status
@app.route('/users/<int:user_id>/status', methods=['PUT'])
def update_user_status(user_id):
    data = request.json
    user_repo.update_user_status(
        user_id,
        data['account_status']
    )
    return jsonify({"message": "User status updated successfully"}), 200

# Flag user as blocked
@app.route('/users/<int:user_id>/block', methods=['PUT'])
def flag_user_as_blocked(user_id):
    user_repo.flag_user_as_blocked(user_id)
    return jsonify({"message": "User flagged as blocked successfully"}), 200

# Get users list with optional filters
@app.route('/users', methods=['GET'])
def get_users():
    filters = request.args.to_dict()
    users = user_repo.get_users(filters)
    return jsonify(users), 200

# Add a new car
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    car_repo.create_car(
        data['brand'],
        data['model'],
        data['year']
    )
    return jsonify({"message": "Car created successfully"}), 201

# Update car status
@app.route('/cars/<int:car_id>/status', methods=['PUT'])
def update_car_status(car_id):
    data = request.json
    car_repo.update_car_status(
        car_id,
        data['car_status']
    )
    return jsonify({"message": "Car status updated successfully"}), 200

# Get cars list with optional filters
@app.route('/cars', methods=['GET'])
def get_cars():
    filters = request.args.to_dict()
    cars = car_repo.get_cars(filters)
    return jsonify(cars), 200

# Create a new rental
@app.route('/rentals', methods=['POST'])
def create_rental():
    data = request.json
    rental_repo.create_rental(
        data['user_id'],
        data['car_id']
    )
    return jsonify({"message": "Rental created successfully"}), 201

# Complete a rental
@app.route('/rentals/<int:rental_id>/complete', methods=['PUT'])
def complete_rental(rental_id):
    rental_repo.complete_rental(rental_id)
    return jsonify({"message": "Rental completed successfully"}), 200

# Update rental status
@app.route('/rentals/<int:rental_id>/status', methods=['PUT'])
def update_rental_status(rental_id):
    data = request.json
    rental_repo.update_rental_status(
        rental_id,
        data['rental_status']
    )
    return jsonify({"message": "Rental status updated successfully"}), 200

# Get rentals list with optional filters
@app.route('/rentals', methods=['GET'])
def get_rentals():
    filters = request.args.to_dict()
    rentals = rental_repo.get_rentals(filters)
    return jsonify(rentals), 200

if __name__ == '__main__':
    app.run(host='localhost', debug=True)