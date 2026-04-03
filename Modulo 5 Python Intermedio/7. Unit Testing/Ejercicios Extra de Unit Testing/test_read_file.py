import pytest
from unittest.mock import mock_open, patch
import importlib.util

path = r"D:\Lyfter-Exercises-main\Lyfter-Exercises\Modulo 5 Python Intermedio\7. Unit Testing\Ejercicios Extra de Unit Testing\2. read_file.py"
spec = importlib.util.spec_from_file_location("read_file", path)
module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)
read_lines = module.read_lines

def test_read_lines_success():
    # Simula el contenido del archivo
    mock_file_content = "Line 1\nLine 2\nLine 3\n"

    # mock_open para simular la apertura y lectura del archivo
    m = mock_open(read_data=mock_file_content)

    #patch para reemplazar opem solo dentro de este contexto
    with patch("builtins.open", m):
        result = read_lines("fake_path.txt")

    assert result == ["Line 1\n", "Line 2\n", "Line 3\n"]

def test_read_lines_file_not_found():
    #simula un error de archivo no encontrado
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines("non_existent_file.txt")


