import importlib.util
from pathlib import Path

import pytest


# Carga bubble_sort.py por ruta porque el nombre de archivo incluye prefijo numerico.
MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "5. Ejercicios de Algoritmos de Ordenamiento"
    / "1. bubble_sort.py"
)
spec = importlib.util.spec_from_file_location("bubble_sort_module", MODULE_PATH)
bubble_sort_module = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(bubble_sort_module)
bubble_sort = bubble_sort_module.bubble_sort


def test_bubble_sort_small_list():
    #arrange
    data = [5, 2, 9,]
    #act
    expected = [2, 5, 9]
    #assert
    assert bubble_sort(data) == expected


def test_bubble_sort_large_list():
    #arrange
    data = list(range(200, 0, -1))#reverse order
    #act
    expected = list(range(1, 201))
    #assert
    assert bubble_sort(data) == expected


def test_bubble_sort_empty_list():
    #arrange
    data = []
    #act
    expected = []
    #assert
    assert bubble_sort(data) == expected


def test_bubble_sort_type_error():
    #arrange
    data = "not a list"
    #act and assert
    with pytest.raises(TypeError):
        bubble_sort(data)
