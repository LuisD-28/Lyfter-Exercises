from database import SessionLocal
from models import Car, User

class CarManager:

    def create_car(self, brand, model, manufacture_year, user_id=None):
        with SessionLocal() as session:
            car = Car(
                brand=brand,
                model=model,
                manufacture_year=manufacture_year,
                user_id=user_id
            )
            session.add(car)
            session.commit()
            session.refresh(car)
            return car
        
    def update_car(self, car_id, **kwargs):
        with SessionLocal() as session:
            car = session.get(Car, car_id)
            if not car:
                return None
            
            for key, value in kwargs.items():
                if hasattr(car, key):
                    setattr(car, key, value)

            session.commit()
            session.refresh(car)
            return car
    
    def assign_car_to_user(self, car_id, user_id):
        with SessionLocal() as session:
            car = session.get(Car, car_id)
            user = session.get(User, user_id)
            if not car or not user:
                return None

            car.user_id = user_id
            session.commit()
            session.refresh(car)
            return car
        
    def get_all_cars(self):
        with SessionLocal() as session:
            cars = session.query(Car).all()
            return cars

    def get_car_by_id(self, car_id):
        with SessionLocal() as session:
            car = session.get(Car, car_id)
            return car