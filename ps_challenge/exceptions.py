class UserDataNotFoundError(Exception):
    """Getting user data from remote API encountered an issue."""

    def __init__(self, msg, status_code):
        super().__init__(msg)
        self.msg = msg
        self.status_code = status_code
