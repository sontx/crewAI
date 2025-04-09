class InterruptedException(Exception):
    """
    Exception raised when the user or tool interrupts the program.
    """

    def __init__(self, message: str = "Program interrupted", resumable = True, success=False) -> None:
        super().__init__(message)
        self.message = message
        self.resumable = resumable
        self.success = success