from enum import Enum

class NodeStatus(Enum):
    START = 1
    GOAL = 2
    EXPLORING = 3
    EXPLORED = 4