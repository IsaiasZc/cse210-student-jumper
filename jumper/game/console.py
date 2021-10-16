class Console:

    def __init__(self):
        """The constructor.
        
        Args:
           self(Console): an instance of the Console.
        """

    def read(self, message):
        """ make an input for the guesser
        and retunr a lower case result.

        Args:
           self(Console): an instance of the Console.
        """
        return input(message).lower()

    def write(self,message):
        """return a message given as parameter.

        Args:
           self(Console): an instance of the Console.
        """
        print(message)

    def write_word(self, word):
        """Print a list as a string separeted by
        blank spaces

        Args:
           self(Console): an instance of the Console.
        """

        for character in word:
            print(character, end=" ") # With this we will have the spaces formated. Example: "_ _ _ _"