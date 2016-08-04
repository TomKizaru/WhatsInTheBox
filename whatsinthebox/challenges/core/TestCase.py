
"""class TestCase(object): R.I.P
    def __init__(self,parameters):
        self._parameters=parameters

    def __str__(self):
        return " ".join(map(str, self._parameters))
"""

class TestCase(object):
    def __init__(self, parameters, formatted_parameter):
        self.parameters = parameters
        self.formatted_parameter = formatted_parameter

    def __str__(self):
        return self.formatted_parameter
