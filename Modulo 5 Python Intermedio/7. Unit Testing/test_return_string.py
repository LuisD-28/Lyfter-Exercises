import importlib.util
import pytest

path = r"D:\Lyfter-Exercises-main\Lyfter-Exercises\Modulo 4 Python Basico\5.Ejercicios de Funciones\4.return_string.py"
spec = importlib.util.spec_from_file_location("return_string", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ordered_string = module.ordered_string

def test_ordered_string():
    #arrange
    data = "hello"
    #act
    expected = "olleh"
    #assert
    assert ordered_string(data) == expected

def test_ordered_string_empty():
    #arrange
    data = ""
    #act
    expected = ""
    #assert
    assert ordered_string(data) == expected

def test_ordered_string_type_error():
    #arrange
    data = 12345
    #act and assert
    with pytest.raises(TypeError):
        ordered_string(data)
