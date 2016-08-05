from whatsinthebox.challenges.core.basechallenge import BaseChallenge
from whatsinthebox.challenges.core.testcase import TestCase

# noinspection PyMethodOverriding
from whatsinthebox.challenges.formatting_utils import format_positive_int
from whatsinthebox.challenges.input_formatter import IOFormatter


class SortChallenge(BaseChallenge):
    level = 2
    test_cases = [
        TestCase((0), "0"),
        TestCase((255), "255"),
        TestCase((8), "8")]

    expected_input = [
        IOFormatter(format_positive_int, "Enter a positive number: ")]

    result_formatter = IOFormatter(format_positive_int, "Please enter a positive number: ")

    @staticmethod
    def query(check_num):
        return bin(check_num)[2:]
