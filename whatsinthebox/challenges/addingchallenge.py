from challenges.core.basechallenge import BaseChallenge
from challenges.core.testcase import TestCase

# noinspection PyMethodOverriding
from challenges.formatting_utils import format_int
from challenges.input_formatter import InputFormatter


class AddingChallenge(BaseChallenge):
    level = 0
    test_cases = [
        TestCase((13, 2), "1, 2 "),
        TestCase((-3, 2), "1, 2 "),
        TestCase((0, 4), "1, 2 ")]

    expected_input = [
        InputFormatter(format_int, "Enter an integer."),
        InputFormatter(format_int, "Enter another integer.")]

    @staticmethod
    def query(first_number, second_number):
        return first_number + second_number
