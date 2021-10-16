import csv
import random

class Jumper:
    """
    A code template for our jumper. The responsibility of this class of
    objects is to draw the jumper, read the list of words and compare the 
    keep playing of the game.

    Stereotype:
        Information Holder
    Attributes:
        words (list): A list of a lot of words for the game.
        word (chosen word): Chosen random word. 
        spaces (number of letters): Size of the word written in underscores.
        jumper (list): A list with the draws of the Jumper.
    """
    def __init__(self):
        """
        The class constructor. Declares and initializes instance attributes.
        Args:
            self (Jumper): An instances of Jumper.
        """
        self.words = self.read_words()
        self.word = random.choice(self.words)
        self.word = self.word[0]
        self.spaces = ["_"] * len(self.word) # We well have the same underscores "_"than characters in the word
        self.jumper = ["""

   x   
  /|\          
  / \ 

^^^^^^^
        ""","""

  \ /  
   0   
  /|\  
  / \  
         
^^^^^^^""","""

 \   / 
  \ /  
   0   
  /|\  
  / \  
         
^^^^^^^""","""

 /___\ 
 \   / 
  \ /  
   0   
  /|\  
  / \  
         
^^^^^^^""","""

  ___  
 /___\ 
 \   / 
  \ /  
   0   
  /|\  
  / \  
         
^^^^^^^"""

        ]

    def letter_in_word(self, letter):
        """ This method will replace the respective letter in the word that needs
            to be gueesed.
        Args:
            self(Jumper): An instance of Jumper.

        Returns:
            boolean: To remove the attemts from the guesser if neeeded.
        """
        # Here we will replace the respective 
        found = False # this information will be returned if a letter is not found in the  word
        for idx, character in enumerate(self.word):
            if character == letter:
                self.spaces[idx] = letter
                found = True
        
        return found # A boolean, this will help us to remove the attemps from the guesses if necessary

    def print_draw(self, attempts):
        """Draw the respective draw of the Jumper
        Args:
            self(Jumper): An instance of Jumper.

        Returns:
            string: A draw of the Jumper.
        """
        # It's necessary to define how the attempts will be subtracted
        return self.jumper[attempts] # here we will print the respective figure as attemps the guesser has

    def read_words(self):
        """This method read through the csv
          file to create a list to store the words.
        Args:
            self(Jumper): An instance of Jumper.

        Returns:
            list: A list of words.
        """

        # empty list that will store the filename data
        words = []

        with open("jumper\game\words.csv", "r") as csv_file:

            # Use the csv.reader to go through the file
            reader = csv.reader(csv_file)

                # create a key for each line
            for word in reader:

                # create a list
                words.append(word)

            return words # Return the list

    def keep_playing(self):
      """To compare the winning condition.
      Args:
            self(Jumper): An instance of Jumper.
      """
      chosen = ""
      for i in self.spaces:
        chosen += i
      
      return chosen == self.word
