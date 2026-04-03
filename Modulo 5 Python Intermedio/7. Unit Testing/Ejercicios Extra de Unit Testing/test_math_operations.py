# from math_operations import mathOps
import importlib.util
import pytest

path = r"D:\Lyfter-Exercises-main\Lyfter-Exercises\Modulo 5 Python Intermedio\7. Unit Testing\Ejercicios Extra de Unit Testing\1. math_operations.py"
spec = importlib.util.spec_from_file_location("math_operations", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

mathOps = module.mathOps

ops = mathOps()

def test_add_positive_numbers():
    #arrange
    a = 2
    b = 3
    #act
    expected = 5
    #assert
    assert ops.add(a, b) == expected

def test_average_negative_numbers():
    #arrange
    numbers = [-1, -2, -3, 5, 10]
    #act
    expected = 1.8
    #assert
    assert ops.average(numbers) == expected

def test_divide():
    #arrange
    number1 = 10
    number2 = 2
    #act
    expected = 5
    #assert
    assert ops.divide(number1, number2) == expected

def test_divide_by_zero():
    #arrange
    number1 = 10
    number2 = 0
    #act and assert
    with pytest.raises(ValueError):
        ops.divide(number1, number2)

def test_divide_non_numeric():
    #arrange
    number1 = 10
    number2 = "a string"
    #act and assert
    with pytest.raises(TypeError):
        ops.divide(number1, number2)
