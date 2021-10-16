class Guesser:

    def __init__(self):
        self.attempts = 4

    def refresh_attempts(self, found):
        if not found:
            self.attempts -= 1

    def keep_playing(self):
        return self.attempts <= 0