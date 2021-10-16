class Guesser:

    def __init__(self):

        self.guess_words = []
        self.attempts = 4

    def store_letters(self,choice):
        self.guess_words.append(choice) # store the chosen character in the list

    def replace_letters(self):
        pass

    def refresh_attempts(self, found):
        if not found:
            self.attempts -= 1

    def keep_playing(self):
        return self.attempts <= 0

