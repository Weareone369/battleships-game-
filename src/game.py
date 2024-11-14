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

    def _place_ships(self, grid): 
        """ Randomly place ships on the grid. For simplicity, each ship is 3 cells long. """ 
        ship_lengths = [3, 2] # Example ship sizes 
        for length in ship_lengths: 
            while True: 
                start_x = random.randint(0, grid.size - 1) 
                start_y = random.randint(0, grid.size - 1) 
                orientation = random.choice(['H', 'V']) 
                if orientation == 'H': 
                    ship = [(start_x, start_y + i) for i in range(length)] 
                else: ship = [(start_x + i, start_y) for i in range(length)] 
                
                try: 
                    break 
                    except ValueError: 
                        continue 
                        