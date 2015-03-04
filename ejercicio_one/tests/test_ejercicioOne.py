from unittest import TestCase
from classes.ejercicio_one import EjercicioOne

__author__ = 'pablo'


class TestEjercicioOne(TestCase):
    def test_concat_num_args_greater_than_10(self):
        self.assertRaises(SyntaxError, EjercicioOne.concat, "hello", "adios", "ee", "assd", "dssdf", "sgdgf", "sddf", "sdfsdf", "dsfdf", "sddfdsf", "sfssf")

    def test_concat_num_args_less_than_2(self):
        self.assertRaises(SyntaxError, EjercicioOne.concat, "sdfsdfd")

    def test_concat_param_integer(self):
        self.assertRaises(ValueError, EjercicioOne.concat, 1, 2)

    def test_concat_param_float(self):
        self.assertRaises(ValueError, EjercicioOne.concat, 1.9, 9.8)

    def test_concat_param_greater_than_10_characters(self):
        self.assertRaises(ValueError, EjercicioOne.concat, "hhshshdkrtlistrl", "hhshshdkrtlistrl")

    def test_concat_result_without_spaces(self):
        result = EjercicioOne.concat("hola ", "adios")
        assert result.find(' ') == -1
