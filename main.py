from turtle import up
import pygame
import sys

#General Setup
pygame.init()
clock = pygame.time.Clock()

FPS = 60
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")

PADDLE_WIDTH, PADDLE_HEIGHT = 20,100

#COLORS

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win,self.COLOR, (self.x,self.y,self.width,self.height))

    
    def move(self, up = True):
        if up:
            self.y -= self.VEL

        else:
            self.y += self.VEL    




def draw_window(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
         paddle.draw(win)
    
    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

     


def main():
    run = True

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH,PADDLE_HEIGHT)


    while run:
        draw_window(WIN,[left_paddle,right_paddle])
        clock.tick(FPS)
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
        

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
                




if __name__ == "__main__":
    main()

