from whatsinthebox.challenges.input_formatter import IOFormatter

class TestInputException(Exception):
    pass

class BaseChallenge(object):
    level = None
    expected_input = None
    test_cases = None

    result_formatter = None
    output_formatter = IOFormatter(str, "")

    @classmethod
    def check_input(cls, input_params):
        if input_params in [test_case.parameters for test_case in cls.test_cases]:
            raise TestInputException("This input is reserved for testing")
        return True

    @staticmethod
    def query(*args):
        raise NotImplemented("this is the base class.")
