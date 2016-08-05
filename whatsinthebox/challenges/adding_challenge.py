from whatsinthebox.challenges.core.basechallenge import BaseChallenge
from whatsinthebox.challenges.core.testcase import TestCase

# noinspection PyMethodOverriding
from whatsinthebox.challenges.formatting_utils import format_int
from whatsinthebox.challenges.input_formatter import IOFormatter


class AddingChallenge(BaseChallenge):
    level = 0
    test_cases = [
        TestCase((13, 2), "13, 2"),
        TestCase((-3, 2), "-3, 2"),
        TestCase((0, 4), "0, 4")]

    expected_input = [
        IOFormatter(format_int, "Enter an integer: "),
        IOFormatter(format_int, "Enter another integer: ")]

    result_formatter = IOFormatter(format_int, "Please enter an intege: ")

    @staticmethod
    def query(first_number, second_number):
        return first_number + second_number
