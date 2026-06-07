import pygame
import random

pygame.init()
pygame.font.init()

speed = 20
display = (1280,720)
screen = pygame.display.set_mode(display)
clock = pygame.time.Clock()

# If you want you input your own array, uncomment this
# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# If you want the code to input the array, uncmment this
arr = []
for i in range(100):
    arr.append(random.randint(1,200))

# ---

comp = 0
text = pygame.font.SysFont('Noto Sans', 30)
bar_w = (display[0]-200) / len(arr)
bar_m_h = (display[1] - 200) / max(arr)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        screen.fill((30,30,30))

        for index, value in enumerate(arr):
            if i == index:
                pygame.draw.rect(screen, (90,90,200), (index*bar_w+100,display[1]-100-bar_m_h*value,bar_w-(100/len(arr)),bar_m_h*value))
            if j == index:
                pygame.draw.rect(screen, (90,200,90), (index*bar_w+100,display[1]-100-bar_m_h*value,bar_w-(100/len(arr)),bar_m_h*value))
            if i != index and j != index:
                pygame.draw.rect(screen, (200,200,200), (index*bar_w+100,display[1]-100-bar_m_h*value,bar_w-(100/len(arr)),bar_m_h*value))

        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        comp += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_EQUALS]:
            speed += 1
        if keys[pygame.K_MINUS]:
            speed -= 1

        screen.blit(text.render(f"Number of Comparisons: {comp}",True,(255,255,255)),(10,10))
        screen.blit(text.render(f"Speed: {speed/20:.1f}x",True,(255,255,255)),(display[0]-150,10))
        pygame.draw.line(screen, (200,200,100), (100,display[1]-100), (display[0]-100,display[1]-100), 5)
        pygame.display.flip()
        clock.tick(speed)
    
screen.fill((30,30,30))
for index, value in enumerate(arr):
    pygame.draw.rect(screen, (200,200,200), (index*bar_w+100,display[1]-100-bar_m_h*value,bar_w-(100/len(arr)),bar_m_h*value))
screen.blit(text.render(f"Number of Comparisons: {comp}",True,(255,255,255)),(10,10))
screen.blit(text.render(f"Speed: {speed/20:.1f}x",True,(255,255,255)),(display[0]-150,10))
pygame.draw.line(screen, (200,200,100), (100,display[1]-100), (display[0]-100,display[1]-100), 5)
pygame.display.flip()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False