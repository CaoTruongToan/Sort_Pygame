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

height = []  # Remove the predefined height list

def is_valid_input(char):
    # Chỉ cho phép nhập số và dấu phẩy
    return char.isdigit() or char == ','

def get_input():
    global height
    input_str = ""
    input_active = True
    font = pygame.font.Font(None, 30)
    input_rect = pygame.Rect(10, 50, win_width - 20, 30)
    title_font = pygame.font.Font(None, 36)
    title_text = title_font.render(u'Nhap các so nguyen cách nhau bang dau phay (VD: 3, 1, 5, 2)', True, (0, 0, 0))
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_str = input_str[:-1]
                elif is_valid_input(event.unicode):
                    input_str += event.unicode
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), input_rect, 2)
        input_surface = font.render(input_str, True, (0, 0, 0))
        win.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        win.blit(title_text, (10, 10))
        pygame.display.update()

    height = [int(val) for val in input_str.split(",") if val.isdigit()]

def show(height, selected, comparing):
    max_height = max(height)
    for i in range(len(height)):
        scaled_height = int(height[i] / max_height * (win_height - 200))
        color = (173, 216, 230)
        if i == comparing:
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

    pygame.display.update()

def insertion_sort(height):
    for i in range(1, len(height)):
        key = height[i]
        j = i - 1
        while j >= 0 and key < height[j]:
            height[j + 1] = height[j]
            j -= 1
            show(height, j + 1, j)
            pygame.time.delay(500)
        height[j + 1] = key
        show(height, -1, -1)
        pygame.time.delay(500)

def main():
    global height
    get_input()
    run_sort = True
    while run_sort:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        insertion_sort(height)
        run_sort = False  # After sorting, exit the loop

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
