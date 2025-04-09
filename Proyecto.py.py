import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Dirección inicial de la serpiente
dx, dy = CELL_SIZE, 0

# Inicialización de la serpiente y la comida
snake = [(WIDTH//2, HEIGHT//2)]
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL_SIZE
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL_SIZE, 0

    # Mover la serpiente
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, new_head)

    # Comprobación de colisión con la comida
    if new_head == food:
        food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    else:
        snake.pop()

    # Comprobación de colisión con los bordes o consigo misma
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]):
        running = False

    # Dibujar la serpiente y la comida
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control de velocidad

pygame.quit()