from whatsinthebox.challenges.core.basechallenge import BaseChallenge
from whatsinthebox.challenges.core.testcase import TestCase

# noinspection PyMethodOverriding
from whatsinthebox.challenges.formatting_utils import format_list, list_to_str
from whatsinthebox.challenges.input_formatter import IOFormatter


class SortChallenge(BaseChallenge):
    level = 1
    test_cases = [
        TestCase(([1, 2, 3, 4],), "1, 2, 3, 4"),
        TestCase(([4, 3, 2, 1],), "4, 3, 2, 1"),
        TestCase(([2, 5, -1, -3],), "2, 5, -1, -3")]

    expected_input = [
        IOFormatter(format_list, "Enter a list: ")]

    result_formatter = IOFormatter(format_list, "Please enter a list: ")
    output_formatter = IOFormatter(list_to_str, "")

    @staticmethod
    def query(check_list):
        return sorted(check_list)
