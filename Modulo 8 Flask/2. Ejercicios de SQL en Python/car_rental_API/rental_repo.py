class RentalRepository:
    def __init__(self, db):
        self.db = db

    def create_rental(self, user_id, car_id): # Rental_date is set to current date by default & Rental_status is set to 'ongoing' by default
        try:
            self.db.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (user_id, car_id) VALUES (%s, %s)",
                (user_id, car_id)
            )

            # UPDATE car status to 'rented' when a rental is created
            self.db.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status = 'rented' WHERE id = %s",
                (car_id,)
            )

            return True
        except Exception as e:
            print(f"Error creating rental: {e}")
            return False
    
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
            query = "SELECT * FROM lyfter_car_rental.rentals"
            params = []

            if filters:
                conditions = []
                for key, value in filters.items():
                    if key == 'rental_date':# rental_date formatting to date only for filtering
                        conditions.append(f'{key}::date = %s')
                    else:
                        conditions.append(f'{key} = %s')
                    params.append(value)
                query += " WHERE " + " AND ".join(conditions)

            # if filters:
            #     conditions = []
            #     for key, value in filters.items():
            #         conditions.append(f'{key} = %s')
            #         params.append(value)
            #     query += " WHERE " + " AND ".join(conditions)

            result = self.db.execute_query(query, params if params else None)
            return result
        
        except Exception as e:
            print(f"Error retrieving rentals: {e}")
            return False