from datetime import date

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def underage_check(func):
    def wrapper(user: User, *args):
        if user.age < 18:
            raise Exception('El Usuario es menor de edad')
        return func(user, *args)
    return wrapper


@underage_check
def verify_years_old(user: User):
    return f'User age: {user.age}'

user1 = User(date(1996, 9, 10))
user2 = User(date(2010, 5, 10))

try:
    print(verify_years_old(user1))
    print(verify_years_old(user2))
except Exception as e:
    print(e)