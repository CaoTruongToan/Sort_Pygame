import pygame
import sys

pygame.init()

win_width = 950
win_height = 600

# Create window
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Selection Sort")

# Initial variables
x = 60
y = 60
width = 50
spacing = 60

height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]
sorted_columns = [False] * len(height)
sort_state_selection = "Selection Sort"  

run = True

# Function to draw columns
def show(height, sorted_columns, selected, comparing):
    max_height = max(height)
    for i in range(len(height)):
        scaled_height = int(height[i] / max_height * (win_height - 200))
        color = (173, 216, 230)
        if sorted_columns[i]:
            if all(sorted_columns[i + 1:]):
                color = (173, 216, 230)
            else:
                color = (255, 165, 0)
        elif i == comparing:
            color = (0, 128, 0)  # Green for comparing
        elif i == selected:
            color = (255, 0, 0)  # Red for selected
        pygame.draw.rect(win, color, (x + spacing * i, win_height - scaled_height - 40, width, scaled_height))
        font = pygame.font.Font(None, 30)
        text = font.render(str(height[i]), True, (0, 0, 0))
        win.blit(text, (x + spacing * i + 15, win_height - scaled_height - 70))
        num_font = pygame.font.Font(None, 30)
        num_text = num_font.render(str(i + 1), True, (0, 0, 0))
        win.blit(num_text, (x + spacing * i + 22, win_height - 30))

    font = pygame.font.Font(None, 36)
    state_text = font.render(f"{sort_state_selection}", True, (0, 0, 0))
    win.blit(state_text, (20, 20))

    pygame.display.update()

def check_if_sorted(sorted_columns):
    if all(sorted_columns):
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

# Main 
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
        for i in range(len(height)):
            min_index = i
            for j in range(i + 1, len(height)):
                comparing = j
                show(height, sorted_columns, i, comparing)
                pygame.time.delay(200)
                pygame.display.update()
                if height[j] < height[min_index]:
                    min_index = j
            height[i], height[min_index] = height[min_index], height[i]
            sorted_columns[i] = True
            win.fill((255, 255, 255))
            show(height, sorted_columns, -1, -1)
            pygame.time.delay(500)
            pygame.display.update()
    else:
        win.fill((255, 255, 255))
        show(height, sorted_columns, -1, -1)
        pygame.display.update()

# Quit Pygame
pygame.quit()
