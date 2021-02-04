import pygame
import random
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (43, 255, 0)
bright_green = (0, 255, 0)

window_width = 900
window_height = 600

snakeX_coordinate = 0
snakeY_coordinate = 0

snakeImage = pygame.image.load('snakePicture.jpg')
snakeImage = pygame.transform.scale(snakeImage, (900, 600))


def snakeImage_show():
    gameWindow.blit(snakeImage, (snakeX_coordinate, snakeY_coordinate))


clock = pygame.time.Clock()
gameWindow = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Snake")


def draw_snake(color, snakeList):
    for x, y in snakeList:
        pygame.draw.rect(gameWindow, red, [x, y, 20, 20])


def text_screen(fontName, text, color, x, y, num):
    font = pygame.font.SysFont(fontName, num)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


run = True


def gameloop():
    gameWindow.fill(white)
    flagPrime = 0
    flag = 0
    score = 0
    game_over = False
    run = True
    snake_List = []
    snake_length = 1
    snake_x = 55
    snake_y = 45
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(10, 800)
    food_y = random.randint(0, 500)
    while run:



        if game_over:
            snakeImage_show()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            text_screen("calibrib.ttf", "Game Over!", black, 320, 130, 75)
            if flag == 1:
                text_screen("calibrib.ttf", "You hit the wall!", black, 365, 190, 35)
            elif flagPrime == 1:
                text_screen("calibrib.ttf", "You bit yourself!", black, 365, 190, 35)


            if 360 < mouse[0] < 559 and mouse[1] > 250 and mouse[1] < 309:
                pygame.draw.rect(gameWindow, red, [360, 250, 200, 60])
                if click[0] == 1 :

                    gameloop()
            else:
                pygame.draw.rect(gameWindow, green, [360, 250, 200, 60])
            text_screen("calibrib.ttf", "Play Again", black, 385, 265, 40)

            if 30 < mouse[0] < 559 and mouse[1] > 350 and mouse[1] < 410:
                pygame.draw.rect(gameWindow, red, [360, 350, 200, 60])
                if click[0] == 1:
                    run = False

            else:
                pygame.draw.rect(gameWindow, green, [360, 350, 200, 60])

            text_screen("calibrib.ttf", "Exit Game", black, 385, 365, 40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            pygame.display.update()

            gameWindow.fill(white)

            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_List.append(snake_head)

            if snake_head in snake_List[:-2]:
                game_over = True
                flagPrime = 1
                time.sleep(1)

            if snake_x < 0 or snake_x > window_width or snake_y < 0 or snake_y > window_width:
                flag = 1
                game_over = True
                time.sleep(1)

            if len(snake_List) > snake_length:
                del snake_List[0]

            pygame.draw.rect(gameWindow, green, [food_x, food_y, 20, 20])
            draw_snake(red, snake_List)

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                snake_length += 10
                score += 10
                food_x = random.randint(0, 600 - 40)
                food_y = random.randint(0, 600 - 40)

            text_screen('calibrib.ttf', "Score:{}".format(score), black, 10, 10, 25)

        pygame.display.update()
        clock.tick(70)


gameloop()
pygame.quit()
quit()
