import pygame



class game:
    def __init__(self) -> None:
        pygame.init()

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

        self.border_color = (0, 255, 0)
        self.border_array = []








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
                self.drawer()

            pygame.display.flip()

        pygame.quit()

    def drawer(self):
        self.screen.fill((255, 253, 208))
        if self.begin:
            self.screen.blit(self.title1, self.title_rect)
            self.screen.blit(self.title2, self.title_rect2)
        for i in self.border_array:
            pygame.draw.rect(self.screen, self.border_color, i)

    


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
                if event.type == pygame.K_RIGHT:
                    #right
                    pass
                if event.type == pygame.K_LEFT:
                    #left
                    pass
                if event.type == pygame.K_UP:
                    #up
                    pass
                if event.type == pygame.K_DOWN:
                    #down
                    pass
    



    def start(self):
        pass


class snake(pygame.sprite.Sprite):
    def __init__(self, arr):
        pass


class apple(pygame.sprite.Sprite):
    def __init__(self, screen, rect) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.rect = rect


    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)






if __name__ == "__main__":
    game()