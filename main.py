import numpy as np

class Gameboard:
    def __init__(self, size=3):
        self.max_index = size * size - 1
        self.board = np.arange(size * size).reshape(size, size).astype(str)
        self.char_width = len(str(self.max_index))

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
               self._ur_bl_diag_contains_only(character) or \
               not np.any(np.char.isdigit(self.board))

    def is_tie(self) -> bool:
        """
        Return True if the game is a tie (no empty spaces left).
        """
        return not np.any(np.char.isdigit(self.board))
    
    def is_done(self, character: str) -> bool:
        return self.is_winner(character) or self.is_tie()

    def display(self):
        # format strings so each cell is left-padded to the board's char width
        formatted = np.array2string(
            self.board,
            separator=' ',
            formatter={'str_kind': lambda x: x.rjust(self.char_width)}
        )
        print(formatted)
    
class Player:
    """
    Player class that can be extended for different types of players.
    """
    def __init__(self, character: str, gameboard: Gameboard):
        self.character = character
        self.board = gameboard

    def decide_move(self, gameboard: Gameboard) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    def move_not_available(self) -> bool:
        if self.board.is_tie():
            print("The game is a tie!")
            return True

        if self.board.is_winner(self.character):    
            print(f"Player {self.character} wins!")
            return True
        return False

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

class RandomPlayer(Player):
    """
    Player subclass that randomly tries moves until one succeeds.
    """
    def decide_move(self, gameboard: Gameboard) -> None:
        # if no numeric (available) positions remain, do nothing
        if not np.any(np.char.isdigit(self.board.board)):
            return
        while True:
            pos = np.random.randint(0, self.board.max_index + 1)
            if self.board.make_move(pos, self.character):
                return

def main():
    print("Hello from tic-tac-toe!")
    # prompt for board size
    while True:
        size_in = input("Enter board size (integer >= 3, default 3): ").strip()
        if size_in == "":
            size = 3
            break
        try:
            size = int(size_in)
            if size >= 3:
                break
            print("Please enter an integer >= 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    game = Gameboard(size)

    def choose_player(letter: str):
        while True:
            choice = input(f"Should player {letter} be human or ai? [h/a] (default h): ").strip().lower()
            if choice == "" or choice.startswith("h"):
                return HumanPlayer(letter, game)
            if choice.startswith("a") or choice.startswith("r"):
                return RandomPlayer(letter, game)
            print("Enter 'h' for human or 'a' for ai.")

    player_x = choose_player("X")
    player_o = choose_player("O")
    
    game.display()
    while True:
        
        player_x.decide_move(game)
        game.display()
        if player_x.move_not_available():
            break        

        player_o.decide_move(game)
        game.display()
        if player_o.move_not_available():
            break

if __name__ == "__main__":
    main()
