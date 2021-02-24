import pygame
from random import randint


def on_grid_random():
    x = randint(0, 590)
    y = randint(0, 590)
    return x // 10 * 10, y // 10 * 10


def collision(c1, c2):
    return c1[0] == c2[0] and (c1[1] == c2[1])


# Definindo os movimentos da cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))  # Definindo a tela
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]  # Corpo da cobra
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))  # Cor da cobra (branca)

apple_pos = on_grid_random()  # Gerando uma posição aleatória para a posição da maçã
apple = pygame.Surface((10, 10))  # Tamanho da maçã
apple.fill((255, 0, 0))  # Cor da maçã (vermelha)

snakedirection = LEFT  # Cobra nasce andando para a esquerda

clock = pygame.time.Clock()  # Faz a cobra andar

font = pygame.font.Font('freesansbold.ttf', 20)  # Escreve a pontuação
score = 0  # Pontuação

game_over = False
while not game_over:
    clock.tick(17)  # Velocidade da cobra
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fechar o jogo
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:  # Configura as teclas das setas para mover a cobra
            if event.key == pygame.K_UP and snakedirection != DOWN:
                snakedirection = UP
            if event.key == pygame.K_DOWN and snakedirection != UP:
                snakedirection = DOWN
            if event.key == pygame.K_RIGHT and snakedirection != LEFT:
                snakedirection = RIGHT
            if event.key == pygame.K_LEFT and snakedirection != RIGHT:
                snakedirection = LEFT

    if collision(snake[0], apple_pos):  # Colisão entre a cobra e a maçã
        apple_pos = on_grid_random()  # Gera uma NOVA maçã
        snake.append((0, 0))  # Faz a cobra crescer
        score = score + 1  # Aumenta a pontuação em +1 ponto

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:  # Colisão com a parede
        game_over = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:  # Cobra morre se bater nela mesma
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if snakedirection == UP:  # Forma que a cobra se movimenta na tela
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if snakedirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if snakedirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if snakedirection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    screen.fill((0, 0, 0))  # Cor da tela
    screen.blit(apple, apple_pos)  # Faz a maçã aparecer na tela

    for x in range(0, 600, 10):  # Linhas horizontais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):  # linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    score_font = font.render(f'Score: {score}', True, (255, 255, 255))  # Escreve a pontuação na tela
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)  # Localização da pontuação
    screen.blit(score_font, score_rect)  # Faz a pontuação aparecer na tela

    for pos in snake:
        screen.blit(snake_skin, pos)  # Faz a cobra aparecer na tela

    pygame.display.update()  # Atualiza a tela

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)  # Fonte que vai ser usada para escrever o "Game Over"
    game_over_screen = game_over_font.render('GAME OVER', True, (255, 255, 255))  # "Renderiza" o 'GAME OVER'
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600/2, 10)
    screen.blit(game_over_screen, game_over_rect)  # Faz aparecer na tela usando a var game_over_screen
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
