import pygame
import sys

# Inicializa PyGame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bola rebotando")

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Configuración de la bola
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal del juego
running = True

while running:

    # Manejar loop de eventos
    for event in pygame.event.get():
        # Detectar clic en X
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Detectar la tecla ESC cuando es presionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("¡Tecla Escape presionada!")
                pygame.quit()
                sys.exit()

    # Mover la bola según lo configurado
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Lóigica para detectar colisiones con las paredes
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_speed_x = -ball_speed_x  # Invertir la dirección en el eje X
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y = -ball_speed_y  # Invertir la dirección en el eje Y

    # Dibujar en la pantalla
    screen.fill(WHITE)  # Fondo blanco
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)  # Dibuja la bola azul

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el FPS (limitar a 60 FPS)
    clock.tick(60)