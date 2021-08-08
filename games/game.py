class Game:
    title = 'Game'

    def __init__(self):
        self.running = True
        self.won = False

    def win(self):
        self.running = False
        self.won = True

    def lose(self):
        self.running = False
        self.won = False

    # Purpose: Should always start with "while self.running:". If the player wins, call self.win() and self.lose() if they lose, followed with break
    # Example:
    def run(self):
        while self.running:
            if 1 == 1:
                self.win()
