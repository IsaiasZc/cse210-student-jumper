from jumper import Jumper
from guesser import Guesser
from console import Console

class Director:
    
    def __init__(self):
        """The constructor."""
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
        # First we write the blank spaces from the Jumper
        self.console.write_word(self.jumper.spaces)

        # then, we print the jumper draw
        draw = self.jumper.print_draw(self.guesser.attempts)
        self.console.write(draw)
        
        #Ask for the chosen character  
        choice = self.console.read("Guess a letter [a-z]: ")

        self.guesser.store_letters(choice) # store it in the guesser

    def do_updates(self):
        # first call the last letter chosen by the guesser
        letter = self.guesser.guess_words[-1]
        found = self.jumper.letter_in_word(letter) # then, send the letter to be compare with the jumper word
        self.guesser.refresh_attempts(found) # refresh the attempts

    def do_outputs(self):
        pass

