class RentalRepository:
    def __init__(self, db):
        self.db = db

    def create_rental(self, user_id, car_id): # Rental_date is set to current date by default & Rental_status is set to 'ongoing' by default
        try:
            # Verify if the car is available before creating a rental
            self.db.cursor.execute(
                "SELECT car_status FROM lyfter_car_rental.cars WHERE id = %s",
                (car_id,)
            )
            result = self.db.cursor.fetchone()

            if not result:
                return False, f"Car with ID {car_id} does not exist."
            
            car_status = result[0]

            # Validate if the car is available for rental
            if car_status != 'available':
                return False, f"Car with ID {car_id} is not available for rental. Current status: {car_status}"
            
            # Create the rental record
            self.db.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (user_id, car_id) VALUES (%s, %s)",
                (user_id, car_id)
            )

            # UPDATE car status to 'rented' when a rental is created
            self.db.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status = 'rented' WHERE id = %s",
                (car_id,)
            )

            return True, "Rental created successfully."
        except Exception as e:
            return False, f"Error creating rental: {e}"
    
    def complete_rental(self, rental_id):
        try:
            # Update rental status to 'completed'
            self.db.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status = 'completed' WHERE id = %s",
                (rental_id,)
            )

            # Update car status to 'available' when a rental is completed
            self.db.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status = 'available' WHERE id = (SELECT car_id FROM lyfter_car_rental.rentals WHERE id = %s)",
                (rental_id,)
            )
            return True
        except Exception as e:
            print(f"Error completing rental: {e}")
            return False
        
    def update_rental_status(self, rental_id, rental_status):
        try:
            self.db.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE id = %s",
                (rental_status, rental_id)
            )
            return True
        except Exception as e:
            print(f"Error updating rental status: {e}")
            return False
        
    def get_rentals(self, filters=None):
        try:
            query = """
                SELECT 
                    r.id,
                    r.user_id,
                    u.full_name AS user_name,
                    r.car_id,
                    c.brand AS car_brand,
                    c.model AS car_model,
                    r.rental_date,
                    r.rental_status
                FROM lyfter_car_rental.rentals r
                JOIN lyfter_car_rental.users u ON r.user_id = u.id
                JOIN lyfter_car_rental.cars c ON r.car_id = c.id"""
            params = []

            if filters:
                conditions = []
                for key, value in filters.items():
                    if key == 'rental_date':# rental_date formatting to only date for filtering
                        conditions.append(f'{key}::date = %s')
                    else:
                        conditions.append(f'{key} = %s')
                    params.append(value)
                query += " WHERE " + " AND ".join(conditions)

            results = self.db.execute_query(query, params if params else None)

            if not results:
                return []
            
            formatted_rentals = [self._format_rental(rental) for rental in results]
            return formatted_rentals
        
        except Exception as e:
            print(f"Error retrieving rentals: {e}")
            return False
    
    #  Format rental data into a dictionary, encapsuling the logic for data representation 
    def _format_rental(self, rental_record):
        return {
            "rental_id": rental_record[0],
            "user_id": rental_record[1],
            "user_name": rental_record[2],
            "car_id": rental_record[3],
            "car_brand": rental_record[4],
            "car_model": rental_record[5],
            "rental_date": rental_record[6],
            "rental_status": rental_record[7]
        }
