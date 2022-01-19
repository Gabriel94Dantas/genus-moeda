
class Error:
    error = {}
    def raise_error(self, code, message):
        self.error = {
            'code': code,
            'message': message
        }
        return self.error