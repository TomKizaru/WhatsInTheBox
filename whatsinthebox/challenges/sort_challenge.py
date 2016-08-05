from challenges.core.basechallenge import BaseChallenge
from challenges.core.testcase import TestCase

# noinspection PyMethodOverriding
from challenges.formatting_utils import format_list
from challenges.input_formatter import InputFormatter


class SortChallenge(BaseChallenge):
    level = 1
    test_cases = [
        TestCase(([1, 2, 3, 4]), "1, 2, 3, 4"),
        TestCase(([4, 3, 2, 1]), "4, 3, 2, 1"),
        TestCase(([2, 5, -1, -3]), "2, 5, -1, -3")]

    expected_input = [
        InputFormatter(format_list, "Enter a list: ")]

    result_formatter = InputFormatter(format_list, "Please enter a list: ")

    @staticmethod
    def query(check_list):
        return check_list.sort()
