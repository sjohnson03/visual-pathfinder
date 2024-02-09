import pygame
from entry import createEntry
from nodestatus import NodeStatus
from typing import List

BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 800
BLOCKSIZE = 20


        
class Window():
    def __init__(self, grid: List[List[bool]] = [[False for _ in range(WIDTH // BLOCKSIZE)] for _ in range(HEIGHT // BLOCKSIZE)], width=WIDTH, height=HEIGHT,blocksize = 20) -> None:
        self.grid = grid
        self.height = height
        self.width = width
        self.blocksize = blocksize
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = False
    
    def drawGrid(self, grid):
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                rect = pygame.Rect(i * BLOCKSIZE, j *BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
                if grid[i][j] == NodeStatus.START:
                    pygame.draw.rect(self.screen, "blue", rect, 10)
                    continue
                if grid[i][j] == NodeStatus.GOAL:
                    pygame.draw.rect(self.screen, "orange", rect, 10)
                    continue
                if grid[i][j]:
                    pygame.draw.rect(self.screen, "white", rect, 10)
                else:
                    rect = pygame.Rect(i * BLOCKSIZE, j *BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
                    pygame.draw.rect(self.screen, "white", rect, 1)
    
    
    def setup(self) -> int:
        """
        Setup the current window. Will exit after the grid has been setup
        
        Args:
            None
            
        Returns:
                1 - grid has been setup  \n
                2 - application closed
        """
        self.running = True
        (start, end) = createEntry(WIDTH / BLOCKSIZE, HEIGHT / BLOCKSIZE)

        (startX, startY) = start
        self.grid[startX][startY] = NodeStatus.START

        (endX, endY) = end
        self.grid[endX][endY] = NodeStatus.GOAL
        
        while self.running:
            
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                return 1
                
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
    
            x, y = pygame.mouse.get_pos()
            (mousePosX, mousePosY) = (x//BLOCKSIZE, y//BLOCKSIZE)
            (mouse1Pressed, _, _) = pygame.mouse.get_pressed()
            try:
                if not self.grid[mousePosX][mousePosY]:
                    self.grid[mousePosX][mousePosY] = mouse1Pressed
                    self.drawGrid(self.grid)
            except IndexError:
                self.drawGrid(self.grid)

            # flip() the display to put your work on screen
            pygame.display.flip()
        pygame.quit()
        return 2
        
    def getGrid(self) -> List[List[any]]:
        return self.grid