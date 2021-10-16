class Guesser:

    def __init__(self):
        """The constructor.
        
        Args:
            self(Guesser): an instance of the Gueser.
            attempts(number): How much attemps has the guesser.
        """
        self.attempts = 4
        self.guess_words = []

    def store_letters(self,choice):
        """store all the letters chosen by the
        guesser

        Args:
            self(Guesser): an instance of the Gueser.
        """
        self.guess_words.append(choice)

    def refresh_attempts(self, found):
        """This method refresh the ramaining 
        attemps for the guesser.

        Args.
            self(Guesser): an instance of the Gueser.
        """
        if not found:
            self.attempts -= 1

    def keep_playing(self):
        """This method return a boolean with information
        about the attempts status.

        Args.
            self(Guesser): an instance of the Gueser.
        """
        return self.attempts <= 0