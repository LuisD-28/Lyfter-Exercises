import importlib.util

path = r"D:\Lyfter-Exercises-main\Lyfter-Exercises\Modulo 4 Python Basico\5.Ejercicios de Funciones\7.prime_number.py"
spec = importlib.util.spec_from_file_location("prime_number", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
get_primenumbers = module.get_primenumbers

def test_get_primenumbers_primeNumber():
    #arrange
    data = 7
    #act
    expected = True
    #assert
    assert get_primenumbers(data) == expected

def test_get_primenumbers_notPrimeNumber():
    #arrange
    data = 10
    #act
    expected = False
    #assert
    assert get_primenumbers(data) == expected

def test_get_primenumbers_negativeNumber():
    #arrange
    data = -5
    #act
    expected = False
    #assert
    assert get_primenumbers(data) == expected
