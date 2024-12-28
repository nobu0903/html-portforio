import pygame, random

#initialize pygame 
pygame.init()

#set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("monster wrangler2")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#set class
class Game:

    def __init__(self, player, monster_group):
        """initialize the game object"""
        self.score = 0
        self.round_number= 0

        self.round_time = 0
        self.frame_count = 0        

        self.player = player
        self.monster_group = monster_group

        #set sound and music
        self.next_round_music = pygame.mixer.Sound("next_level.wav")

        #set font
        self.font= pygame.font.Font("Abrushow.ttf", 24)

        #set images
        blue_image = pygame.image.load("blue_monster.png")
        green_image = pygame.image.load("green_monster.png")
        purple_image = pygame.image.load("purple_monster.png")
        yellow_image = pygame.image.load("yellow_monster.png")

        self.target_monster_images = [blue_image, green_image, purple_image, yellow_image]
        
        self.target_monster_type = random.randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WINDOW_WIDTH//2
        self.target_monster_rect.top = 30

    def update(self):
        """update game object"""
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

            #check collision
            self.check_collisions()

    def draw(self):
        #set colors
        WHITE = (255, 255, 255)
        BLUE = (20, 176, 235)
        GREEN = (87, 201, 47)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157, 20)

        #add colors
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        #set text
        catch_text = self.font.render("Current Ctach", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WINDOW_WIDTH//2
        catch_rect.top = 5

        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        lives_text = self.font.render("Lives " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)
        
        round_text = self.font.render("Round " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

        time_text = self.font.render("Round Time: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, 5)

        warp_text = self.font.render("Warps: " + str(self.player.warps), True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topright = (WINDOW_WIDTH - 10, 35)

         # Blit HUD
        display_surface.blit(catch_text, catch_rect)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(lives_text, lives_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)
        display_surface.blit(warp_text, warp_rect)
        display_surface.blit(self.target_monster_image, self.target_monster_rect)

        pygame.draw.rect(display_surface, colors[self.target_monster_type], (WINDOW_WIDTH//2 - 32, 30, 64, 64), 2)
        pygame.draw.rect(display_surface, colors[self.target_monster_type], (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT - 200), 4)
        
    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)

        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                self.score += 100*self.round_number

                collided_monster.remove(self.monster_group)
                if self.monster_group:
                    self.player.catch_sound.play()
                    self.choose_new_target()

                else:
                    self.player.reset()
                    self.start_new_round
            #caught wrong monster
            else:
                self.player.die_sound.play()
                self.playerlives -= 1
                #check game over
                if self.player.lives <= 0:
                    self.pause_game("Final Score: " + str(self.score), "Press ENter to play again")
                    self.reset_game()
                self.player.reset()            


    def start_new_round(self):
        self.score += int(10000 * self.round_number / (1 + self.round_time))

        #reset the values
        self.round_time = 0
        self.frame_count = 0
        self.round_number += 1
        self.player.warps += 1

        for monster in self.monster_group:
            self.monster_group.remove(monster)

        # Add monsters to the monster group
        for i in range(self.round_number):
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[0], 0))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[1], 1))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[2], 2))
            self.monster_group.add(Monster(random.randint(0, WINDOW_WIDTH - 64), random.randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[3], 3))
                          
    def choose_new_target(self):
        target_monster = random.choice(self.monster_group.sprites())
        self.target_monster_type = target_monster.type
        self.target_monster_image = target_monster.image

    def pause_game(self, main_text, sub_text):
        global running
        # Set colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # Create main pause text
        main_text_render = self.font.render(main_text, True, WHITE)
        main_rect = main_text_render.get_rect()
        main_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        # Create the sub pause text
        sub_text_render = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text_render.get_rect()
        sub_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

        # Display the pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text_render, main_rect)
        display_surface.blit(sub_text_render, sub_rect)
        pygame.display.update()

        # Pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    is_paused == False
                    running = False
    
    def reset_game(self):
        self.score = 0
        self.round_number = 0
        self.player.lives = 5
        self.player.warps = 2
        self.player.reset()
        self.start_new_round()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("catch.wav")
        self.die_sound = pygame.mixer.Sound("die.wav")
        self.warp_sound = pygame.mixer.Sound("warp.wav")

    def update(self):
        """update the player"""
        #move the player within the bounnddery of the screen
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity
        
class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.type = monster_type

        #set_random mostion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)        

    def update(self):
        self.rect.x += self.dx * self.velocity
        self.rect.y -= self.dy * self.velocity

        #Bounce the monster if monster come to the edge of the screen
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -self.dx
        if self.rect.top <= 0 or self.rect.left >= WINDOW_HEIGHT:
            self.dy = -self.dy 

#Create player group
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#create monster group
my_monster_group = pygame.sprite.Group()

#create a game object
my_game = Game(my_player, my_monster_group)
my_game.pause_game("Monster Wrangler", "Press Enter to bigin")
my_game.start_new_round()


#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.warp()

    # Fill the display
    display_surface.fill((0, 0, 0))

    # Update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    # Update the game and draw HUD
    my_game.update()
    my_game.draw()

    # Update display and tick
    pygame.display.update()
    clock.tick(FPS)


#End the pygame
pygame.quit()
