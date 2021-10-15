class Console:

    def __init__(self):
        pass

    def read(self, message):
        return input(message).lower()

    def write(self,message):
        print(message)

    def write_word(self, word):
        for character in word:
            print(character, end=" ") # With this we will have the spaces formated. Example: "_ _ _ _"