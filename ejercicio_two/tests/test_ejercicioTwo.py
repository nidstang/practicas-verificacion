from unittest import TestCase
from classes.ejercicio_two import EjercicioTwo
__author__ = 'pablo'


class TestEjercicioTwo(TestCase):
    def test_concat_float_concat_string_result_must_string(self):
        result = EjercicioTwo.sum(1.3, "hello")
        self.assertEquals(result, "1.3hello")

    def test_concat_integer_concat_string_result_must_string(self):
        result = EjercicioTwo.sum(2, "hello")
        self.assertEquals(result, "2hello")

    def test_concat_add_float_with_integers(self):
        result = EjercicioTwo.sum(2, 2.1)
        self.assertEquals(result, 4.1)
