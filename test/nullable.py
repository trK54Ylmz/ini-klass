from ini import IniConfig
from pathlib import Path
from unittest import TestCase


class NullableTest(TestCase):
    def setUp(self):
        path = Path(__file__).parent / 'simple.ini'

        self.config = IniConfig.read(str(path), empty_to_none=True)

    def test_null_array(self):
        self.assertEqual(self.config.nulls.age, None)

    def test_string(self):
        self.assertEqual(self.config.nulls.users, [1, 2, None])
