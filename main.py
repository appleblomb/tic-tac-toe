import numpy as np

class Gameboard:
    def __init__(self, size=3):
        self.board = np.arange(size * size).reshape(size, size).astype(str)

    def make_move(self, position, character):
        # normalize position to string (board stores string values)
        pos_str = str(position)
        # find positions matching the requested position
        matches = np.argwhere(self.board == pos_str)
        if matches.size == 0:
            return False
        # use the first match, replace with the character, and return True
        r, c = matches[0]
        self.board[r, c] = character
        return True
    
    def display(self):
        print(self.board)
    
class Player:
    """
    Player class that can be extended for different types of players.
    """
    def __init__(self, character: str, gameboard: Gameboard):
        self.character = character
        self.board = gameboard

    def decide_move(self, gameboard: Gameboard) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")

class HumanPlayer(Player):
    """
    Player subclass for human players that prompts for input.
    """
    def decide_move(self, gameboard: Gameboard) -> None:
        prompt = f"Player {self.character}, enter your move: "
        while True:
            move = input(prompt).strip()
            if self.board.make_move(move, self.character):
                return
            print("Invalid move. Try again.")

def main():
    print("Hello from tic-tac-toe!")
    game = Gameboard()
    game.display()

    while True:
        player_x = HumanPlayer("X", game)
        player_x.decide_move(game)
        game.display()
        
        player_o = HumanPlayer("O", game)
        player_o.decide_move(game)
        game.display()


if __name__ == "__main__":
    main()
