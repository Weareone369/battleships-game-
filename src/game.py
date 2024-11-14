from grid import Grid 
from player import Player 
import random 

class Game: 
    """Coordinates the overall gameplay between the player and AI opponent.""" 
    
    def __init__(self, grid_size): 
        """Set up the game with grids for both player and AI based on grid size.""" 
        self.player_grid = Grid(grid_size) 
        self.ai_grid = Grid(grid_size) 
        self.player = Player("User", self.player_grid) 
        self.ai = Player("AI", self.ai_grid) 
        
        # Place ships for player and AI 
        self._place_ships(self.player_grid) 
        self._place_ships(self.ai_grid)
        grid.add_ship(ship) 