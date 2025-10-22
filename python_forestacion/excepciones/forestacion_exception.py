class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del sistema de forestación.
    """

    def __init__(self, error_code: str, user_message: str):
        super().__init__(f"[{error_code}] {user_message}")
        self.error_code = error_code
        self.user_message = user_message

    def get_error_code(self):
        return self.error_code

    def get_user_message(self):
        return self.user_message

    def get_full_message(self):
        return f"Error {self.error_code}: {self.user_message}"
