import pygame, sys, time, random
from pygame.locals import *

pygame.init()
play_surface = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

def food_spawn():
    food_pos = [random.randint(0,49)*10, random.randint(0,49)*10]
    return food_pos

def main():
    snake_pos = [100,50]
    snake_body = [[100,50], [90,50],[80,50]]
    direction = "RIGHT"
    change = direction
    food_pos = food_spawn()
    score = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        change = "RIGHT"
                    if event.key == pygame.K_LEFT:
                        change = "LEFT"
                    if event.key == pygame.K_UP:
                        change = "UP"
                    if event.key == pygame.K_DOWN:
                        change = "DOWN"

        if change == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"
        if change == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change == "UP" and direction != "DOWN":
            direction = "UP"
        if change == "DOWN" and direction != "UP":
            direction = "DOWN"

        if direction == "RIGHT":
            snake_pos[0] += 10
        if direction == "LEFT":
            snake_pos[0] -= 10
        if direction == "UP":
            snake_pos[1] -= 10
        if direction == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_pos = food_spawn()
            score += 1
        else:
            snake_body.pop()

        play_surface.fill((0,0,0))

        for pos in snake_body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(food_pos[0], food_pos[1], 10, 10))


        if snake_pos[0] >= 500 or snake_pos[0] <=0:
            print(f"Game Over! Score: {score})")
            run = False
        if snake_pos[1] >= 500 or snake_pos[1] <=0:
            print(f"Game Over! Score: {score})")
            run = False

        if snake_pos in snake_body[1:]:
            print(f"Game Over! Score: {score})")
            run = False

        pygame.display.flip()
        fps.tick(10)

main()
pygame.quit()
