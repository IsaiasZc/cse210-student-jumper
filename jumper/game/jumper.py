import random

class Jumper:

    def __init__(self):

        self.word = "perro"
        self.spaces = "_" * len(self.word) # We well have the same underscores "_"than characters in the word
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