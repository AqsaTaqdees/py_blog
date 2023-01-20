import pygame
import random

# Initializing all the modules in pygame
pygame.init()
clock = pygame.time.Clock()  # Clock is used for changing the speed of game which will call in the main part of loop
# Setting Display
DISPLAY_SCREEN = pygame.display.set_mode((1000, 710))
# Setting Background
BACKGROUND_IMAGE = pygame.image.load('C:/Users/Administrator/OneDrive/Pictures/Saved Pictures/flappybird_bg.jpg')

# BIRD
BIRD_IMAGE = pygame.image.load('C:/Users/Administrator/OneDrive/Pictures/Saved Pictures/flappybird_icon.png')
# Fixing x and y coordinates of placing the bird
bird_x = 50
bird_y = 300
'''We are not going to be moving the x coordinates because the bird either moves up or down so, changing here
the y coordinates'''
bird_y_change = 0


# Drawing the bird on screen
def display_bird(x, y):
    DISPLAY_SCREEN.blit(BIRD_IMAGE, (x, y))


# OBSTACLES
OBSTACLE_WIDTH = 70  # Setting the width of obstacle to 70px
OBSTACLE_HEIGHT = random.randint(150, 450)  # Setting the height of top obstacle by importing random package (for first iteration)
OBSTACLE_COLOR = (211, 253, 117)  # Set the color of obstacle
OBSTACLE_X_CHANGE = -4  # Obstacle starts from right side, and it will move towards 0(left) so place the -ve value here
obstacle_x = 500  # This 500 is the x position on the right side so the obstacle will start from corner right position
obstacle_gap = 150


def display_obstacle(height):
    # Drawing the top obstacle (start drawing obstacle from the top boundary position i.e. 0 & it comes downwards)
    # height here comes from the above OBSTACLE_HEIGHT parameter where height could be anything from 150 to 450
    pygame.draw.rect(DISPLAY_SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    '''Calculating the height of bottom obstacle by subtracting the height from the bottom to upper boundary to the 
       height of top obstacle & 150. Here 150 is the gap left between both obstacles which will be same for all obstacles'''
    bottom_obstacle_height = 635 - height - obstacle_gap
    '''Drawing the bottom obstacle (start drawing obstacle from the bottom boundary position i.e. 635 & it moves upwards 
       so obstacle_height here is -ve)'''
    # pygame.draw.rect(DISPLAY_SCREEN, OBSTACLE_COLOR, (obstacle_x, height + obstacle_gap, OBSTACLE_WIDTH, bottom_obstacle_height))
    # pygame.draw.rect(DISPLAY_SCREEN, OBSTACLE_COLOR, (obstacle_x, 635, OBSTACLE_WIDTH, bottom_obstacle_height))
    pygame.draw.rect(DISPLAY_SCREEN, OBSTACLE_COLOR,
                     (obstacle_x, height + obstacle_gap, OBSTACLE_WIDTH, bottom_obstacle_height))


# DETECTING THE COLLISION
def collision_detection(obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64): # at 50 we are starting to draw the bird & bird have width of 64px
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False

# SCORE
score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)  # font language and font size of score

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    DISPLAY_SCREEN.blit(display, (10, 10))


# START SCREEN
startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    # displays: "press space bar to start)
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    DISPLAY_SCREEN.blit(display, (20, 200))
    pygame.display.update()

# GAME OVER SCREEN
# This list will hold all the scores
score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)


def game_over():
    # check for the maximum score
    maximum = max(score_list)
    #  "game over"
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    DISPLAY_SCREEN.blit(display1, (50, 300))
    # shows your current score and your max score
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    DISPLAY_SCREEN.blit(display2, (50, 400))
    #  If your new score is the same as the maximum then u reached a new high score
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200, 35, 35))
        DISPLAY_SCREEN.blit(display3, (80, 100))


run = True
# waiting is going to refer to our end or start screen
waiting = True
# set collision to false in the beginning so that we only see the start screen in the beginning
collision = False
while run:
    DISPLAY_SCREEN.fill((0, 0, 0))  # Filling the screen here with rgb_color black
    # blit draws whatever you wanna draw; here (0,0) means it's gonna drawing on the top left corner and then covers the whole screen
    DISPLAY_SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    # we will be sent into this while loop at the beginning and ending of each game
    clock.tick(60)  # Setting the speed of our game
    while waiting:
        if collision:
            # If collision is True (from the second time onwards) we will see both the end screen and the start screen
            game_over()
            start()
        else:
            # This refers to the first time the player is starting the game
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #  If we press the space bar we will exit out of the waiting while loop and start to play the game
                    # we will also reset some of the variables such as the score and the bird's Y position and the obstacle's starting position
                    score = 0
                    bird_y = 300
                    obstacle_x = 500
                    #  to exit out of the while loop
                    waiting = False
            if event.type == pygame.QUIT:
                # in case we exit make both running and waiting false
                waiting = False
                run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If you press exit you will out of while loop and the game quits
            run = False

        # If we press the space bar this event is called & the bird move upward towards the y_change which is 0.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -6

        # If we release the space bar this event is called & the bird move downward away from y_change which is 0.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 3

    # moving the bird vertically
    bird_y += bird_y_change  # Adding the change in y
    if bird_y <= 0:  # 0 is the top most boundary to set for the bird if it goes up; so it can't fly above that boundary
        bird_y = 0
    if bird_y >= 515:  # 515 is the bottom boundary to set for the bird if it goes down
        bird_y = 515

    # To show obstacles continuously
    obstacle_x += OBSTACLE_X_CHANGE  # By doing this the obstacle starts moving
    # COLLISION
    # add 150 to the top obstacle height to get bottom obstacle height
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 150)
    if collision:
        # if a collision does occur we are going to add that score to our list of scores and make waiting True
        score_list.append(score)
        waiting = True
    # generating new obstacles
    if obstacle_x <= -10:  # Resetting the x value and generate new obstacle height because if once the old obstacle
        # reaches the most left side it can disappear & new obstacle with new height can show on screen
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1
    display_obstacle(OBSTACLE_HEIGHT)  # Display here obstacle with new height

    display_bird(bird_x, bird_y)  # Calling the function
    score_display(score)  # display the score
    # Updating the display after each iteration of while loop
    pygame.display.update()

# Quit the program
pygame.quit()
