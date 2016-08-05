import exceptions

from whatsinthebox.challenges.formatting_utils import FormattingException


class ChallengePresentor(object):
    def __init__(self):
        pass

    def show_challenge(self, challenge):
        while True:
            try:
                command = self.get_command()
                if command == 1:
                    return False
                elif command == 2:
                    if self.do_test(challenge):
                        print "You have passed the test!"
                        return True
                    else:
                        print "You have failed the test."
                else:
                    self.do_query(challenge)
            except FormattingException as exception:
                print exception.message


    def get_command(self):
        while True:
            command = raw_input("Enter 1) to exit\n2) to have the test\n3) to do a query\n").strip()
            if command == '1':
                return 1
            elif command == '2':
                return 2
            elif command == '3':
                return 3


    def do_test(self, challenge):
        #returns True if successful, False otherwise
        for case in challenge.test_cases:
            print "input: " + case.formatted_parameters
            answer = raw_input("answer: ")
            if challenge.result_formatter.conversion_function(answer.strip().lower()) != challenge.query(*case.parameters):
                return False
        return True

    def do_query(self, challenge):
        inputs = []
        for format in challenge.expected_input:
            input = format.conversion_function(raw_input(format.info_message))
            inputs.append(input)
        result = challenge.output_formatter.conversion_function(challenge.query(*inputs))
        print "output: " + str(result)
