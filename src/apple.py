import pygame
import random
class Apple(pygame.sprite.Sprite):
    def __init__(self, screen, size, leng, snake) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.issue = True
        self.screen = screen
        self.size = size
        self.len = leng
        

        self.generate(snake)

    def generate(self, snake):
        x = random.randint(1, self.len-1)*self.size
        y = random.randint(1, self.len-1)*self.size
        
        while self.issue:
            for i in snake:
                if(x == i.x):
                    x = random.randint(1, self.len-1)*self.size
                elif(y == i.y):
                    y = random.randint(1, self.len-1)*self.size
                else:
                    self.issue = False
        self.rect = pygame.Rect(x, y, self.size, self.size)
    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)