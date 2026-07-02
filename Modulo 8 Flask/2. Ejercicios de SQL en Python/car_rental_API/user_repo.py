class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, full_name, email, username, password, birth_date):# account_status 'active' by default
        try:    
            self.db.execute_query(
                "INSERT INTO lyfter_car_rental.users (full_name, email, username, password, birth_date) VALUES (%s, %s, %s, %s, %s)",
                (full_name, email, username, password, birth_date)
            )
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        
    
    def update_user_status(self, user_id, account_status):
        try:
            self.db.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s",
                (account_status, user_id)
            )
            return True
        except Exception as e:
            print(f"Error updating user status: {e}")
            return False
    
    def flag_user_as_blocked(self, user_id):
        try:
            self.db.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = 'blocked' WHERE id = %s",
                (user_id,)
            )
            return True
        except Exception as e:
            print(f"Error flagging user as blocked: {e}")
            return False
        
    def get_users(self, filters=None):
        try:
            query = "SELECT * FROM lyfter_car_rental.users"
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
            
            formatted_users = [self._format_user(user) for user in results]
            return formatted_users
        except Exception as e:
            print(f"Error retrieving users: {e}")
            return False
    
    #  Format user data into a dictionary, encapsuling the logic for data representation 
    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "username": user_record[3],
            "birth_date": user_record[5].strftime("%Y-%m-%d"),
            "account_status": user_record[6]
        }
