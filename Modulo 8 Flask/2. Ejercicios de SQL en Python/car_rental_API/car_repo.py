class CarRepository:
    def __init__(self, db):
        self.db = db

    def create_car(self, brand, model, year):# Car_status 'available' by default
        try:
            self.db.execute_query(
                "INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year) VALUES (%s, %s, %s)",
                (brand, model, year)
            )
            return True
        except Exception as e:
            print(f"Error creating car: {e}")
            return False
    
    def update_car_status(self, car_id, car_status):
        try:
            self.db.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status = %s WHERE id = %s",
                (car_status, car_id)
            )
            return True
        except Exception as e:
            print(f"Error updating car status: {e}")
            return False
    
    def get_cars(self, filters=None):
        try:
            query = "SELECT * FROM lyfter_car_rental.cars"
            params = []

            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f'{key} = %s')
                    params.append(value)
                query += " WHERE " + " AND ".join(conditions)
            
            results = self.db.execute_query(query, params if params else None)

            if not results:
                return []
            
            formatted_cars = [self._format_car(car) for car in results]
            return formatted_cars
        
        except Exception as e:
            print(f"Error retrieving cars: {e}")
            return False
    
    #  Format car data into a dictionary, encapsuling the logic for data representation 
    def _format_car(self, car_record):
        return {
            "id": car_record[0],
            "brand": car_record[1],
            "model": car_record[2],
            "manufacture_year": car_record[3],
            "car_status": car_record[4]
        }
