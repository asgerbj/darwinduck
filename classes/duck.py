import pygame
import math
import os

class duck(pygame.sprite.Sprite):
    def __init__(self, name, volume,x,y):
        pygame.sprite.Sprite.__init__(self) 
        self.name = name
        self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "N.png"))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10,-10)
        self.rect.x = x
        self.rect.y = y
        self.xpos = float(x)
        self.ypos = float(y)
        self.old_x = 0
        self.old_y = 0

        self.lookdir = 0
        self.movementdir = 0
        self.movementspeed = 5
        self.maxspeed = 5

        # Load sounds
        self.sound_stone_hit = pygame.mixer.Sound(os.path.join('sound', 'stone_hit.wav'))
        self.sound_stone_hit.set_volume(volume)
        self.sound_duck1 = pygame.mixer.Sound(os.path.join('sound', 'duck_sound1.wav'))
        self.sound_duck1.set_volume(volume)
        self.sound_duck2 = pygame.mixer.Sound(os.path.join('sound', 'duck_sound2.wav'))
        self.sound_duck2.set_volume(volume)

    def right(self):
        self.movementspeed += 1
        if self.movementspeed > self.maxspeed:
            self.movementspeed = self.maxspeed
        elif self.movementspeed < -self.maxspeed:
            self.movementspeed = -self.maxspeed

        self.lookdir -= 30
        # self.movementdir -= 30
        self.movementdir = self.lookdir

        if self.lookdir < 0:
            self.lookdir = 360 + self.lookdir
        if self.movementdir < 0:
            self.movementdir = 360 + self.movementdir

    def left(self):
        self.movementspeed += 1
        if self.movementspeed > self.maxspeed:
            self.movementspeed = self.maxspeed
        elif self.movementspeed < -self.maxspeed:
            self.movementspeed = -self.maxspeed

        self.lookdir += 30
        # self.movementdir += 30
        self.movementdir = self.lookdir

        if self.lookdir > 360:
            self.lookdir = self.lookdir - 360
        if self.movementdir > 360:
            self.movementdir = self.movementdir - 360

    def playercollision(self, player_list):
        pygame.sprite.Sprite.remove(self, player_list)

        player_collision = pygame.sprite.spritecollide(self, player_list, False)
        collision_true = False

        multiplier = 1
        for player_collide in player_collision:
            collision_true = True
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            self.xpos   = self.old_x
            self.ypos   = self.old_y
            player_collide.rect.x = player_collide.old_x
            player_collide.rect.y = player_collide.old_y
            player_collide.xpos   = player_collide.old_x
            player_collide.ypos   = player_collide.old_y

            if self.movementspeed > player_collide.movementspeed:
                # constant to multiple the affect to push away ducks, avoid getting stuck in eachother
                self.movementspeed -= (self.movementspeed - player_collide.movementspeed) * multiplier
                # player_collide.movementdir   += self.movementdir
                # tmp1 = abs(abs(player_collide.movementspeed) - abs(self.movementspeed))/max(abs(player_collide.movementspeed), abs(self.movementspeed))
                player_collide.movementdir = self.movementdir
                player_collide.movementspeed += (player_collide.movementspeed - self.movementspeed) * 1.5
            else:
                # Switch self and player
                player_collide.movementspeed -= (player_collide.movementspeed - self.movementspeed) * 1.5
                self.movementdir = player_collide.movementdir
                self.movementspeed += (self.movementspeed - player_collide.movementspeed) * multiplier

            # speed cap
            if self.movementspeed > self.maxspeed:
                self.movementspeed = self.maxspeed
            elif self.movementspeed < -self.maxspeed:
                self.movementspeed = -self.maxspeed
            if player_collide.movementspeed > self.maxspeed:
                player_collide.movementspeed = self.maxspeed
            elif player_collide.movementspeed < -player_collide.maxspeed:
                player_collide.movementspeed = -player_collide.maxspeed
        player_list.add(self)
        return collision_true 

    def update(self, player_list, block_list, slow_list):
        old_x = self.rect.x
        old_y = self.rect.y
        self.old_x = old_x
        self.old_y = old_y

        self.ypos -= self.movementspeed * math.cos(self.movementdir * math.pi / 180)
        self.rect.y = int(self.ypos)
        self.xpos -= self.movementspeed * math.sin(self.movementdir * math.pi / 180) 
        self.rect.x = int(self.xpos)

        slowed = pygame.sprite.spritecollide (self, slow_list, False)
        for i in slowed:
            self.movementspeed = self.movementspeed * 0.9 # Controls slow effect

        self.movementspeed =  self.movementspeed * 0.95
        angle = 360 / 8 / 2

        if self.lookdir >= 360-angle or self.lookdir <= angle :
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "N.png"))
        elif self.lookdir >= 360 - 3 * angle :
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "NE.png"))
        elif self.lookdir >= 360 - 5 * angle:
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "E.png"))
        elif self.lookdir >= 360 - 7 * angle:
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "SE.png"))
        elif self.lookdir >= 360 - 9 * angle:
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "S.png"))
        elif self.lookdir >= 360 - 11 * angle:
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "SW.png"))
        elif self.lookdir >= 360 - 13 * angle:
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "W.png"))
        elif self.lookdir >= 360 - 15 * angle:
            self.image = pygame.image.load(os.path.join("images/%s/"%self.name, "NW.png"))

        collide = pygame.sprite.spritecollide (self, block_list, False)
        if collide:
            # We collided, go back to the old pre-collision location
            self.rect.x = old_x
            self.rect.y = old_y
            self.xpos = old_x
            self.ypos = old_y
            self.movementspeed = 0
            if self.sound_last_collide == False:
                self.sound_stone_hit.play()
                self.sound_last_collide = True
        else:
            self.sound_last_collide = False

        if self.rect.y >= 600 : # screen height
            # diff = player1.rect.y - 500
            self.rect.y = 600 - self.rect[3]
            # player2.rect.y -= diff
            # for block in block_list:
            #     block.rect.y -= diff

        if self.rect.x <= 0:
           # diff = player1.rect.y - 500
           self.rect.x = 0
           self.xpos = 0

        if self.rect.x >= 500 - self.rect[2]:
           # diff = player1.rect.y - 500
           self.rect.x = 500 - self.rect[2]
           self.xpos = 500  - self.rect[2]

        self.rect.y += 1
        self.ypos += 1

        if self.rect.y > 600:
            self.kill()

    def detectsprint(self, player_list, block_list, slow_list):
        if self.rect.y <= 50:
            pygame.sprite.Sprite.remove(self, player_list)
            diff = 50 - self.rect.y
            self.rect.y = 50
            self.ypos = 50

            for block in block_list:
                block.rect.y += 3	
            for block in slow_list:
                block.rect.y += 3
            for player in player_list:
                player.rect.y += 4
                player.ypos = player.rect.y
            player_list.add(self)

