#'W' eine Wand
# 'P' ein Pellet
# 'G' ein Geist
# '.' einen leeren Raum.
class Level:
    def __init__(self):
        self.grid = [
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'U', 'P', 'P', 'P', 'P', 'P', 'W'],
            ['W', 'P', 'W', 'W', 'P', 'W', 'P', 'W', 'P', 'W', 'W', 'P', 'W', 'P', 'W', 'P', 'W', 'W', 'P', 'W'],
            ['W', 'P', 'P', 'P', 'P', 'W', 'P', 'W', 'P', 'W', 'W', 'P', 'W', 'P', 'W', 'P', 'P', 'P', 'P', 'W'],
            ['W', 'P', 'W', 'W', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'W', 'W', 'P', 'W'],
            ['W', 'P', 'U', 'P', 'P', 'W', 'W', 'G', 'W', 'W', 'P', 'W', 'W', 'G', 'W', 'P', 'P', 'P', 'P', 'W'],
            ['W', 'P', 'W', 'W', 'P', 'W', 'W', 'P', 'W', 'W', 'P', 'W', 'W', 'P', 'W', 'P', 'W', 'W', 'P', 'W'],
            ['W', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        ]
