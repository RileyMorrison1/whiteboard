import pygame
from pygame.locals import *

pygame.init()

#Determines the initial size of the screen.
x, y = 1280, 720

screen = pygame.display.set_mode((x, y), pygame.RESIZABLE)

# Determines the size of the brush.
brush_size = 5

# Determines the initial colour of the brush.
colour = "black"

running = True

# Sets the name of the window.
pygame.display.set_caption("Whiteboard App")

# Sets the initial colour of the screen
screen.fill("white")

# change_colour command changes the colour.
def change_colour(sl_colour):
    global colour 
    colour = sl_colour
    
# adjust_size command changes the size of the brush.
def adjust_size(up_down):
    global brush_size
    # up_down variable is used to determine if increasing, or decreasing.
    if up_down:
        brush_size += 5

    else:

        if brush_size > 5:
            brush_size -= 5

    pygame.time.wait(200)

# clear function erases everything on the screen.
def clear(clear_colour):
	screen.fill(clear_colour)

# button function creates a button, based on the parameters used.
def button(x_position, y_position, radius, bg_colour="black", hl_colour="white", sl_colour="blue", function=print, function_variable="No Variable"):
    
    button_colour = bg_colour
    if ((pygame.mouse.get_pos()[0] > x_position - radius) & (pygame.mouse.get_pos()[0] < x_position + radius)):
        if ((pygame.mouse.get_pos()[1] > y_position - radius) & (pygame.mouse.get_pos()[1] < y_position + radius)):
            button_colour = hl_colour
            if pygame.mouse.get_pressed()[0]:
                button_colour = sl_colour
                function(function_variable)

    else:
        button_colour = bg_colour
    pygame.draw.circle(screen, button_colour, (x_position, y_position), radius)
    
# user_interface function creates and refreshes the user interface.
def user_interface(width):
    pygame.draw.rect(screen, "teal", pygame.Rect(0, 0, width, y))
    button(25, 50, 17.5, "black", "gray8", "gray10", adjust_size, False)
    button(75, 50, 17.5 , "black", "gray8", "gray10", adjust_size, True)
    button(50, 190, 30, "red", "red3", "red4", change_colour, "red")
    button(50, 260, 30, "blue", "blue3", "blue4", change_colour, "blue")
    button(50, 330, 30, "green", "green3", "green4", change_colour, "green")
    button(50, 400, 30, "yellow", "yellow3", "yellow4", change_colour, "yellow")
    button(50, 470, 30, "purple", "purple3", "purple4", change_colour, "purple")
    button(50, 540, 30, "black", "gray8", "gray10", change_colour, "black")
    button(25, 610, 17.5, "red", "red3", "red4", clear, "white")

while running:
    screen_info = pygame.display.Info()
    x = screen_info.current_w
    y = screen_info.current_h

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        

        if event.type == VIDEORESIZE:
            screen.fill("white")


        if event.type == pygame.KEYDOWN:

            # If the backspace key is pressed erase the whiteboard.
            if event.key == pygame.K_BACKSPACE:
                screen.fill("white")


            # Increases the brush size if the '0' key is pressed.
            if event.key == pygame.K_0:
                brush_size += 5

            # Decreases the brush size if the '9' key is pressed.
            if event.key == pygame.K_9:
                if brush_size > 5:
                    brush_size -= 5
            
            # Takes a screen shot if the '1' key is pressed.
            if event.key == pygame.K_1:
                pygame.image.save(screen, "screenshot.png")
                print("Screenshot taken")

            # Changes the brush colour to white if the 'w' key is pressed.
            if event.key == pygame.K_w:
                colour = "white"

            # Changes the brush colour to blue if the 'b' key is pressed.
            if event.key == pygame.K_b:
                colour = "blue"

            # Changes the brush colour to black if the 'd' key is pressed.
            if event.key == pygame.K_d:
                colour = "black"

            # Changes the brush colour to purple if the 'p' key is pressed.
            if event.key == pygame.K_p:
                colour = "purple"

            # Changes the brush colour to red if the 'r' key is pressed.
            if event.key == pygame.K_r:
                colour = "red"

            # Changes the brush colour to green if the 'g' key is pressed.
            if event.key == pygame.K_g:
                colour = "green"

            #Changes the brush colour to yellow if the 'y' key is pressed.
            if event.key == pygame.K_y:
                colour = "yellow"

    # Detects if the mouse is on the whiteboard.
    if (pygame.mouse.get_pos()[0] > 100):
        # Draw to whiteboard if the primary mouse key is pressed.
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, colour, pygame.mouse.get_pos(), brush_size)

        # Erase to whiteboard if the secondary mouse key is pressed.
        elif pygame.mouse.get_pressed()[2]:
            pygame.draw.circle(screen, "white", pygame.mouse.get_pos(), brush_size)

    # Refreshes the use interface.
    user_interface(100)
    
    pygame.display.flip()

print("Program terminated")
pygame.quit()
