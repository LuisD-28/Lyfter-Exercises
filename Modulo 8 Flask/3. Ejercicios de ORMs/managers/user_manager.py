from database import SessionLocal
from models import User

class UserManager:

    def create_user(self, full_name, email, username, password):
        with SessionLocal() as session:
            new_user = User(
                full_name=full_name,
                email=email,
                username=username,
                password=password
            )
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
    
    # Only the fields listed in ALLOWED_UPDATE_FIELDS can be updated
    ALLOWED_UPDATE_FIELDS = {"full_name", "email", "username", "password"}
    def update_user(self, user_id, **kwargs):
        with SessionLocal() as session:
            user = session.get(User, user_id)
            if not user:
                return None
            
            for key, value in kwargs.items():
                if key in self.ALLOWED_UPDATE_FIELDS:
                    setattr(user, key, value)
                else:
                    print(f"Field User'{key}' is not allowed to be updated.")

            session.commit()
            session.refresh(user)
            return user
        
    def delete_user(self, user_id):
        with SessionLocal() as session:
            user = session.get(User, user_id)
            if not user:
                return False
            
            session.delete(user)
            session.commit()
            return True
        
    def get_all_users(self):
        with SessionLocal() as session:
            return session.query(User).all()

    def get_user_by_id(self, user_id):
        with SessionLocal() as session:
            return session.get(User, user_id)