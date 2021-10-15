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
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass

