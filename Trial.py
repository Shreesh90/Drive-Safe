import pygame
import time
import random

pygame.init()

crashSound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("jazz.wav")

# --INITIALISING SCREEN RESOLUTION--
display_width = 800
display_height = 600

# --COLOUR INITIALISATION AS (R,G,B)--
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
darkRed = (150, 0, 0)
darkGreen = (0, 150, 0)
obstacleColour = (168, 238, 21)
crashColour = (85, 234, 255)
orange = (92, 250, 152)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Drive Safe!')  # --SETTING NAME FOR GAME--
clock = pygame.time.Clock()  # --INITIALISING 'clock' VARIABLE USED TO SET GAME SPEED--

introImg = pygame.image.load('IntroImage.jpg')
into_width = 900
intro_height = 600
def IntroImage(x, y):
    gameDisplay.blit(introImg, (x,y))


roadImg = pygame.image.load('RoadStrip.jpg')
def RoadImg(x, y):
    gameDisplay.blit(roadImg, (x, y))

carImg = pygame.image.load('racecar.png')  # --LOADING IMAGE OF CAR IN A VARIABLE--
# --INITIALISING VARIABLES EQUAL TO DIMENSIONS OF IMAGE--
car_width = 77
car_height = 52


# --FUNCTION TO DISPLAY THE IMAGE OF CAR LOADED IN VARIABLE 'carImg'--
def car(x, y):
    gameDisplay.blit(carImg, (x, y))    # -- 'blit' IS USED TO SHOW IMAGE ON SCREEN --


# --FUNCTION TO CALCULATE SCORE --
def score(count):
    font = pygame.font.Font(None, 25)
    text = font.render("Dodged: "+str(count), True, obstacleColour)
    gameDisplay.blit(text, (0, 0))


# --FUNCTION TO DRAW OBSTACLES --
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


# -- FUNCTION RETURNS TEXT AND RECTANGLE OBJECT TO PRINT THEM
def text_objects(text, font, color):
    TextSurface = font.render(text, True, color)
    return TextSurface, TextSurface.get_rect()


def message_display(text, dodged, color):
    largeText = pygame.font.SysFont("elephant", 75)
    dodgeFont = pygame.font.SysFont("elephant", 50)
    TextSurf, TextRect = text_objects(text, largeText, color)  # -- TextSurf(Text to be displayed), TextRect(rectangular box to display Text in it) --
    dodgedSurf, dodgedRect = text_objects(dodged, dodgeFont, color)
    TextRect.center = ((display_width / 2), (display_height / 2))   # -- SETTING POSITION FOR TextRect --
    dodgedRect.center = ((display_width/2), (display_width/2 + 120))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(dodgedSurf, dodgedRect)
    pygame.display.update()
    time.sleep(3)   # -- PAUSE EVERYTHING FOR 2 SECONDS AT THIS COMMAND --
    game_loop()


# -- WHENEVER CRASH OCCURS THIS WILL EXECUTE --
def crash(SCORE, color):
    message_display('You Crashed', "Dodged: " + str(SCORE), color)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == "play":
            #     game_loop()
            # elif action == "quit":
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

    startText = pygame.font.SysFont("elephant", 25)
    startSurf, startRect = text_objects(msg, startText, black)
    startRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(startSurf, startRect)


def crashed(SCORE):

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashSound)


    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        IntroImage(0, 0)  # -- TO ADD IMAGE IN BACKGROUND IN INTRO SCREEN --

        # -- DISPLAYING 'You crashed' --
        largeText = pygame.font.SysFont("elephant", 90)
        textSurf, textRect = text_objects("You Crashed!!", largeText, orange)
        textRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(textSurf, textRect)

        # -- DISPLAYING SCORE --
        smallText = pygame.font.SysFont("elephant", 30)
        smallSurf, smallRect = text_objects("Your total score is: " + str(SCORE), smallText, orange)
        smallRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(smallSurf, smallRect)


        # -- FUNCTION CALLING TO CREATE BUTTONS --
        # button(message, x, y, width, height, inactive_colour, active_colour)
        button("Replay", 200, 450, 150, 75, green, darkGreen, game_loop)
        button("Exit", 450, 450, 150, 75, red, darkRed, quit)

        pygame.display.update()


pause = False
def unpause():
    pygame.mixer.music.unpause()
    global pause
    pause = False


def paused(SCORE):

    pygame.mixer.music.pause()
    global pause
    pause = True

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #IntroImage(0, 0)    # -- TO ADD IMAGE IN BACKGROUND IN INTRO SCREEN --

        # -- DISPLAYING 'Game Paused' --
        largeText = pygame.font.SysFont("elephant", 90)
        textSurf, textRect = text_objects("Game Paused", largeText, orange)
        textRect.center = ((display_width/2), (display_height/4))
        gameDisplay.blit(textSurf, textRect)

        # -- DISPLAYING SCORE --
        smallText = pygame.font.SysFont("elephant", 50)
        smallSurf, smallRect = text_objects("Hey coward your Score is: " + str(SCORE), smallText, orange)
        smallRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(smallSurf, smallRect)

        # -- FUNCTION CALLING TO CREATE BUTTONS --
        # button(message, x, y, width, height, inactive_colour, active_colour)
        button("Continue", 200, 450, 150, 75, green, darkGreen, unpause)
        button("Abort!", 450, 450, 150, 75, red, darkRed, quit)

        pygame.display.update()


