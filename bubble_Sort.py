import pygame
import sys

pygame.init()

win_width = 950
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Bubble sort")

x = 60
y = 60
width = 50
spacing = 60

height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]
sorted_columns = [False] * len(height)
sort_state = "Bubble Sort"

font = pygame.font.Font(None, 25)
font_color = (0, 0, 0)
font_position = (20, 20)

run = True

def show(height, sorted_columns, comparisons, swapping):
    max_height = max(height)
    for i in range(len(height)):
        scaled_height = int(height[i] / max_height * (win_height - 200))
        if i in comparisons:
            color = (0, 128, 0) 
        elif i in swapping: 
            color = (255, 0, 0)
        elif sorted_columns[i]:
            if all(sorted_columns[i+1:]):
                color = (173, 216, 230) 
            else:
                color = (255, 165, 0) 
        else:
            color = (173, 216, 230) 
        pygame.draw.rect(win, color, (x + spacing * i, win_height - scaled_height - 40, width, scaled_height))
        text = font.render(str(height[i]), True, (0, 0, 0))
        win.blit(text, (x + spacing * i + 15, win_height - scaled_height - 70))
        num_font = pygame.font.Font(None, 30)
        num_text = num_font.render(str(i+1), True, (0, 0, 0))
        win.blit(num_text, (x + spacing * i + 22, win_height - 30))

def check_if_sorted(sorted_columns):
    if all(sorted_columns):
        for i in range(len(sorted_columns)):
            sorted_columns[i] = False 
        win.fill((255, 255, 255))
        show(height, sorted_columns, [], []) 
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit() 
    return False

while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_SPACE]:
        execute = True

    if execute == False:
        check_if_sorted(sorted_columns)

    if execute:
        comparisons = []
        swapping = []
        swapped = True 
        while swapped:
            swapped = False
            for i in range(len(height) - 1):
                comparisons = [i, i + 1] 
                if height[i] > height[i + 1]:
                    height[i], height[i + 1] = height[i + 1], height[i]
                    swapped = True
                    swapping = [i, i + 1]
                    win.fill((255, 255, 255))
                    show(height, sorted_columns, comparisons, swapping)
                    pygame.time.delay(200)  
                    pygame.display.update()
                    swapping = [] 
                    comparisons = []
    else:
        win.fill((255, 255, 255))
        show(height, sorted_columns, [], [])
        pygame.display.update()

    # Display the sort state
    state_text = font.render(sort_state, True, font_color)
    win.blit(state_text, font_position)
    pygame.display.update()

pygame.quit()
