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
    
    def _row_contains_only(self, character: str) -> bool:
        """
        Private helper.
        Return True if any row in the board array consists entirely of `character`.
        """
        # Compare elementwise to character, then check rows where all entries match.
        return bool(np.any(np.all(self.board == character, axis=1)))
    
    def _col_contains_only(self, character: str) -> bool:
        """
        Private helper.
        Return True if any column in the board array consists entirely of `character`.
        """
        # Compare elementwise to character, then check columns where all entries match.
        return bool(np.any(np.all(self.board == character, axis=0)))
    
    def _ul_br_diag_contains_only(self, character: str) -> bool:
        """
        Private helper.
        Return True if the upper-left to bottom-right diagonal consists entirely of `character`.
        """
        # Extract main diagonal and check all entries equal to character
        return bool(np.all(np.diag(self.board) == character))
    
    def _ur_bl_diag_contains_only(self, character: str) -> bool:
        """
        Private helper.
        Return True if the upper-right to bottom-left diagonal consists entirely of `character`.
        """
        # Extract anti-diagonal and check all entries equal to character
        return bool(np.all(np.diag(np.fliplr(self.board)) == character))

    def is_winner(self, character: str) -> bool:
        """
        Return True if `character` has won the game.
        """
        return self._row_contains_only(character) or\
               self._col_contains_only(character) or \
               self._ul_br_diag_contains_only(character) or \
               self._ur_bl_diag_contains_only(character)
    
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
    
    def is_winner(self) -> bool:
        return self.board.is_winner(self.character)

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
        if player_x.is_winner():
            print("Player X wins!")
            break
        player_o = HumanPlayer("O", game)
        player_o.decide_move(game)
        game.display()
        if player_o.is_winner():
            print("Player O wins!")
            break


if __name__ == "__main__":
    main()
