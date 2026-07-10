from database import (validate_connection, validate_and_create_schema, validate_and_create_tables)
from managers.user_manager import UserManager
from managers.car_manager import CarManager
from managers.address_manager import AddressManager

def setup_database():
    validate_connection()
    validate_and_create_schema()
    validate_and_create_tables()

def run_exercise():
    u = UserManager()
    c = CarManager()
    a = AddressManager()

    print('\nNew user')

    user = u.create_user(
        full_name="John Doe",
        email="l.dorantes@example.com",
        username="ldorantes",
        password="123456"
    )
    print(f"Created user: ID:{user.id}, Full Name:{user.full_name}")

    print('\nNew car')
    car = c.create_car(
        brand="Toyota",
        model="Corolla",
        manufacture_year=2020,
        user_id=user.id
    )
    print(f"Created car: ID:{car.id}, Brand:{car.brand}, Model:{car.model}, user_id:{car.user_id}")

    print('\nlink car to user')
    c.assign_car_to_user(car.id, user.id)
    print(f"Linked car ID:{car.id} to user ID:{user.id}")

    print('\nNew address')
    address = a.create_address(
        street="123 Main St",
        city="Austin",
        state="TX",
        zip_code="12345",
        user_id=user.id
    )
    print(f"Created address: ID:{address.id}, Street:{address.street}, City:{address.city}, user_id:{address.user_id}")


if __name__ == "__main__":
    setup_database()
    run_exercise()
    