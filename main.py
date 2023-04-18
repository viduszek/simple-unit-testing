import unittest
import datetime

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-2, 4), 1) # Error on purpose! (4 should be 3)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-2, 3), -5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(4, 2), 2)
        self.assertRaises(ValueError, self.calculator.divide, 4, 0)


if __name__ == "__main__":
    # unittest.main()

    with open('results.txt', 'a') as file:
        result = unittest.TestResult()
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
        suite.run(result)

        now = datetime.datetime.now()

        file.write("\n--- Test: ")
        file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        file.write("\nTests: {}\n".format(result.testsRun))
        file.write("Errors: {}\n".format(len(result.errors)))
        file.write("Failures: {}\n".format(len(result.failures)))
        if len(result.errors) + len(result.failures) == 0:
            file.write("All tests OK.")
        else:
            file.write("Errors: {}\n".format(result.errors))
            file.write("Failures: {}\n".format(result.failures))

