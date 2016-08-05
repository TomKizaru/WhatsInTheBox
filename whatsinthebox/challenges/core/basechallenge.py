class BaseChallenge(object):
    level = None
    expected_input = None
    test_cases = None

    result_formatter = None

    @staticmethod
    def query(*args):
        raise NotImplemented("this is the base class.")
