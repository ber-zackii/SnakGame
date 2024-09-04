import pygame
import time
import random

pygame.init()


WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 20
FPS = 15


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def reset_game():
    return [(100, 100), (90, 100), (80, 100)], (SNAKE_SIZE, 0), (
        random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
        random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE
    ), 0


snake, snake_direction, food, score = reset_game()


font = pygame.font.Font(None, 36)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, SNAKE_SIZE):
                snake_direction = (0, -SNAKE_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -SNAKE_SIZE):
                snake_direction = (0, SNAKE_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (SNAKE_SIZE, 0):
                snake_direction = (-SNAKE_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-SNAKE_SIZE, 0):
                snake_direction = (SNAKE_SIZE, 0)

    
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]
    ):
        snake, snake_direction, food, score = reset_game()

    
    if new_head == food:
        score += 1
        snake.append(snake[-1])  
        food = (
            random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
            random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE,
        )

    
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    
    clock.tick(FPS)


screen.fill(WHITE)
game_over_text = font.render(f"Game Over! Your Score: {score}", True, (0, 0, 0))
screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
pygame.display.flip()


time.sleep(3)


pygame.quit()
