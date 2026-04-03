import importlib.util

path = r"D:\Lyfter-Exercises-main\Lyfter-Exercises\Modulo 4 Python Basico\5.Ejercicios de Funciones\5.Upper_and_lowerCases_count.py"
spec = importlib.util.spec_from_file_location("upper_and_lower_cases_count", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
upper_and_lower_cases_count = module.upper_and_lower_cases_count

def test_upper_and_lower_cases_count_no_upper():
    #arrange
    data = 'hello world'
    #act
    expected = (0, 10)
    #assert
    assert upper_and_lower_cases_count(data) == expected

def test_upper_and_lower_cases_count_no_lower():
    #arrange
    data = 'HELLO WORLD'
    #act
    expected = (10, 0)
    #assert
    assert upper_and_lower_cases_count(data) == expected

def test_upper_and_lower_cases_count_special_characters():
    #arrange
    data = 'Hello, World! 123'
    #act
    expected = (2, 8)
    #assert
    assert upper_and_lower_cases_count(data) == expected