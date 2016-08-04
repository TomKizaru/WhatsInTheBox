import exceptions

class ExitException(Exception):
    pass

class TestException(Exception):
    pass

class ChallengePresentor(object):
    def __init__(self):
        pass

    def show_challenge(self, challenge):
        self.print_initial_message()
        while True:
            try:
                input = self.get_input()
            except:
                raise
            result = challenge.query()

    def print_initial_message(self):
        print "Enter exit to exit, test to have the test"

    def get_input(self):
        input = raw_input()
        if input == 'exit':
            raise ExitException()
        elif input == 'test':
            raise TestException()
        return input

    #sdsadsd