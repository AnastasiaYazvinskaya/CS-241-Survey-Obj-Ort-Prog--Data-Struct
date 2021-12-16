"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Prove 11
"""

import math
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

class Velocity:
    def __init__(self):
        self.dx = 0
        self.dy = 0

class FlyingObjects:
    def __init__(self):
        self.img = ""
        self.center = Point()
        self.velocity = Velocity()
        self.angle = 0
        self.speed = 1
        self.alive = True
        self.radius = 0

        self.visiable = 255

    def advance(self):
        self.is_off_screen()
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def draw(self):
        texture = arcade.load_texture(self.img)

        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      texture.width, texture.height, texture,
                                      self.angle, self.visiable)

    def is_off_screen(self):
        if (self.center.x) > SCREEN_WIDTH:
            self.center.x -= SCREEN_WIDTH
        elif (self.center.x) < 0:
            self.center.x += SCREEN_WIDTH
        elif (self.center.y) > SCREEN_HEIGHT:
            self.center.y -= SCREEN_HEIGHT
        elif (self.center.y) < 0:
            self.center.y += SCREEN_HEIGHT

class Asteroid(FlyingObjects): #Large
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_big1.png"

        self.center.x = random.randint(0, SCREEN_WIDTH)
        self.center.y = random.randint(0, SCREEN_HEIGHT)

        self.radius = BIG_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        self.angle = random.randint(0, 360)
        self.velocity.dx = math.cos(math.radians(self.angle+90)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle+90)) * self.speed    

    def hit(self):
        self.alive = False

    def new_asteroid(self, type):
        asteroid = Asteroid()
        if type == 'small':
            asteroid = SmallRock()
            asteroid.velocity.dx = self.velocity.dx + math.cos(math.radians(0)) * 5
            asteroid.velocity.dy = self.velocity.dy
        elif type == 'small2':
            asteroid = SmallRock()
            asteroid.velocity.dx = self.velocity.dx + math.cos(math.radians(0)) * 1.5
            asteroid.velocity.dy = self.velocity.dy + math.sin(math.radians(90)) * 1.5
        elif type == 'small3':
            asteroid = SmallRock()
            asteroid.velocity.dx = self.velocity.dx + math.cos(math.radians(180)) * 1.5
            asteroid.velocity.dy = self.velocity.dy + math.sin(math.radians(270)) * 1.5
        elif type == 'medium1':
            asteroid = MediumRock()
            asteroid.velocity.dx = self.velocity.dx
            asteroid.velocity.dy = self.velocity.dy + math.sin(math.radians(90)) * 2
        elif type == 'medium2':
            asteroid = MediumRock()
            asteroid.velocity.dx = self.velocity.dx
            asteroid.velocity.dy = self.velocity.dy + math.sin(math.radians(270)) * 2
        asteroid.center.x = self.center.x
        asteroid.center.y = self.center.y
        
        return (asteroid)

class LargeRock(Asteroid):
    def __init__(self):
        super().__init__()
        self.center.y = random.randint(0, SCREEN_HEIGHT*2/3)

    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN

    def hit(self):
        super().hit()
        asteroids = []
        #1 medium rock
        asteroids.append(self.new_asteroid('medium1'))
        #2 medium rock
        asteroids.append(self.new_asteroid('medium2'))
        #1 small rock
        asteroids.append(self.new_asteroid('small'))

        return asteroids
    
class MediumRock(Asteroid):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_med1.png"
        self.radius = MEDIUM_ROCK_RADIUS

    def advance(self):
        super().advance()
        self.angle -= MEDIUM_ROCK_SPIN

    def hit(self):
        super().hit()
        asteroids = []
        #1 small rock
        asteroids.append(self.new_asteroid('small2'))
        #2 small rock
        asteroids.append(self.new_asteroid('small3'))
        
        return asteroids

class SmallRock(Asteroid):
    def __init__(self):
        super().__init__()
        self.img = "images/meteorGrey_small1.png"
        self.radius = SMALL_ROCK_RADIUS

    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN

    def hit(self):
        super().hit()
        return []

class Ship(FlyingObjects):
    def __init__(self):
        super().__init__()
        self.img = "images/playerShip1_orange.png"
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.radius = SHIP_RADIUS

    def rotate(self, key):
        if key == 'l':
            self.angle += SHIP_TURN_AMOUNT
        elif key == 'r':
            self.angle -= SHIP_TURN_AMOUNT

    def go(self, key):
        if key == 'u':
            self.velocity.dx -= math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy += math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        elif key == 'd':
            self.velocity.dx += math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy -= math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT

class Bullet(FlyingObjects):
    def __init__(self, ship_angle, ship_center, ship_speed):
        super().__init__()
        self.img = "images/laserBlue01.png"

        self.center.x = ship_center.x
        self.center.y = ship_center.y
        self.angle = ship_angle + 90
        
        self.radius = BULLET_RADIUS
        self.speed = BULLET_SPEED
        self.lives = BULLET_LIFE

        self.velocity.dx = ship_speed.dx + math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = ship_speed.dy + math.sin(math.radians(self.angle)) * self.speed

    def advance(self):
        super().advance()
        self.lives -= 1
        if self.lives == 0:
            self.alive = False

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.ship = Ship()
        self.bullets = []
        self.asteroids = []

        for i in range(INITIAL_ROCK_COUNT):
            self.asteroids.append(LargeRock())

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        if not self.ship.alive:
            # Imitation of the game if ship die (Game over)
            self.imitate()

            arcade.draw_text("GAME OVER",
                             start_x = SCREEN_WIDTH/5, start_y = SCREEN_HEIGHT/2,
                             font_size = 60, color = arcade.color.WHITE_SMOKE)

        # TODO: draw each object
        self.ship.draw()

        for bullet in self.bullets:
            bullet.draw()

        for asteroid in self.asteroids:
            asteroid.draw()

    # Imitation of the game if ship die (Game over)
    def imitate(self):
        self.ship.visiable = 50

        if random.randint(1, 50) == 1:
            bullet = Bullet(self.ship.angle, self.ship.center, self.ship.velocity)
            bullet.visiable = 50
            self.bullets.append(bullet)

            angle = random.randint(-10, 10)
            self.ship.angle += SHIP_TURN_AMOUNT*angle
        elif random.randint(1, 3) == 3:
            self.ship.velocity.dx -= math.sin(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy += math.cos(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
        elif random.randint(1, 4) % 2 == 0:
            self.ship.velocity.dx += math.sin(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy -= math.cos(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
            
        for asteroid in self.asteroids:
            asteroid.visiable = 50

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        self.ship.advance()
        
        for bullet in self.bullets:
            bullet.advance()
       
        for asteroid in self.asteroids:
            asteroid.advance()
            
        # TODO: Check for collisions
        self.check_collisions()


    def check_collisions(self):
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and abs(bullet.center.y - asteroid.center.y) < too_close):
                        bullet.alive = False
                        self.asteroids += asteroid.hit()
        
        for asteroid in self.asteroids:
            if self.ship.alive and asteroid.alive:
                too_close = self.ship.radius + asteroid.radius

                if (abs(self.ship.center.x - asteroid.center.x) < too_close and abs(self.ship.center.y - asteroid.center.y) < too_close):
                    self.ship.alive = False
                    self.asteroids += asteroid.hit()   
                
        self.cleanup_zombies()

    def cleanup_zombies(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.rotate('l')

        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate('r')

        if arcade.key.UP in self.held_keys:
            self.ship.go('u')

        if arcade.key.DOWN in self.held_keys:
            self.ship.go('d')

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys:
            pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet(self.ship.angle, self.ship.center, self.ship.velocity)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
