import unittest
import ex2_203436449 as test_file


class TestMain(unittest.TestCase):
    def average_list_length_test(self):
        first_lst_test = []
        second_lst_test = ['h', 'h', 'h']
        third_lst_test = ['123', '123456', '12', '123']
        fourth_lst_test = ['hello', 123]

        result1 = test_file.average_list_length(first_lst_test)
        self.assertEqual(result1,)


# ?how to check functions that print and do not return anything at all
