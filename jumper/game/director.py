from game.jumper import Jumper
from game.guesser import Guesser
from game.console import Console

class Director:
    
    def __init__(self):
        """The class constructor. Declares and initializes instance attributes.
        Args:
            self (Hider): An instances of Hider."""
        self.keep_playing = True
        self.jumper = Jumper()
        self.console = Console()
        self.guesser = Guesser()
    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Prints the blank spaces for the word,
        draws the jumper with his parashute,
        prits the prompt to "Guess the letter from A to Z
        and then stores it in the guesser

        Args:
            self (Director): an instance of Director
        """
        # First we write the blank spaces from the Jumper
        self.console.write_word(self.jumper.spaces)

        # then, we print the jumper draw
        draw = self.jumper.print_draw(self.guesser.attempts)
        self.console.write(draw)
        
        #Ask for the chosen character  
        choice = self.console.read("Guess a letter [a-z]: ")

        self.guesser.store_letters(choice) # store it in the guesser

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case calls for the letter chosen, then the letter is compared with the 
        randomly chosen word that the guesser needs to guess, and then it refreshes the attempts

        Args:
            self (Director): An instance of Director.
        """
        # first call the last letter chosen by the guesser
        letter = self.guesser.guess_words[-1]
        found = self.jumper.letter_in_word(letter) # then, send the letter to be compare with the jumper word
        self.guesser.refresh_attempts(found) # refresh the attempts

    def do_outputs(self):
        """Outputs the messages at the end of the game.
        Ends the game for the guessor.

        Args:
            self (Director): an instance of the director
        """
        if self.guesser.keep_playing():
            draw = self.jumper.print_draw(self.guesser.attempts)
            self.console.write(draw)
            self.console.write("Great guess, keep it up!")
            self.console.write("==========================")
            self.console.write(f"The word was {self.jumper.word}")
            self.console.write("==========================")
            self.keep_playing = False
        elif self.jumper.keep_playing():
            self.console.write("You win bro!")
            self.keep_playing = False

            
        


