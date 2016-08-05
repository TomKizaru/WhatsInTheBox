from whatsinthebox.challenges.input_formatter import IOFormatter


class BaseChallenge(object):
    level = None
    expected_input = None
    test_cases = None

    result_formatter = None
    output_formatter = IOFormatter(str, "")

    @staticmethod
    def query(*args):
        raise NotImplemented("this is the base class.")
