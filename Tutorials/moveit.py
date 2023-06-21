import sys, pygame
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ballimg = pygame.image.load("intro_ball.gif")
ballrect = ballimg.get_rect()

class GameObject:
    def __init__(self, image: pygame.Surface, speed: int, pos = (0, 0)) -> None:
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(pos)
    
    # Move the object
    def move(self, up = False, down = False, left = False, right = False):
        if up:
            self.pos.top -= self.speed
        if down:
            self.pos.bottom += self.speed
        if left:
            self.pos.left -= self.speed
        if right:
            self.pos.right += self.speed
        
        # Detect if the object is out of bounds
        if self.pos.bottom < 0:
            self.pos.top = height
        if self.pos.top > height:
            self.pos.bottom = 0
        if self.pos.right < 0:
            self.pos.left = width
        if self.pos.left > width:
            self.pos.right = 0

# Create the ball object
ball = GameObject(ballimg, 5)

# Enter main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if pygame.mouse.get_pressed(num_buttons=3)[0] and ball.pos.collidepoint(pygame.mouse.get_pos()): 
                print("POP!")
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball.move(up=True)
    if keys[pygame.K_DOWN]:
        ball.move(down=True)
    if keys[pygame.K_LEFT]:
        ball.move(left=True)
    if keys[pygame.K_RIGHT]:
        ball.move(right=True)
    
    screen.fill(black)
    screen.blit(ball.image, ball.pos)
    pygame.display.update((screen.get_rect(), ball.image.get_rect()))
    clock.tick(60)
