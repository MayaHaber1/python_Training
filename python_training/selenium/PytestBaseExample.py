from unittest import TestCase


class PytestBaseExample (TestCase):


    def test_pass_first_example (self):
        sum = 2 + 3
        exp_sum = 7
        multi = 2*3
        self.assertTrue(sum == exp_sum, "the summery results is not as expected")
        self.assertTrue(multi == 6 , "the multiple results is not as expected")


    def test_pass_second_example(self):
        self.assertTrue(True, "true was not found")

    def test_fail_example(self):
        sum =2+3
        exp_sum = 6
        self.assertEqual(exp_sum ,sum , "the summery of 2+3 is not 5 as expected")