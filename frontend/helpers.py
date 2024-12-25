import re


EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


def validate_email(email):
    return bool(re.match(EMAIL_REGEX, email))


def is_positive_integer(s):
    return s.isdigit() and int(s) >= 0
