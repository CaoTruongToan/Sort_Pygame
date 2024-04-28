import pygame

pygame.init()

win_width = 950
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Quick sort")

x = 60
spacing = 60

height = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]

sorted_columns = [False] * len(height)

run = True

def show(height, sorted_columns, pivot_index, comparisons):
    max_height = max(height)
    for i in range(len(height)):
        scaled_height = int(height[i] / max_height * (win_height - 200))
        if i in comparisons:
            color = (0, 128, 0)  # Màu xanh cho việc so sánh
        elif i == pivot_index:
            color = (255, 165, 0)  # Màu cam cho pivot
        elif sorted_columns[i] or height[i] > height[pivot_index]:
            color = (255, 165, 0)  # Màu cam cho các cột đã sắp xếp và các cột lớn hơn giá trị pivot
        else:
            color = (0, 128, 0)  # Màu xanh cho các cột chưa sắp xếp và nhỏ hơn giá trị pivot
            
        pygame.draw.rect(win, color, (x + spacing * i, win_height - scaled_height - 40, 50, scaled_height))
        font = pygame.font.Font(None, 30)
        text = font.render(str(height[i]), True, (0, 0, 0))
        win.blit(text, (x + spacing * i + 15, win_height - scaled_height - 70))
        num_font = pygame.font.Font(None, 30)
        num_text = num_font.render(str(i+1), True, (0, 0, 0))
        win.blit(num_text, (x + spacing * i + 22, win_height - 30))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons = [j, high]
        show(arr, sorted_columns, high, comparisons)
        pygame.time.delay(100)
        pygame.display.update()
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    sorted_columns[i + 1] = True  # Cập nhật cờ đã sắp xếp cho cột đã đặt vào vị trí đã sắp xếp của nó
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

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
        quicksort(height, 0, len(height) - 1)
        win.fill((255, 255, 255))
        show(height, sorted_columns, -1, [])
        pygame.display.update()
    else:
        win.fill((255, 255, 255))
        show(height, sorted_columns, -1, [])
        pygame.display.update()

pygame.quit()
