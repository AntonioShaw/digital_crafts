class CalculatorTests(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(2,3)
        self.assertEual(5, rsult)