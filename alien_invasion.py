import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet



class AlienInvasion:
    '''Overall class to manage game asserts and behavior.'''
    def __init__(self):
        '''Initialize the game and create game resources.'''
        #Initialize pygame
        pygame.init()  
        #Timer and Settings
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Fullscreen mode
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #Create the screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Create the Ship
        self.ship = Ship(self)
        
        self.bullets = pygame.sprite.Group()

        

    def run_game(self):
        '''Start the main loop for the game'''  
        while True:
            self._check_events()
            self.ship.update()
            #Bullet
            self.bullets.update()
            self._update_screen()
            #clock update 60 events per second
            self.clock.tick(6000)
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            #Make the most recently drawn screen visible.
            pygame.display.flip()


    def _check_events(self):
        '''Detecting keystroke events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    #Move the ship to the right.
                    self.ship.moving_down = False
                    self.ship.rect.y += 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                    self.ship.rect.y -= 1
                    
            elif event.type == pygame.K_RIGHT:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                    self.ship.rect.x += 1

            elif event.type == pygame.K_LEFT:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    self.ship.rect.x -= 1


    def _check_keydown_events(self,event):
        ''''''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.meoving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)



    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        #Bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()
        pygame.display.flip()




if __name__ == "__main__":
    #make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
    

