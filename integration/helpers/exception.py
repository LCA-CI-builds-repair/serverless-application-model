fclass StatusCodeError(Error):
    def __init__(self, message):
        self.message = message py.error import Error


class StatusCodeError(Error):
    """raise when the return status code is not match the expected one"""
