class ScoreBoard:

    def __init__(self, capacity=10):
        
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()

    # Does new entry qualify as a high score?
    # Answer is yes if board not full or score is higher than last entry

    good = self._n < (self._board) or score > self._board[-1].get_score()

    if good:
        self._n < len(self._board):  # No score drops from list
        self._n += 1                # So overall number increases

    
    # Shift lower score rightwar to make room for new entry

    j = self._n - 1
    while j > 0 and self._board[j-1].get_score() < score:
        self._board[j] = self._board[j-1]
        j -= 1
    self._board[j] = entry





