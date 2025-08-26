import pygame, math, time
from pygame.locals import K_w
pygame.init()
pygame.font.init()
pygame.mixer.init()

def restart():
    global size, begin, switch 
    size = 75
    begin = True 
    ball.x = 127
    if ai == 'no':
      if switch == 0:
        ball.y = 150
      else:
        ball.y = 320
    else:
       switch = 1
       ball.y = 320
    red.x = 125
    red.y = 450
    blue.x = 125
    blue.y = 50
    

SCREEN_WIDTH = 350
SCREEN_HIGHT = 600

ai = 'not_decided'
ai_x = 0

font_large = pygame.font.SysFont(None, 72)

red_score = 0 
blue_score = 0 

start = True 
counter = 0
switch = 0 

font = pygame.font.SysFont(None, 48)

RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)

running = True 
begin = True 

pedal_speed = 5
red_pedal_speed_x = 0
red_pedal_speed_y = 0

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 100
size = 75
width = hight = 75

blue_win_x =1000
red_win_x = 1000

RED = (255, 0, 0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
background = pygame.image.load('./assets/sprites/yellow-background.png').convert_alpha()
red_pedal = pygame.image.load('./assets/sprites/red-pedal.png').convert_alpha()
blue_pedal = pygame.image.load('./assets/sprites/blue-pedal.png').convert_alpha()
table = pygame.image.load('./assets/sprites/table.jpeg').convert_alpha()
ball = pygame.image.load('./assets/sprites/ball.png').convert_alpha()
red_wins = pygame.image.load('./assets/sprites/red_win.PNG').convert_alpha()
blue_wins = pygame.image.load('./assets/sprites/blue_win.PNG').convert_alpha()
ai_screen = pygame.image.load('./assets/sprites/ai?.JPG').convert_alpha()
scaled_red_pedal = pygame.transform.scale(red_pedal, (100, 100))
scaled_blue_pedal = pygame.transform.scale(blue_pedal, (100, 100))
scaled_table = pygame.transform.scale(table, (192, 346))
scaled_ball = pygame.transform.scale(ball, (size, size))
scaled_red = pygame.transform.scale(red_wins, (350, 600))
scaled_blue = pygame.transform.scale(blue_wins, (350, 600))
scaled_ai_screen = pygame.transform.scale(ai_screen, (350, 600))

ping = './assets/audio/ping-pong-64516-[AudioTrimmer.com].mp3'
pong = './assets/audio/ping-pong-64516-[AudioTrimmer.com]-2.mp3'
ding = './assets/audio/ding-101492.mp3'
#dead = './assets/audio/wrong-47985.mp3'
dead = './assets/audio/wronganswer-37702.mp3'
#dead = './assets/audio/oh-no-392258.mp3'
victory = './assets/audio/11l-victory-1749704552668-358772.mp3'
class Red(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        super().__init__() 
        self.x = float(x)
        self.y = float(y)
        self.image = scaled_red_pedal
       
    def update(self):
        pass

class Blue(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        super().__init__() 
        self.x = float(x)
        self.y = float(y)
        self.image = scaled_blue_pedal
       
    def update(self):
        pass

class Ball(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        super().__init__()
        self.x = float(x)
        self.y = float(y) 
        self.speed_x = 4.0
        self.speed_y = 4.0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y


red = Red(125, 450)
blue = Blue(125, 50)
ball = Ball(127, 150) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if red_score or blue_score == 7:
            restart()
            red_win_x = blue_win_x = 1000
            blue_score = 0
            red_score = 0 
    if start == True:
      if keys[pygame.K_y]:
         start = False
         switch = 1
         ai_x = 1000
         ai = 'yes'
         ball.y = 320
      if keys[pygame.K_n]:
         start = False
         ai = 'no'
         ai_x = 1000
    if start == False:
        if keys[pygame.K_UP]:
              red.y -= pedal_speed
        if keys[pygame.K_DOWN]:
              red.y += pedal_speed
        if keys[pygame.K_LEFT]:
              red.x -= pedal_speed
        if keys[pygame.K_RIGHT]:
             red.x += pedal_speed
        if ai == 'no':
             if keys[pygame.K_w]:
                 blue.y -= pedal_speed
             if keys[pygame.K_s]:
                 blue.y += pedal_speed
             if keys[pygame.K_a]:
                blue.x -= pedal_speed
             if keys[pygame.K_d]:
                 blue.x += pedal_speed

    RED_RECT = pygame.Rect(red.x + 35, red.y + 20, 35, 25)
    BLUE_RECT = pygame.Rect(blue.x + 35, blue.y + 55, 35, 25)
    BALL_RECT = pygame.Rect(ball.x + 25, ball.y + 20, 30, 30)

    if ai == 'yes':
       blue.x = ball.x
       switch = 1

    if BALL_RECT.colliderect(RED_RECT):
        pygame.mixer.music.load(ping)
        pygame.mixer.music.play()
        begin = False
        ball.speed_y *= -1 
        center_difference = BALL_RECT.centerx - RED_RECT.centerx
        ball.speed_x = center_difference * 0.1
        ball.y = RED_RECT.top - scaled_ball.get_height()

    if BALL_RECT.colliderect(BLUE_RECT):
        pygame.mixer.music.load(pong)
        pygame.mixer.music.play()
        ball.speed_y *= -1
        begin = False
        center_difference = BALL_RECT.centerx - BLUE_RECT.centerx
        ball.speed_x = center_difference * 0.1
        ball.y = BLUE_RECT.bottom

    if ball.x <= 0 or ball.x >= SCREEN_WIDTH - scaled_ball.get_width():
        ball.speed_x *= -1 
    
    if ball.y <= 0:
        if counter < 3:
          counter += 1
        red_score += 1
        ball.speed_y *= -1
        pygame.mixer.music.load(dead)
        pygame.mixer.music.play()
        time.sleep(1)
        restart()

    if ball.y >= SCREEN_HIGHT - scaled_ball.get_height():
           if counter < 3:
              counter += 1
           blue_score += 1
           ball.speed_y *= -1
           pygame.mixer.music.load(dead)
           pygame.mixer.music.play()
           time.sleep(1)
           pygame.mixer.music.load(ding)
           pygame.mixer.music.play()
           restart()

    if counter == 2:
        if switch == 1:
         switch = 0
        else:
         switch = 1
        counter = 0

    if red_score == 7:
        pygame.mixer.music.load(victory)
        pygame.mixer.music.play()
        red_win_x = 0 

    if blue_score == 7:
       pygame.mixer.music.load(victory)
       pygame.mixer.music.play()
       blue_win_x = 0 

    red.x = max(0, min(red.x, SCREEN_WIDTH - PADDLE_WIDTH))
    red.y = max(320, min(red.y, SCREEN_HIGHT - PADDLE_HEIGHT))

    blue.x = max(0, min(blue.x, SCREEN_WIDTH - PADDLE_WIDTH))
    blue.y = max(0, min(blue.y, 120))
        
    red.update()
    blue.update()
    if not begin:
       ball.update()
 
    screen.blit(background, (0, 0))
    screen.blit(scaled_table, (70, 100))
    screen.blit(scaled_ball, (int(ball.x), int(ball.y)))
    screen.blit(scaled_red_pedal, (int(red.x), int(red.y)))
    screen.blit(scaled_blue_pedal, (int(blue.x), int(blue.y)))
    #pygame.draw.rect(screen, RED, BLUE_RECT, 0)
    #pygame.draw.rect(screen, RED, RED_RECT, 0)
    #pygame.draw.rect(screen, RED, BALL_RECT, 0)
    #text 
    red_score_text = font_large.render(f'{red_score}', True, RED)
    colon_text = font_large.render(':', True, WHITE)
    blue_score_text = font_large.render(f'{blue_score}', True, BLUE)

    red_score_rect = red_score_text.get_rect()
    colon_rect = colon_text.get_rect()
    blue_score_rect = blue_score_text.get_rect()

    total_width = red_score_rect.width + colon_rect.width + blue_score_rect.width
    x_position = (SCREEN_WIDTH - total_width) // 2
    y_position = 10

    red_score_rect.topleft = (x_position, y_position)
    colon_rect.topleft = (red_score_rect.topright[0], y_position)
    blue_score_rect.topleft = (colon_rect.topright[0], y_position)

    screen.blit(red_score_text, red_score_rect)
    screen.blit(colon_text, colon_rect)
    screen.blit(blue_score_text, blue_score_rect)
    screen.blit(scaled_red, (red_win_x, 0))
    screen.blit(scaled_blue, (blue_win_x, 0))
    screen.blit(scaled_ai_screen, (ai_x, 0))
    pygame.display.flip()

    clock.tick(60)

