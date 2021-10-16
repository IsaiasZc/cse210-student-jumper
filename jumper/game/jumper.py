import csv
import random

class Jumper:
  
    def __init__(self):
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
        # Here we will replace the respective 
        found = False # this information will be returned if a leter is not found in the  word
        for idx, character in enumerate(self.word):
            if character == letter:
                self.spaces[idx] = letter
                found = True
        
        return found # A boolean, this will help us to remove the attemps fromthe guesses if necessary

    def print_draw(self, attempts):
        # It's necessary to define how the attempts will be subtracted
        return self.jumper[attempts] # here we will print the respective figure as attemps the guesser has

    def read_words(self):
      """This method read through the csv
      file to create a list to store the words.
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
      chosen = ""
      for i in self.spaces:
        chosen += i
      
      return chosen == self.word
