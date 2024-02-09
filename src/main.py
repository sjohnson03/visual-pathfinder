from window import Window
from nodestatus import NodeStatus


def aSearch(grid):
    pass

w = Window()
if w.setup() == 1:
    grid = w.getGrid()
    aSearch(grid)
