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
        full_name="Luis Dorantes",
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

    print('\nUpdate User Information')
    user = u.update_user(
        user.id,
        full_name="Luis F. Dorantes",
        email="l.dorantes_updated@example.com",
        username="ldorantes_updated",
    )
    print(f"Updated user: ID:{user.id}, Full Name:{user.full_name}, Email:{user.email}")

    #! 
    print('\nTrying to update id field which is not allowed')
    user = u.update_user(
        user.id,
        id=999,
        full_name="Luis F. Dorantes",
        email="l.dorantes_updated@example.com"
    )
    address = a.update_address(
        address.id,
        id=999,
        street="456 Elm St",
        city="Dallas",
        state="TX",
        zip_code="67890"
    )
    car = c.update_car(
        car.id,
        id=999,
        brand="Honda",
        model="Civic",
        manufacture_year=2022,
        user_id=user.id
    )

    
    print('\nTrying to access "car.user" and "user.addresses" outside the managed session, once the session is closed')
    try:
        print(f"{car.user}")
    except Exception as e:
        print(f"Error accessing car user: {e}")

    try:
        print(f"{user.addresses}")
    except Exception as e:
        print(f"Error accessing user addresses: {e}")


if __name__ == "__main__":
    setup_database()
    run_exercise()
    