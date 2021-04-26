import pygame

pygame.init()

size = [1920, 1080]
number_of_pixels = size[0] * size[1]
green = (0, 255, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode(size)
is_prime = [True] * (number_of_pixels + 1)
numbers = []
prime_numbers = []
total = 0
for i in range(0, (number_of_pixels + 1)):
    numbers.append(i)

# create a 1920 * 1080 window : 2,073,600 pixels
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(2, (number_of_pixels + 1)):
        coordinates = (i // 1920, i % 1920)  # i / y'de i sayi, y 1080 dik pixelden hangisi oldugu, kalan da x pixeli
        if i % 1000 == 0:  # update screen this often
            pygame.display.flip()
        if is_prime[i]:
            prime_numbers.append(i)
            screen.set_at((coordinates[1], coordinates[0]), green)
            number_to_multiply = i
            times_multiplied = 1
            while number_to_multiply < number_of_pixels:
                times_multiplied += 1
                number_to_multiply = times_multiplied * i
                if number_to_multiply < number_of_pixels:
                    paint_this_pixel_red = (number_to_multiply // 1920, number_to_multiply % 1920)
                    is_prime[number_to_multiply] = False
                    screen.set_at((paint_this_pixel_red[1], paint_this_pixel_red[0]), red)
                    if times_multiplied % 1000 == 0:  # update screen this often
                        pygame.display.flip()

        # screen.set_at((coordinates[1], coordinates[0]), green)
        # if i % 100 == 0:
        #     pygame.display.flip()
pygame.quit()
