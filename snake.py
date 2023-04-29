import pygame
import random



class game:
    def __init__(self) -> None:
        pygame.init()
        #TODO move all this clutter to a settings class
        self.screen_width = 860
        self.screen_height = 860
        self.tile_size = 20
        self.tile_len = 43

        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.font = pygame.font.Font('freesansbold.ttf', 35)
        self.font2 = pygame.font.Font('freesansbold.ttf', 25)
        self.title1 = self.font.render('Snake!', True, (0, 0, 0))
        self.title2 = self.font2.render('Press space to play!', True, (0, 0, 0))
        self.title_rect = self.title1.get_rect()
        self.title_rect2 = self.title2.get_rect()
        self.title_rect.center = (self.screen_width//2, 150)
        self.title_rect2.center = (self.screen_width//2, 200)

        self.border_color = (204, 213, 174)
        self.border_array = []


        self.clock = pygame.time.Clock()

        self.start_pos = (self.tile_len//2*self.tile_size, self.tile_len//2*self.tile_size)
        self.snake = snake(self.screen, self.tile_size, self.start_pos)
        self.apple = apple(self.screen, self.tile_size, self.tile_len, self.snake.snake_arr)
        
        
        self.direction = (0, -1)
        self.begin = True
        self.run = True




        self.border();
        self.main()

  

    def border(self):
        for x in range(0, self.screen_width, self.tile_size):
            for y in range(0, self.screen_height, self.tile_size):
                if(y == 0 or y == self.screen_height-self.tile_size or x == 0 or x == self.screen_width-self.tile_size):
                    self.border_array.append(pygame.Rect(x, y, self.tile_size, self.tile_size))


    def main(self):
        while self.run:
            self.event_handler()
            self.drawer()
            if self.begin:
                self.start()

            else:
                self.snake.movement(self.direction)
                self.drawer()
            
            self.clock.tick(10)
            pygame.display.flip()

        pygame.quit()

    def drawer(self):
        self.screen.fill((255, 253, 208))
        if self.begin:
            self.screen.blit(self.title1, self.title_rect)
            self.screen.blit(self.title2, self.title_rect2)
        for i in self.border_array:
            pygame.draw.rect(self.screen, self.border_color, i)
        self.snake.draw()
        self.apple.draw()

    


    def event_handler(self):
        if self.begin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.begin = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.begin = False
        elif self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.begin = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.direction = (1, 0)
                        print(self.direction)
                    if event.key == pygame.K_LEFT:
                        self.direction = (-1, 0)
                        
                    if event.key == pygame.K_UP:
                        self.direction = (0, -1)
                        
                    if event.key == pygame.K_DOWN:
                        self.direction = (0, 1)

    



    def start(self):
        pass

#TODO move this seperate file
class snake(pygame.sprite.Sprite):
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
        #end game if wall
        #increase length if apple
        pass

    def draw(self):
        for i, el in enumerate(self.snake_arr):
            if i == 0:
                pygame.draw.rect(self.screen, self.head_color, el)
            else:
                pygame.draw.rect(self.screen, self.tail_color, el)
    
    def movement(self, direction):
        self.snake_arr.pop()
        self.snake_arr.insert(0, pygame.Rect((self.snake_arr[0].left + direction[0]*self.size, self.snake_arr[0].top + direction[1]*self.size), (self.size, self.size)))
        

#TODO move this seperate file
class apple(pygame.sprite.Sprite):
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






if __name__ == "__main__":
    game()