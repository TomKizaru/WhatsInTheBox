
class BaseChallenge(object):
    level = None
    expected_input = None
    test_cases = None
    
    @staticmethod
    def query(*args):
        raise NotImplemented("this is the base class.")

