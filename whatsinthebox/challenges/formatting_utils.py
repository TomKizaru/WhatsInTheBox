class FormattingException(Exception):
    pass


def format_int(input_string):
    try:
        result = int(input_string)
    except ValueError:
        raise FormattingException("Couldn't parse as int.")

    return result


def format_float(input_string):
    try:
        result = float(input_string)
    except ValueError:
        raise FormattingException("Couldn't parse as float.")

    return result


def format_list(input_string):
    try:
        result = [float(curr) for curr in input_string.split(" ") if len(curr) > 0]
    except ValueError:
        raise FormattingException("Couldn't parse the numbers entered.\n\
         Please make sure you entered a list on numbers with spaces as separators.")

    return result
