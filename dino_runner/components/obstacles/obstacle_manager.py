import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus 
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
          if random.randint(0, 2) == 0:
              self.obstacles.append(Cactus(SMALL_CACTUS))
          elif random.randint(0, 2) == 1:
              self.obstacles.append(Cactus(LARGE_CACTUS))
          elif random.randint(0, 2) == 2:
              self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)   
            if game.player.dino_rect.colliderect(obstacle.rect):
              if not game.player.has_power_up:
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break
              else: 
                  self.obstacles.remove(obstacle)
    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)        
