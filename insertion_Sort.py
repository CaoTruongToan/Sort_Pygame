import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
win_width = 950
win_height = 600

# Create window
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Insertion Sort")

# Initial variables
x = 60
y = 60
width = 50
spacing = 60

height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]
sorted_columns = [False] * len(height)
sort_state = "Insertion Sort"  # Add sort state

run = True

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
        # Adjust text position
        text_rect = text.get_rect(center=(x + spacing * i + width // 2, win_height - scaled_height - 60))
        win.blit(text, text_rect)
        num_font = pygame.font.Font(None, 30)
        num_text = num_font.render(str(i + 1), True, (0, 0, 0))
        # Adjust number position
        num_rect = num_text.get_rect(center=(x + spacing * i + width // 2, win_height - 30))
        win.blit(num_text, num_rect)
    
    # Show sorting state
    font = pygame.font.Font(None, 36)
    state_text = font.render(f"{sort_state}", True, (0, 0, 0))
    win.blit(state_text, (20, 20))

    pygame.display.update()

def check_if_sorted(sorted_columns):
    if all(sorted_columns):
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()


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
        for i in range(1, len(height)):
            key = height[i]
            j = i - 1
            while j >= 0 and key < height[j]:
                height[j + 1] = height[j]
                j -= 1
                show(height, sorted_columns, j + 1, j)
                pygame.time.delay(500)
            height[j + 1] = key
            sorted_columns[i] = True
            if all(sorted_columns):
                sort_state = "Sorted"  # Update sort state
            win.fill((255, 255, 255))
            show(height, sorted_columns, -1, -1)
            pygame.time.delay(200)
    else:
        win.fill((255, 255, 255))
        show(height, sorted_columns, -1, -1)

# Quit Pygame
pygame.quit()
