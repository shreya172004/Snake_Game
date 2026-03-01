import pygame as pg
import random
import math

class game():
    def snakegame():
        window_size = 800
        tilesize = 50
        range_x = (tilesize, window_size - tilesize, tilesize)
        range_y = (tilesize, window_size - tilesize, tilesize)
        pos = lambda: [random.randrange(*range_x), random.randrange(*range_y)]
        snake = pg.Rect(pos() + [tilesize - 2, tilesize - 2])
        snake_center = pos()
        snake_direction = (0, 0)
        snake_length = 1
        segments = [snake.copy()]
        def generate_food():
            while True:
                food_position = pg.Rect(pos() + [tilesize - 2, tilesize - 2])
                if not snake.colliderect(food_position):
                     return food_position
        food = generate_food()
        screen = pg.display.set_mode([window_size] * 2)
        clock = pg.time.Clock()
        timestep = 200
        dirs = {pg.K_w: (0, -tilesize), pg.K_s: (0, tilesize), pg.K_a: (-tilesize, 0), pg.K_d: (tilesize, 0)}
        while True: 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key in dirs:
                        snake_direction = dirs[event.key]
                    elif event.key == pg.K_q:  # Check if 'Q' key is pressed
                        pg.quit()
                        exit() 
            screen.fill((0, 0, 0))
            self_eat = snake.collidelist(segments[:-1]) != -1
            if snake.left < 0 or snake.right > window_size or snake.top < 0 or snake.bottom > window_size or self_eat:
                snake.center = pos()
                food.center = generate_food().center  # Regenerate food position
                snake_length = 1
                segments = [snake.copy()]
            if snake.colliderect(food):
                snake_length += 1
                food.center = generate_food().center  # Regenerate food position
            segments.insert(0, snake.copy())
            if len(segments) > snake_length:
                segments.pop()
            snake.move_ip(snake_direction)
            for segment in segments:
                pg.draw.rect(screen, (0, 255, 0), segment)
            pg.draw.rect(screen, (255, 0, 0), food)
            pg.display.flip()

            clock.tick(7)  # Lowered the tick rate for better visibility


    snakegame()


    