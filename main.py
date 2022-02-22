import pygame, colour as col, random

# initializing pygame
pygame.init()

# creating surface 
WIDTH, HEIGHT = 800, 500
surface = pygame.display.set_mode((WIDTH, HEIGHT))

# fps and clocking values
FPS = 60
clock = pygame.time.Clock()

# game values
BUFFER_DISTANCE = 40
MAX_LIVES = 5
COIN_VEL = 8
SCORE = 0
lives = MAX_LIVES
DRAGON_VEL = 9
coin_velocity = COIN_VEL
ACCELERATION = 0.5

# loading images ./feed_the_dragon/assets/
dragon_image = pygame.image.load('dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (75, HEIGHT//2)

coin_image = pygame.image.load('coin.png')
coin_rect = coin_image.get_rect()
coin_rect.center = (WIDTH+BUFFER_DISTANCE, random.randint(50, HEIGHT-24))

# loading sounds
hit_sound = pygame.mixer.Sound('sound_1.wav')
miss_sound = pygame.mixer.Sound('sound_2.wav')
miss_sound.set_volume(0.1)

pygame.mixer.music.load('music.wav')

# Defining fonts
custom_font = pygame.font.Font('AttackGraffiti.ttf', 26)

# Defining texts
game_text = custom_font.render('Feed the dragon', True, col.green)
game_text_rect = game_text.get_rect()
game_text_rect.center = (WIDTH // 2, 20)

score_text = custom_font.render(f'Score: {SCORE}', True, col.green)
score_text_rect = score_text.get_rect()
score_text_rect.center = (70, 20)

life_text  = custom_font.render(f'Lives left: {lives}', True, col.green)
life_text_rect = life_text.get_rect()
life_text_rect.center = (WIDTH - 120, 20)

continue_text = custom_font.render('Press any key to play again or quit window', True, col.red)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WIDTH//2, HEIGHT//2 - 50)

gameover_text = custom_font.render('GAME OVER you couldnt beat vilas hehehe!', True, col.green)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = (WIDTH//2, HEIGHT//2)


# playing the sound
pygame.mixer.music.play(-1,0.0)

# main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if lives <= 0:
        surface.blit(continue_text, continue_text_rect)
        surface.blit(gameover_text, gameover_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    SCORE = 0
                    coin_velocity = COIN_VEL
                    lives = MAX_LIVES
                    pygame.mixer.music.play()
                    is_paused = False


    if coin_rect.x < 0:
        coin_rect.center = (WIDTH+BUFFER_DISTANCE, random.randint(50, HEIGHT-24))
        lives -= 1
        miss_sound.play(1)

    coin_rect.x -= coin_velocity

    if dragon_rect.colliderect(coin_rect):
        SCORE += 1
        hit_sound.play(1)
        coin_rect.center = (WIDTH+BUFFER_DISTANCE, random.randint(50, HEIGHT-24))
        coin_velocity += ACCELERATION

    #fetching keys pressed
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and dragon_rect.top > 40:
        dragon_rect.y -= DRAGON_VEL

    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and dragon_rect.bottom < HEIGHT:
        dragon_rect.y += DRAGON_VEL

    # filling surface
    surface.fill(col.black)

    # blitting assets
    surface.blit(dragon_image, dragon_rect)
    surface.blit(coin_image,coin_rect)
    surface.blit(game_text, game_text_rect)
    surface.blit(score_text, score_text_rect)
    surface.blit(life_text, life_text_rect)

    # drawing a neat line between text and game play
    pygame.draw.line(surface, col.red, (0,40), (WIDTH,40), 3)

    # updating texts
    score_text = custom_font.render(f'Score: {SCORE}', True, col.green)
    life_text  = custom_font.render(f'Lives left: {lives}', True, col.green)

    # updating display
    pygame.display.update()
    clock.tick(FPS)

# uninitializing pygame
pygame.quit()