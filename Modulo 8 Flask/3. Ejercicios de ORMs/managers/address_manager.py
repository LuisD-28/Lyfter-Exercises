from database import SessionLocal
from models import Address

class AddressManager:

    def create_address(self, street, city, state, zip_code, user_id):
        with SessionLocal() as session:
            address = Address(
                street=street,
                city=city,
                state=state,
                zip_code=zip_code,
                user_id=user_id
            )
            session.add(address)
            session.commit()
            session.refresh(address)
            return address
        
    def update_address(self, address_id, **kwargs):
        with SessionLocal() as session:
            address = session.get(Address, address_id)
            if not address:
                return None
            
            for key, value in kwargs.items():
                if hasattr(address, key):
                    setattr(address, key, value)

            session.commit()
            session.refresh(address)
            return address
        
    def delete_address(self, address_id):
        with SessionLocal() as session:
            address = session.get(Address, address_id)
            if not address:
                return False
            
            session.delete(address)
            session.commit()
            return True

    def get_addresses(self):
        with SessionLocal() as session:
            addresses = session.query(Address).all()
            return addresses
        
    def get_address_by_id(self, address_id):
        with SessionLocal() as session:
            address = session.get(Address, address_id)
            return address