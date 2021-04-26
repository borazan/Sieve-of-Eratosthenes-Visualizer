import pygame

pygame.init()

size = [1920, 1080] #set screen size
number_of_pixels = size[0] * size[1]
green = (0, 255, 0) #define colors for later use
red = (255, 0, 0)
screen = pygame.display.set_mode(size) # create a 1920 * 1080 window : 2,073,600 pixels
is_prime = [True] * (number_of_pixels + 1) #initialize all numbers as prime to flag them false later
numbers = []
prime_numbers = []
for i in range(0, (number_of_pixels + 1)):
    numbers.append(i)


running = True
while running:

    # Allows closing window via the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(2, (number_of_pixels + 1)):
        coordinates = (i % 1920, i // 1920)  # turn current number into pixel coordinate
        if i % 1000 == 0:  # update screen this often
            pygame.display.flip()
        if is_prime[i]: # Prevents iterating multiple times over the same number
            prime_numbers.append(i) # list not used, implemented before doing the visualization
            screen.set_at((coordinates[0], coordinates[1]), green) #paint pixel green if it's prime
            number_to_multiply = i 
            times_multiplied = 1 # Used in while loop
            while number_to_multiply < number_of_pixels:
                times_multiplied += 1
                number_to_multiply = times_multiplied * i
                if number_to_multiply < number_of_pixels: # had to implement an if check since while check comes after execution
                    paint_this_pixel_red = (number_to_multiply % 1920, number_to_multiply // 1920)
                    is_prime[number_to_multiply] = False 
                    screen.set_at((paint_this_pixel_red[0], paint_this_pixel_red[1]), red)
                    if times_multiplied % 1000 == 0:  # update screen this often
                        pygame.display.flip()

pygame.quit()
