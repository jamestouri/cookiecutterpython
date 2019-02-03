import app
import unittest
import os


class TestAlg(unittest.TestCase):
    def test_addTwoNumbers(self):
        add = app.Alg()
        result = add.addTwoNumbers(3, 4)
        self.assertEqual(
            result,
            7,
        )

    def test_subtractNumbers(self):
        subtract = app.Alg()
        result = subtract.subtractNumbers(4, 1)
        self.assertEqual(
            result,
            3,
        )


class TestMultiplyNumbers(unittest.TestCase):
    def test_multiplyNumbers(self):
        result = app.multiplyNumbers(5, 3)
        self.assertEqual(
            result,
            15,
        )
