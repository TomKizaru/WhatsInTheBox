from whatsinthebox.challenges.core.basechallenge import BaseChallenge
from whatsinthebox.challenges.core.testcase import TestCase

# noinspection PyMethodOverriding
from whatsinthebox.challenges.formatting_utils import format_int
from whatsinthebox.challenges.input_formatter import IOFormatter


class SubtractChallenge(BaseChallenge):
    level = 0
    test_cases = [
        TestCase((5, 8), "5, 8"),
        TestCase((42, 2), "42, 2"),
        TestCase((0, 1), "0, 1")]

    expected_input = [
        IOFormatter(format_int, "Enter an integer: "),
        IOFormatter(format_int, "Enter another integer: ")]

    result_formatter = IOFormatter(format_int, "Please enter an integer: ")

    @staticmethod
    def query(first_number, second_number):
        return first_number - second_number
