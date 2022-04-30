##
# Llama Dodge
# A game where you are to escape the llama spit at all costs, or die.
# @author Gangadhar Chinta
# @course ICS3UC
# @date 2021/12/03 - LastModified
###

## Pygame setup
import pygame
import random

##Sprites

#Create sprite for boundaries
class Boundary(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):

        # Call the parent class
        super().__init__()

        # Create an image of the player and fill in
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        #Set values of rect.x and rect.y
        self.rect = self.image.get_rect()

        ##Attributes
        self.rect.x = x
        self.rect.y = y

#Create sprite for llama
class Llama(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
 
        # Call the parent class
        super().__init__()
 
        # Load the image of the llama
        self.image = pygame.image.load("Llama.png").convert()
 
        #Set values of rect.x and rect.y
        self.rect = self.image.get_rect()

        ##Attributes
        self.rect.x = x
        self.rect.y = y

#Create sprite for spit
class Spit(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
 
        # Call the parent class
        super().__init__()
 
        # Create an image of the block and fill in
        self.image = pygame.Surface([5, 5])
        self.image.fill(WHITE)
 
        #Set values of rect.x and rect.y
        self.rect = self.image.get_rect()

        ##Attributes
        self.rect.x = x
        self.rect.y = y
        self.changeY = 0

    def update(self):
        self.rect.y = self.rect.y + self.changeY

#Create sprite for platform
class Platform(pygame.sprite.Sprite):
    
    def __init__(self, x, y):

        # Call the parent class
        super().__init__()

        # Create an image of the platform and fill in
        self.image = pygame.Surface([50, 25])
        self.image.fill(BROWN)

        #Set values of rect.x and rect.y
        self.rect = self.image.get_rect()

        ##Attributes
        self.rect.x = x
        self.rect.y = y

#Create sprite for player
#Taken from http://programarcadegames.com/
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):

        # Call the parent class
        super().__init__()

        # Create an image of the player and fill in
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        #Set values of rect.x and rect.y
        self.rect = self.image.get_rect()

        ##Attributes
        self.rect.x = x
        self.rect.y = y
        self.changeX = 0
        self.changeY = 0
        self.changeSpeedY = 0

    #Move player
    def update(self):
        self.changeY += self.changeSpeedY
        self.rect.x = self.rect.x + self.changeX
        self.rect.y = self.rect.y + self.changeY

#Create sprite for instructions
class InstructionsScene(pygame.sprite.Sprite):
    
    def __init__(self):

        # Call the parent class
        super().__init__()

        # Create an image of the player and fill in
        self.image = pygame.Surface([600, 400])
        self.image.fill(BROWN)

        #Set values of rect.x and rect.y
        self.rect = self.image.get_rect()

        ##Attributes
        self.rect.x = 0
        self.rect.y = 0

#Setting up pygame
#Taken from Mr. Reid
pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Llama Dodge")

## MODEL - Data use in system
# Define some colors
#Taken from Mr. Reid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (122, 1, 15)

#Defining font
font = pygame.font.SysFont('Calibri', 25, True, False)

#Creating groups of sprites
allSpritesList = pygame.sprite.Group()
platformTwoList = pygame.sprite.Group()
llamaTwoList = pygame.sprite.Group()
platformThreeList = pygame.sprite.Group()
llamaThreeList = pygame.sprite.Group()
platformFourList = pygame.sprite.Group()
llamaFourList = pygame.sprite.Group()
platformFiveList = pygame.sprite.Group()
llamaFiveList = pygame.sprite.Group()
currentPlatformList = pygame.sprite.Group()
currentLlamaList = pygame.sprite.Group()
playerList = pygame.sprite.Group()
boundaryList = pygame.sprite.Group()
spitList = pygame.sprite.Group()
sceneList = pygame.sprite.Group()

#Adding boundaries to boundary and all sprites group
leftBoundary = Boundary(-25, 0, 5, 400)
rightBoundary = Boundary(620, 0, 5, 400)
upBoundary = Boundary(0, 75, 600, 10)
downBoundary = Boundary(0, 350, 600, 10)
boundaryList.add(leftBoundary)
boundaryList.add(rightBoundary)
boundaryList.add(upBoundary)
boundaryList.add(downBoundary)
allSpritesList.add(leftBoundary)
allSpritesList.add(rightBoundary)
allSpritesList.add(upBoundary)
allSpritesList.add(downBoundary)

#Creating platforms and llamas for when there are 2
for i in range(2):
    platform = Platform(150+300*i, 300)
    llama = Llama(140+300*i, 75)
    platformTwoList.add(platform)
    llamaTwoList.add(llama)

#Creating platforms and llamas for when there are 3
for j in range(3):
    platform = Platform(150+150*j, 300)
    llama = Llama(140+150*j, 75)
    platformThreeList.add(platform)
    llamaThreeList.add(llama)

#Creating platforms and llamas for when there are 4
for k in range(4):
    platform = Platform(120+120*k, 300)
    llama = Llama(110+120*k, 75)
    platformFourList.add(platform)
    llamaFourList.add(llama)

#Creating platforms and llamas for when there are 5
for l in range(5):
    platform = Platform(100+100*l, 300)
    llama = Llama(90+100*l, 75)
    platformFiveList.add(platform)
    llamaFiveList.add(llama)

#Adding current platform groups and llama groups to all sprites group and current platform group and current llama group
allSpritesList.add(platformTwoList)
allSpritesList.add(llamaTwoList)
currentPlatformList.add(platformTwoList)
currentLlamaList.add(llamaTwoList)

#Adding player to all sprites group
player = Player(165, 280)
playerList.add(player)
allSpritesList.add(playerList)

#Creating Instructions Scene and condition to use it
gameOverInstructions = InstructionsScene()
sceneList.add(gameOverInstructions)
gameOver = False
instructionsShow = True

#Setting up restart
restart = False

#Setting up starting platform count
platformCount = 2

#Setting score to 0
score = 0
highScore = 0

#Setting up loop count in order to decrease time for spit
spitLoopCount = 0

#Setting up how much time it takes for each spit to come
spitTime = 1000

#Setting up spit speed
spitSpeed = 2

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Setting up counter to multiply pltforms
#Idea came from Mr. Reid
pygame.time.set_timer(pygame.USEREVENT, 7000, True)
countDown = 3

#Setting up counter to continuously spit
pygame.time.set_timer(pygame.USEREVENT+1, 1000, True)

## Main Program Loop
while not done:

    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #Moving player if the left and right arrow keys are pressed or the a and d keys are pressed
        elif event.type == pygame.KEYDOWN:

            #Only moving player id game is not over
            if (gameOver == False): 
                if (event.key == pygame.K_RIGHT):

                    #Changing speed of player based on number of platforms
                    if (len(currentPlatformList) == 2):
                        player.changeX = 10
                        player.changeY = -5
                    elif (len(currentPlatformList) == 3 or len(currentPlatformList) == 4):
                        player.changeX = 5
                        player.changeY = -5
                    elif (len(currentPlatformList) == 5):
                        player.changeX = 3.5
                        player.changeY = -5

                    #Idea of changing speed for gravity came from Mr. Reid's more demos
                    player.changeSpeedY = 0.4
                elif (event.key == pygame.K_LEFT):
                    if (len(currentPlatformList) == 2):
                        player.changeX = -10
                        player.changeY = -5
                    elif (len(currentPlatformList) == 3 or len(currentPlatformList) == 4):
                        player.changeX = -5
                        player.changeY = -5
                    elif (len(currentPlatformList) == 5):
                        player.changeX = -3.5
                        player.changeY = -5
                    player.changeSpeedY = 0.4
                if (event.key == pygame.K_d):
                    if (len(currentPlatformList) == 2):
                        player.changeX = 10
                        player.changeY = -5
                    elif (len(currentPlatformList) == 3 or len(currentPlatformList) == 4):
                        player.changeX = 5
                        player.changeY = -5
                    elif (len(currentPlatformList) == 5):
                        player.changeX = 3.5
                        player.changeY = -5
                    player.changeSpeedY = 0.4
                elif (event.key == pygame.K_a):
                    if (len(currentPlatformList) == 2):
                        player.changeX = -10
                        player.changeY = -5
                    elif (len(currentPlatformList) == 3 or len(currentPlatformList) == 4):
                        player.changeX = -5
                        player.changeY = -5
                    elif (len(currentPlatformList) == 5):
                        player.changeX = -3.5
                        player.changeY = -5
                    player.changeSpeedY = 0.4

            #What to do if r key is pressed (restart game if game over)
            if (event.key == pygame.K_r):
                gameOver = False
                instructionsShow = False
                restart = True

        #Setting up user event
        #Idea came from Mr. Reid
        elif event.type == pygame.USEREVENT:
            
            #Setting up to remove spiut every time platform and llama number increases
            if (len(currentPlatformList) < 5):
                allSpritesList.remove(spitList)
                spitList.empty()

            #Increasing number of platforms and llamas to three if there are 2 right now
            if (platformCount == 2):
                platformCount += 1
                allSpritesList.remove(platformTwoList)
                allSpritesList.add(platformThreeList)
                allSpritesList.remove(llamaTwoList)
                allSpritesList.add(llamaThreeList)
                currentPlatformList.remove(platformTwoList)
                currentPlatformList.add(platformThreeList)
                currentLlamaList.remove(llamaTwoList)
                currentLlamaList.add(llamaThreeList)
            
            #Increasing number of platforms and llamas to three if there are 3 right now
            elif (platformCount == 3):
                platformCount += 1
                allSpritesList.remove(platformThreeList)
                allSpritesList.add(platformFourList)
                allSpritesList.remove(llamaThreeList)
                allSpritesList.add(llamaFourList)
                currentPlatformList.remove(platformThreeList)
                currentPlatformList.add(platformFourList)
                currentLlamaList.remove(llamaThreeList)
                currentLlamaList.add(llamaFourList)

            #Increasing number of platforms and llamas to three if there are 4 right now
            elif (platformCount == 4):
                platformCount += 1
                allSpritesList.remove(platformFourList)
                allSpritesList.add(platformFiveList)
                allSpritesList.remove(llamaFourList)
                allSpritesList.add(llamaFiveList)
                currentPlatformList.remove(platformFourList)
                currentPlatformList.add(platformFiveList)
                currentLlamaList.remove(llamaFourList)
                currentLlamaList.add(llamaFiveList)
            
            #Setting up new player position every time platform and llama number increases
            if (platformCount == 2):
                player.rect.x = 165
                player.rect.y = 300
            elif (platformCount == 3):
                player.rect.x = 165
                player.rect.y = 300
            elif (platformCount == 4):
                player.rect.x = 135
                player.rect.y = 300
            elif (platformCount == 5):
                player.rect.x = 115
                player.rect.y = 300

            #Counting down till number of platforms and llamas is 5
            if (countDown>0):
                countDown -= 1

                # Reset the timer
                pygame.time.set_timer(pygame.USEREVENT, 7000, True)

        #Setting up user event
        elif event.type == pygame.USEREVENT+1:

            #Increasing score if game is being played
            if (gameOver == False and instructionsShow == False):
                score += 10

            #Going through each llama in current llama group
            for llamas in currentLlamaList:

                #Choosing random number
                spitLlama = random.randrange(1, 4)
                
                #If random number chosen is 1 make spit come from that llama
                if (spitLlama == 1):

                    #Defining spit
                    spit = Spit(-5, -5)
                    spit.rect.x = llamas.rect.x + 30
                    spit.rect.y = llamas.rect.y + 10
                    spit.changeY = spitSpeed
                    
                    #Increasing spit speed
                    spitSpeed += 0.1

                    #Increasing spit loop count
                    spitLoopCount += 1

                    #Adding spit to groups
                    spitList.add(spit)
                    allSpritesList.add(spit)

            #Checking if spit loop count is 35 and decreasing time between each spit accoringly   
            if (spitLoopCount>35):
                spitTime = 500
                
            #Checking if spit loop count is 35 and decreasing time between each spit accordingly   
            if (spitLoopCount>70):
                spitTime = 250

            # Reset the timer
            pygame.time.set_timer(pygame.USEREVENT+1, spitTime, True)

    # Game logic

    #Checking if user chose to restart
    if (restart == True):

        #Restarting everything
        platformCount = 2
        score = 0
        spitLoopCount = 0
        spitTime = 1000
        spitSpeed = 2
        pygame.time.set_timer(pygame.USEREVENT, 7000, True)
        countDown = 3
        pygame.time.set_timer(pygame.USEREVENT+1, 1000, True)
        allSpritesList.empty()
        currentPlatformList.empty()
        currentLlamaList.empty()
        allSpritesList.add(boundaryList)
        allSpritesList.add(platformTwoList)
        allSpritesList.add(llamaTwoList)
        currentPlatformList.add(platformTwoList)
        currentLlamaList.add(llamaTwoList)
        player.rect.x = 165
        player.rect.y = 280
        allSpritesList.add(playerList)
        collidedPlatformList = []
        boundaryCollision = []
        spitBoundaryCollision = []
        spitPlayerCollision = []
        gameOver = False
        restart = False

    #Updating all sprites group
    allSpritesList.update()

    #Checking for collisions
    #Taken from program arcade games
    collidedPlatformList = pygame.sprite.spritecollide(player, currentPlatformList, False)
    boundaryCollision = pygame.sprite.spritecollide(player, boundaryList, False)
    spitBoundaryCollision = pygame.sprite.spritecollide(downBoundary, spitList, True)
    spitPlayerCollision = pygame.sprite.spritecollide(player, spitList, True)

    #Checking if player landed on platform and placing player on platform accordingly
    if (len(collidedPlatformList) > 0):
        for collidedPlatforms in collidedPlatformList:
            player.rect.x = collidedPlatforms.rect.x + 15
            player.rect.y = 280
            player.changeY = 0
            player.changeX = 0
            player. changeSpeedY = 0
            collidedPlatformList.remove(collidedPlatforms)
    
    #Checking if player hit boundary and setting game over accordingly
    if (len(boundaryCollision) > 0):
        gameOver = True
        instructionsShow = True
    
    ##Cheking if spit hit player and setting game over accordingly
    if (len(spitPlayerCollision) > 0):
        gameOver = True
        instructionsShow = True

    #Setting up score text to be displayed on screen
    #Came from programarcadegames.com
    numberScoreText = font.render(str(score),True,BLACK)
    scoreText = font.render("SCORE:",True,BLACK) 

    ## VIEW
    # Clear screen
    screen.fill(WHITE)

    #Draw background
    pygame.draw.rect(screen, GREEN, [0, 75, 600, 325])
    pygame.draw.rect(screen, BLUE, [0, 0, 600, 75])

    #Draw all sprites
    allSpritesList.draw(screen)

    #Cheking if instructions should show is true
    if (instructionsShow == True):

        #Emptying all sprties
        allSpritesList.empty()

        #Drawing game over screen
        sceneList.draw(screen)
        gameOverText = font.render("Game Over:",True,BLACK)
        controlsText = font.render("- Use the arrow keys to move",True,BLACK)
        instructionsText = font.render("- Don't go too far left, right, up or down",True,BLACK)
        instructionsTextTwo = font.render("- Don't get hit by spit",True,BLACK)
        instructionsTextThree = font.render("- You can jump an unlimited amount of times",True,BLACK)
        instructionsTextFour = font.render("- Have Fun!",True,BLACK)
        restartText = font.render("Press r to restart",True,BLACK)
        startText = font.render("Press r to start",True,BLACK)


        #Wrinting game over if game is over
        if (gameOver == True):
            screen.blit(gameOverText, [250, 50])

        screen.blit(controlsText, [100, 100])
        screen.blit(instructionsText, [50, 150])
        screen.blit(instructionsTextTwo, [50, 200])
        screen.blit(instructionsTextThree, [5, 250])
        screen.blit(instructionsTextFour, [250, 300])

        #showing either start or restart depending on situation
        if (gameOver == True):
            screen.blit(restartText, [200, 350])
        else:
            screen.blit(startText, [200, 350])

        #Checking if current score is greater than the high score
        if (score > highScore):

            #Assigning current score to high score
            highScore = score

    #Setting up high score to show on screen
    numberHighScoreText = font.render(str(highScore),True,BLACK)
    highScoreText = font.render("HI-SCORE:",True,BLACK) 

    #Showing score text and high score text on screen
    screen.blit(numberScoreText, [150, 50])
    screen.blit(scoreText, [110, 25])
    screen.blit(numberHighScoreText, [470, 50])
    screen.blit(highScoreText, [410, 25])

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()