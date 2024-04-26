# import pygame
# import sys

# pygame.init()

# win_width = 950
# win_height = 600

# win = pygame.display.set_mode((win_width, win_height))
# pygame.display.set_caption("Bubble sort")

# x = 60
# spacing = 60

# height = []

# def get_input():
#     global height
#     input_str = ""
#     input_font = pygame.font.Font(None, 30)
#     input_active = True
#     while input_active:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     input_active = False
#                 elif event.key == pygame.K_BACKSPACE:
#                     input_str = input_str[:-1]
#                 else:
#                     input_str += event.unicode
#         win.fill((255, 255, 255))
#         input_surface = input_font.render("Enter the values separated by commas: " + input_str, True, (0, 0, 0))
#         win.blit(input_surface, (10, 10))
#         pygame.display.update()

#     height = [int(val) for val in input_str.split(",")]

# def show(height, sorted_columns, comparisons):
#     max_height = max(height)
#     for i in range(len(height)):
#         scaled_height = int(height[i] / max_height * (win_height - 200))
#         if i in comparisons:
#             color = (0, 128, 0)  # Green color (RGB)
#             if i == 0 or i == 1: 
#                 color = (255, 165, 0)  # Orange color (RGB)
#         elif sorted_columns[i]:
#             if i == 0 or i == 1:  # First columns
#                 color = (255, 165, 0)  # Orange color (RGB)
#             elif i == len(height) - 1 or all(sorted_columns[i+1:]):  # Last column or all remaining columns sorted
#                 color = (255, 165, 0)  # Orange color (RGB)
#             else:
#                 color = (173, 216, 230)  # Light blue color (RGB) for other columns
#         else:
#             color = (173, 216, 230)  # Light blue color (RGB) for unsorted columns
            
#         pygame.draw.rect(win, color, (x + spacing * i, win_height - scaled_height - 40, 50, scaled_height))
#         font = pygame.font.Font(None, 30)
#         text = font.render(str(height[i]), True, (0, 0, 0))
#         win.blit(text, (x + spacing * i + 15, win_height - scaled_height - 70))
#         num_font = pygame.font.Font(None, 30)
#         num_text = num_font.render(str(i+1), True, (0, 0, 0))
#         win.blit(num_text, (x + spacing * i + 22, win_height - 30))

# def bubble_sort(height, sorted_columns):
#     comparisons = []
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(height) - 1):
#             comparisons = [i, i + 1]
#             if height[i] > height[i + 1]:
#                 height[i], height[i + 1] = height[i + 1], height[i]
#                 swapped = True
#                 sorted_columns[i] = False
#                 sorted_columns[i + 1] = True
#                 win.fill((255, 255, 255))
#                 show(height, sorted_columns, comparisons)
#                 pygame.time.delay(100)
#                 pygame.display.update()
#                 comparisons = []
#     # After sorting, set all sorted_columns to True
#     sorted_columns = [True] * len(height)

# def main():
#     global height
#     get_input()
#     sorted_columns = [False] * len(height)
#     run = True
#     while run:
#         pygame.time.delay(10)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if 800 <= event.pos[0] <= 900 and 50 <= event.pos[1] <= 90:
#                     bubble_sort(height, sorted_columns)
#         win.fill((255, 255, 255))
#         show(height, sorted_columns, [])
#         pygame.draw.rect(win, (0, 0, 0), (800, 50, 100, 40))
#         font = pygame.font.Font(None, 30)
#         text = font.render("Run", True, (255, 255, 255))
#         win.blit(text, (820, 60))
#         pygame.display.update()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()


import pygame
import sys

pygame.init()

win_width = 950
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Bubble sort")

x = 60
spacing = 60

height = []

def get_input():
    global height
    input_str = ""
    input_active = True
    font = pygame.font.Font(None, 30)
    input_rect = pygame.Rect(10, 10, win_width - 20, 30)
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
                else:
                    input_str += event.unicode
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), input_rect, 2)
        input_surface = font.render(input_str, True, (0, 0, 0))
        win.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.display.update()

    height = [int(val) for val in input_str.split(",")]

def show(height, sorted_columns, comparisons):
    max_height = max(height)
    for i in range(len(height)):
        scaled_height = int(height[i] / max_height * (win_height - 200))
        if i in comparisons:
            color = (0, 128, 0)  # Green color (RGB)
            if i == 0 or i == 1: 
                color = (255, 165, 0)  # Orange color (RGB)
        elif sorted_columns[i]:
            if i == 0 or i == 1:  # First columns
                color = (255, 165, 0)  # Orange color (RGB)
            elif i == len(height) - 1 or all(sorted_columns[i+1:]):  # Last column or all remaining columns sorted
                color = (255, 165, 0)  # Orange color (RGB)
            else:
                color = (173, 216, 230)  # Light blue color (RGB) for other columns
        else:
            color = (173, 216, 230)  # Light blue color (RGB) for unsorted columns
            
        pygame.draw.rect(win, color, (x + spacing * i, win_height - scaled_height - 40, 50, scaled_height))
        font = pygame.font.Font(None, 30)
        text = font.render(str(height[i]), True, (0, 0, 0))
        win.blit(text, (x + spacing * i + 15, win_height - scaled_height - 70))
        num_font = pygame.font.Font(None, 30)
        num_text = num_font.render(str(i+1), True, (0, 0, 0))
        win.blit(num_text, (x + spacing * i + 22, win_height - 30))

def bubble_sort(height, sorted_columns):
    comparisons = []
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(height) - 1):
            comparisons = [i, i + 1]
            if height[i] > height[i + 1]:
                height[i], height[i + 1] = height[i + 1], height[i]
                swapped = True
                sorted_columns[i] = False
                sorted_columns[i + 1] = True
                win.fill((255, 255, 255))
                show(height, sorted_columns, comparisons)
                pygame.time.delay(100)
                pygame.display.update()
                comparisons = []
    # After sorting, set all sorted_columns to True
    sorted_columns = [True] * len(height)

def main():
    global height
    get_input()
    sorted_columns = [False] * len(height)
    run = True
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 800 <= event.pos[0] <= 900 and 50 <= event.pos[1] <= 90:
                    bubble_sort(height, sorted_columns)

        sorted_columns = [True] * len(height)
        for i in range(len(height)):
            sorted_columns[i] = False           
        win.fill((255, 255, 255))
        show(height, sorted_columns, [])
        pygame.draw.rect(win, (0, 0, 0), (800, 50, 100, 40))
        font = pygame.font.Font(None, 30)
        text = font.render("Run", True, (255, 255, 255))
        win.blit(text, (820, 60))
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
