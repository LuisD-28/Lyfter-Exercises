user_loogged_in = False

def requires_login(func):
    def wrapper(*args):
        if not user_loogged_in:
            raise Exception('Usuario no autenticado')
        return func(*args)
    return wrapper


@requires_login
def view_profile():
    print('Mostrando perfil del usuario')


try:
    view_profile()
except Exception as e:
    print(e)


user_loogged_in = True
view_profile()