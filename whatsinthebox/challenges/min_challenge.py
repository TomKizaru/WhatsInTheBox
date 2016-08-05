from whatsinthebox.challenges.core.basechallenge import BaseChallenge
from whatsinthebox.challenges.core.testcase import TestCase

# noinspection PyMethodOverriding
from whatsinthebox.challenges.formatting_utils import format_int
from whatsinthebox.challenges.input_formatter import IOFormatter


class MinChallenge(BaseChallenge):
    level = 1
    test_cases = [
        TestCase((100, -100), "100, -100"),
        TestCase((16, 17), "16, 17"),
        TestCase((3, 3), "3, 3")]

    expected_input = [
        IOFormatter(format_int, "Enter an integer: "),
        IOFormatter(format_int, "Enter another integer: ")]

    result_formatter = IOFormatter(format_int, "Please enter an integer: ")

    @staticmethod
    def query(first_number, second_number):
        return min(first_number, second_number)
