import pygame

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen, size,  pos):
        pygame.sprite.Sprite.__init__(self)
        self.start_pos = pos
        self.size = size
        self.screen = screen
        self.snake_head = pygame.Rect(self.start_pos, (self.size, self.size))

        self.start_tail1 = pygame.Rect(self.start_pos, (self.size, self.size))
        self.start_tail2 = pygame.Rect(self.start_pos, (self.size, self.size))

        self.start_tail1.y = self.start_tail1.y + self.size
        self.start_tail2.y = self.start_tail1.y + self.size
        self.head_color = (51, 0, 0)
        self.tail_color = (102, 51, 0)
        self.snake_arr = [self.snake_head, self.start_tail1, self.start_tail2]
        self.length = 1

    def collision(self):
        if self.snake_arr[0].left < 0 or self.snake_arr[0].right > self.screen.get_width() or self.snake_arr[0].top < 0 or self.snake_arr[0].bottom > self.screen.get_height():
            return True
        for segment in self.snake_arr[1:]:
            if self.snake_arr[0].colliderect(segment):
                return True
        return False


    def draw(self):
        for i, el in enumerate(self.snake_arr):
            if i == 0:
                pygame.draw.rect(self.screen, self.head_color, el)
            else:
                pygame.draw.rect(self.screen, self.tail_color, el)

    def grow(self):
        tail_end = self.snake_arr[-1]
        new_segment = pygame.Rect(tail_end.left, tail_end.top, self.size, self.size)
        self.snake_arr.append(new_segment)
    
    def movement(self, direction):
        self.snake_arr.pop()
        self.snake_arr.insert(0, pygame.Rect((self.snake_arr[0].left + direction[0]*self.size, self.snake_arr[0].top + direction[1]*self.size), (self.size, self.size)))
