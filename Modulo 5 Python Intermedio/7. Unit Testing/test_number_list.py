# import importlib.util
# from pathlib import Path

# import pytest

# MODULE_PATH = (
#     Path(__file__).resolve().parents[1]
#     / "Modulo 4 Python Basico"
#     / "5. Ejercicios de Funciones"
#     / "3. number_list.py"
# )
# spec = importlib.util.spec_from_file_location("number_list_module", MODULE_PATH)
# number_list_module = importlib.util.module_from_spec(spec)
# assert spec is not None and spec.loader is not None
# spec.loader.exec_module(number_list_module)
# getList_total = number_list_module.getList_total
import importlib.util
import pytest

path = r"D:\Lyfter-Exercises-main\Lyfter-Exercises\Modulo 4 Python Basico\5.Ejercicios de Funciones\3.number_list.py"

spec = importlib.util.spec_from_file_location("number_list", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
getList_total = module.getList_total


def test_getList_total():
    #arrange
    data = [1,2]
    #act
    expected = 3
    #assert
    assert getList_total(data) == expected

def test_getList_total_empty():
    #arrange
    data = []
    #act
    expected = 0
    #assert
    assert getList_total(data) == expected

def test_getList_total_type_error():
    #arrange
    data = "not a list"
    #act and assert
    with pytest.raises(TypeError):
        getList_total(data)
