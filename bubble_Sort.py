import pygame

pygame.init()

win_width = 950
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Bubble sort")

x = 60
spacing = 60

height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]

sorted_columns = [False] * len(height)

run = True

def show(height, sorted_columns, comparisons):
    max_height = max(height)
    for i in range(len(height)):
        scaled_height = int(height[i] / max_height * (win_height - 200))
        if i in comparisons:
            color = (0, 128, 0)  # Màu xanh đậm (RGB)
            if i == 0 or i == 1: 
                color = (255, 165, 0)
        elif sorted_columns[i]:
            if i == 0 or i == 1:  # Các cột đầu tiên
                color = (255, 165, 0)  # Màu cam (RGB)
            elif i == len(height) - 1 or all(sorted_columns[i+1:]):  # Cột cuối cùng hoặc tất cả các cột còn lại đã sắp xếp xong
                color = (255, 165, 0)  # Màu cam (RGB)
            else:
                color = (173, 216, 230)  # Màu xanh nhạt (RGB) cho các cột còn lại
        else:
            color = (173, 216, 230)  # Màu xanh nhạt (RGB) cho các cột chưa được sắp xếp
            
        pygame.draw.rect(win, color, (x + spacing * i, win_height - scaled_height - 40, 50, scaled_height))
        font = pygame.font.Font(None, 30)
        text = font.render(str(height[i]), True, (0, 0, 0))
        win.blit(text, (x + spacing * i + 15, win_height - scaled_height - 70))
        num_font = pygame.font.Font(None, 30)
        num_text = num_font.render(str(i+1), True, (0, 0, 0))
        win.blit(num_text, (x + spacing * i + 22, win_height - 30))

while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_SPACE]:
        execute = True

    if not execute:
        execute = True if not all(sorted_columns) else False

    if execute:
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
        # Sau khi quá trình sắp xếp hoàn tất, chuyển tất cả các giá trị trong sorted_columns về True
        sorted_columns = [True] * len(height)
        
        for i in range(len(height)):
            sorted_columns[i] = False
        win.fill((255, 255, 255))
        show(height, sorted_columns, [])
        pygame.display.update()
    else:
        win.fill((255, 255, 255))
        show(height, sorted_columns, [])
        pygame.display.update()

pygame.quit()