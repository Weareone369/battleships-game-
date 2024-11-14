# grid.py 
class Grid: 
    """Handles grid setup, display, and interactions for the Battleships game.""" 

def __init__(self, size): 
    """Initialize the grid with a given size and empty cells.""" 
    self.size = size 
    self.ships = [] 
    self.grid = [['~' for _ in range(size)] for _ in range(size)]