def game_Intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        IntroImage(0, 0)    # -- TO ADD IMAGE IN BACKGROUND IN INTRO SCREEN --
        largeText = pygame.font.SysFont("elephant", 90)
        textSurf, textRect = text_objects("Quick Drive", largeText, crashColour)
        textRect.center = ((display_width/2), (display_height/4))
        gameDisplay.blit(textSurf, textRect)
        # pygame.draw.circle(gameDisplay, green, (200, 450), 60)
        # pygame.draw.circle(gameDisplay, red, (600,450), 60)

        # -- FUNCTION CALLING TO CREATE BUTTONS --
        # button(message, x, y, width, height, inactive_colour, active_colour)
        button("Start!", 200, 450, 150, 75, green, darkGreen, game_loop)
        button("Exit", 450, 450, 150, 75, red, darkRed, quit)

        pygame.display.update()

        #time.sleep(10)



# --MAIN LOOP WHERE ALL GAME FLOW IS WRITTEN --
def game_loop():

    pygame.mixer.music.play(-1)
    global pause

    # -- SETTING VALUES OF x AND y  WHERE THE CAR SHOULD BE INITIALLY--
    x = display_width * 0.1
    y = display_height * 0.50
    # -- VARIABLES TO CONTAIN CHANGE IN COORDINATES x AND y OF CAR AFTER PRESSING ARROW KEY --
    x_change = 0
    y_change = 0
    # -- SETTING ALL THE PARAMETERS FOR THE OBSTACLE --
    thing_startx = display_width + 600
    thing_starty = random.randrange(0,display_height)
    thing_width = 100
    thing_height = 40
    thing_speed = 5
    SCORE = 0

    # -- VARIABLE THAT WILL HELP BREAK THE LOOP --
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                #gameExit = True
            # print(event) # -- THIS COMMAND WILL HELP PRINT ALL THE EVENTS --

            # -- INSTRUCTION AS TO WHAT WILL HAPPEN IF ARROE KEYS ARE PRESSED --
            if event.type == pygame.KEYDOWN:    # --DEFINING THAT THE TYPE OF EVENT IS PRESSING A KEY --
                if event.key == pygame.K_LEFT:  # -- IF PRESSED KEY IS LEFT ARROW --
                    x_change = -5
                if event.key == pygame.K_RIGHT:   # -- IF PRESSED KEY IS RIGHT ARROW --
                    x_change = 5
                if event.key == pygame.K_UP:  # -- IF PRESSED KEY IS UP ARROW --
                    y_change = -5
                if event.key == pygame.K_DOWN:    # -- IF PRESSED KEY IS DOWN ARROW --
                    y_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused(SCORE)

            # -- INSTRUCTION WHEN PRESSED KEY IS RELEASED --
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        # -- CHANGING THE COORDINATES OF CAR--
        x += x_change
        y += y_change

        RoadImg(0, 0)
        #gameDisplay.fill(green) # -- FILLS BACKGROUND WITH WHITE --
        car(x, y)   # -- FUNCTION CALL TO DISPLAY CAR ON SCREEN --
        score(SCORE)

        # -- PASSING PARAMETERS TO CREATE OBSTACLE --
        # things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, obstacleColour)
        thing_startx -= thing_speed  # -- CHANGING COORDINATE OF THE OBSTACLE EACH TIME AFTER IT IS PRINTED --


        # -- DEFINING BOUNDARY OF SCREEN WHERE CAR WILL CRASH
        if x > display_width - car_width or x < 0:
            # crash(SCORE, crashColour)
            crashed(SCORE)
        elif y > display_height - car_height or y < 0:
            # crash(SCORE, crashColour)
            crashed(SCORE)
        # -- CHANGE OF CONDITIONS TO CREATE ANOTHER OBSTACLE IN DIFFERENT LOCATION --
        if thing_startx < 0-thing_width:
            thing_startx = display_width+thing_width
            thing_starty = random.randrange(0, display_height)
            if thing_speed <= 40:
                thing_speed += 0.5
            SCORE += 1

        # -- CONDITIONS WHEN CAR CRASHES WITH THE OBSTACLE --
        if x+car_width > thing_startx and x+car_width < thing_startx + thing_width or x > thing_startx and x<thing_startx+thing_width:
            if y+car_height > thing_starty and y+car_height < thing_starty+thing_height or y > thing_starty and y < thing_starty+thing_height:
                # crash(SCORE, crashColour)
                crashed(SCORE)
        pygame.display.update()  # -- UPDATING SCREEN AT EVERY STEP AFTER ALL THE INSTRUCTIONS ARE GIVEN --
        clock.tick(100)  # -- 100 frames/sec --


game_Intro()
game_loop()
pygame.quit()
quit()
