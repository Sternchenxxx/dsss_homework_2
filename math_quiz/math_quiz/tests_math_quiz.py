import unittest
from math_quiz import RandomNumber, RandomOperaters, Calculate


class TestMathGame(unittest.TestCase):

    def test_RandomNumber(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_RandomOperaters(self):
        # TODO
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operators
            operator = RandomOperaters()
            self.assertIn(operator, valid_operators)

    def test_Calculate(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
                (5, 2, '-', '5 - 2', 3)
                (5, 2, '*', '5 * 2', 10)
                (2, 5, '-', '2 - 5', -3)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, answer = Calculate(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertAlmostEqual(answer, expected_answer) 

if __name__ == "__main__":
    unittest.main()
