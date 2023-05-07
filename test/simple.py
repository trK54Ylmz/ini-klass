from ini import IniConfig
from pathlib import Path
from unittest import TestCase


class SimpleTest(TestCase):
    def setUp(self):
        path = Path(__file__).parent / 'simple.ini'

        self.config = IniConfig.read(str(path), empty_to_none=False)

    def test_numeric(self):
        self.assertEqual(self.config.example.id, 12)

    def test_string(self):
        self.assertEqual(self.config.example.name, 'John')

    def test_boolean(self):
        self.assertEqual(self.config.example.status, True)

    def test_float(self):
        self.assertEqual(self.config.example.salary, 100.5)

    def test_null_list(self):
        self.assertEqual(self.config.nulls.age, '')

    def test_list(self):
        self.assertEqual(self.config.example.group, ['car', 'book', 'phone'])

    def test_empty_list(self):
        self.assertEqual(self.config.example.detail, ['user'])
