class UserDataNotFoundError(Exception):
    """Getting user data encountered an issue."""

    def __init__(self, *args, message, status_code):
        super.__init__(self, *args)
        self.message = message
        self.status_code = status_code
