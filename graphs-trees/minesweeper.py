"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 
'M' represents an unrevealed mine, 
'E' represents an unrevealed empty square, 
'B' represents a revealed blank square that has no adjacent 
(above, below, left, right, and all 4 diagonals) mines, 
('1' to '8') represents how many mines are adjacent to this revealed square, 
'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

"""

from typing import List
from collections import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        revealed, mines = set(), set()
        queue = deque([(click[0], click[1])])
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        while queue and (len(revealed) + len(mines)) <= (len(board) * len(board[0])):
            space = queue.popleft()
            revealed.add(space)
            
            if board[space[0]][space[1]] == "E":
                neighbors, new_mines = self.getNeighbors(space, revealed, board)
                if len(new_mines) == 0:
                    queue.extend(neighbors | new_mines)
                mines |= new_mines
                board[space[0]][space[1]] = str(len(new_mines)) if new_mines else "B" 
            
        return board
                
                
    def getNeighbors(self, space, visited, board):
        dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        r, c = space
        neighbors, mines = set(), set()
        
        for i, j in dirs:
                if (0 <= r+i < len(board)) and (0 <= c+j < len(board[0])):
                    if (r+i,c+j) not in visited:
                        neighbors.add((r+i,c+j))
                    if board[r+i][c+j] == "M":
                        mines.add((r+i,c+j))
        return neighbors, mines


obj = Solution()
out = obj.updateBoard([['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']], [1,2])
print(out) 
"""
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
"""