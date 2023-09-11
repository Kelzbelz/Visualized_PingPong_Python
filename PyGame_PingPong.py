import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = random.choice((BALL_SPEED, -BALL_SPEED))
ball_speed_y = random.choice((BALL_SPEED, -BALL_SPEED))

# Paddles
player_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, 10, 100)
opponent_paddle = pygame.Rect(10, HEIGHT // 2 - 50, 10, 100)

# Score variables
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x = -ball_speed_x

    # Scoring
    if ball.left <= 0:
        player_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = BALL_SPEED
        ball_speed_y = random.choice((BALL_SPEED, -BALL_SPEED))

    if ball.right >= WIDTH:
        opponent_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = -BALL_SPEED
        ball_speed_y = random.choice((BALL_SPEED, -BALL_SPEED))

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (WIDTH - 180, 20))
    screen.blit(opponent_text, (20, 20))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
