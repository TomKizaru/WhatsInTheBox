from challenges.core.basechallenge import BaseChallenge
from challenges.core.testcase import TestCase


# noinspection PyMethodOverriding
class AddingChallenge(BaseChallenge):
    level = 0
    test_cases = [TestCase((1, 2), "1, 2 ")]

    @staticmethod
    def query(first_number, second_number):
        return first_number + second_number
