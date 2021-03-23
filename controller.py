class Action():
    def __init__(self, body):
        self.x = int(body['x'])
        self.y = int(body['y'])
        self.color = int(body['color'])

    def as_dict(self):
        as_dict = {}
        as_dict['x'] = self.x
        as_dict['y'] = self.y
        as_dict['color'] = self.color
        return as_dict
        
history = []
grid = [[0 for i in range(30)] for j in range(30)]

def place_pixel(action: Action):
    history.append(action)
    grid[action.x][action.y] = action.color

def get_grid():
    return grid
