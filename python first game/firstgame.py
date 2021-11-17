
import pygame
pygame.init()



win= pygame.display.set_mode((500,500))
pygame.display.set_caption("my first game")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
background= pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock= pygame.time.Clock()

class Player ():
    def __init__(self, x,y, width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.is_jump=False
        self.jump_count=10
        self.left=False
        self.right=False
        self.walk_count=0
        self.standing=True

    def draw(self, win):
        if self.walk_count+1>=27:
            self.walk_count=0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
            elif self.right:
                win.blit(walkRight[self.walk_count//3],(self.x,self.y))
                self.walk_count+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
            

class Projectile():
    def __init__(self,x,y, radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
       








def draw_game():
    win.blit(background,(0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

man=Player(300,425,64,64)
bullets=[]
run=True 

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    for bullet in bullets:
        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(Projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))

    if keys[pygame.K_LEFT] and man.x>man.vel:
            man.x-=man.vel
            man.left=True
            man.right=False
            man.standing=False
    elif keys[pygame.K_RIGHT] and man.x<win.get_width()-man.width-man.vel:
            man.x+=man.vel
            man.right=True
            man.left=False
            man.standing=False
    else:
            man.walk_count=0
            man.standing=True

    

    if not man.is_jump:
        if keys[pygame.K_UP]:
            man.is_jump=True
            man.left=False
            man.right=False
            man.walk_count=0
    else:
        if man.jump_count>=-10:
            neg=1
            if man.jump_count<0:
                neg=-1
            man.y-=(man.jump_count**2)/2*neg
            man.jump_count-=1
        else:
            man.jump_count=10
            man.is_jump=False
    
    draw_game()
    
           

pygame.quit()