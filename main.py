# Game launch (#8)
# Entry point: run this file to start the game.
# Contains the start menu loop with an option to start or exit.
import pygame
from Shared.settings import WIDTH, HEIGHT, FPS, BG_COLOR
from menu import Menu
from Models.ball import ball
from Models.field import GameField
from Models.game_over import game_over_screen

def main():
    """
    Main entry point for the Pong game.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
    
    # 1. Run Menu
    menu = Menu(screen)
    action = menu.run()
    
    # 2. Handle action
    if action == 'QUIT':
        pygame.quit()
        return
        
    elif action == 'PLAY':
        print("Starting the game...")
        # TODO: Initialize Paddles, Ball, and Game Loop here
        # (Insert your friend's paddle logic and ball logic here)
        game_ball = ball()
        game_field = GameField(0, 0, WIDTH, HEIGHT)
        running = True
        dt = 0
        # --- Temporary placeholder loop so you can see it works ---
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            screen.fill(BG_COLOR)
            # Draw game objects 
            game_field.draw(screen)
            goal_side = game_field.check_goal(game_ball)

            if goal_side == 'left':
                result = game_over_screen(screen, "Game Over")
                if result == 'RESTART':
                    game_ball.reset()
                    continue
                else: 
                    running = False
                    break
            elif goal_side == 'right':
                result = game_over_screen(screen, "You win")
                if result == 'RESTART':
                    game_ball.reset()
                    continue
                else: 
                    running = False
                    break
            game_ball.ball_movement()
            game_ball.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)
            
    pygame.quit()

if __name__ == "__main__":
    main()