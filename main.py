import pygame
import random 
import math
from pygame import mixer 


#initialize the pygame
pygame.init()

# create the screen
screen= pygame.display.set_mode((800, 600))


# Title and ICON
pygame.display.set_caption("Space Invader By(Mayurzark)")

icon= pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#Background
background=pygame.image.load("background.jpg")

#Background music
mixer.music.load("background.wav")
mixer.music.play(-1)


#Player
playerimg=pygame.image.load("startup.png")
playerX= 375
playerY= 480
playerX_change=0

#enemy
enemyimg=[]
enemyX= []
enemyY=[]

enemyX_change=[]
enemyY_change=[]
num_of_enemies=5
for i in range  (num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append( random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(50)
    
#game over 
game_over_font=pygame.font.Font("freesansbold.ttf",80)

#score
score=0
font=pygame.font.Font("freesansbold.ttf",32)

textX=10
textY=10
    

#ready--> You can't see the bullet
#fire--> you can see the bullet
bulletimg=pygame.image.load("bullet.png")
bulletX= 0
bulletY= 480
bulletX_change=0
bulletY_change=1
bullet_state="ready"
def show_score(x,y):
    score_=font.render("Score : "+str(score),True,(254,234,253))
    screen.blit(score_,(x,y))
    

def player(X,Y):
    screen.blit(playerimg,(X,Y))
    
def enemy (X,Y,i):
    screen.blit(enemyimg[i],(X,Y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x + 20 ,y + 10 ))

def Collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2 + (enemyY-bulletY)**2)
    if distance < 25:
        return True
def game_over_text():
    game_over=game_over_font.render("GAME OVER",True,(255,104,30))
    screen.blit(game_over,(160,200))
    
# Game Loop
running =True

while running:
    # RGB screen
    screen.fill((0,140,240))
    
    #load Background 
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            
        #If keystroke is press whether its right or left
        if event.type==pygame.KEYDOWN:
            print("key is pressed")
            if event.key==pygame.K_LEFT:
                playerX_change=-0.4
            if event.key==pygame.K_RIGHT:
                playerX_change=0.4
            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
                    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
        
    # if playerX > 0 and playerX < 374:
    # checking for the boundaries so it doesn't go out of bound.      
    playerX+=playerX_change
    if playerX > 736:
        playerX=736
    if playerX <= 0:
        playerX=0
    
    
    #Enemy movement
    for i in range (num_of_enemies):
        #Game over
        if enemyY[i] > 480:
            for j in range (num_of_enemies):
                enemyY[j]=1000
            game_over_text()
            bulletY_change=0
            
            break
            
            
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<0 or enemyX[i]>736:
                enemyY[i]+=100
                print(enemyY[i])
        if enemyX[i] > 736:
                enemyX_change[i]=-0.3
        if enemyX[i] <= 0:
                enemyX_change[i]=0.3
        
        
        #Collision 
    
        collision=Collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosive_sound=mixer.Sound("explosion.wav")
            explosive_sound.play()
            score+=1
            bulletY=480
            bullet_state="ready"
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50, 150)
        enemy(enemyX[i],enemyY[i],i)
            
    #Bullete movement
    if bulletY <=0:
        bulletY= 480
        bullet_state = "ready" 
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change
    
        
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()  
        
    
        
    
    
        
        
                
        
            
            
           
        
           
    

    
        
        
    
    
    
    
    
    
    

        
    
    
        
        
        
    
    
