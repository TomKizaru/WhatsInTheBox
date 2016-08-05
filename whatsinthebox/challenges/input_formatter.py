class IOFormatter(object):
    def __init__(self, conversion_function, info_message):
        self.conversion_function = conversion_function
        self.info_message = info_message
