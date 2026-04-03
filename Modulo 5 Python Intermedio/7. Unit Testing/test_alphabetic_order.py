import importlib.util
import pytest

path = r"D:\Lyfter-Exercises-main\Lyfter-Exercises\Modulo 4 Python Basico\5.Ejercicios de Funciones\6. alphabetic_order.py"
spec = importlib.util.spec_from_file_location("alphabetic_order", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
alphabetic_order = module.alphabetic_order

def test_alphabetic_order_empty_string():
    #arrange
    data = ['']
    #act
    expected = ''
    #assert
    assert alphabetic_order(data) == expected

def test_alphabetic_order_type_error():
    #arrange
    data = 12345
    #act and assert
    with pytest.raises(TypeError):
        alphabetic_order(data)

def test_alphabetic_order_normal_string_list():
    #arrange
    data = ['banana', 'apple', 'cherry']
    #act
    expected = 'apple-banana-cherry'
    #assert
    assert alphabetic_order(data) == expected