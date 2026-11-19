# Game launch (#8)
# Entry point: run this file to start the game.
# Contains the start menu loop with an option to start or exit.
import pygame
from Shared.settings import WIDTH, HEIGHT, FPS, BG_COLOR
import menu
from Models.ball import ball
from Models.field import GameField
from Models.game_over import game_over_screen
from Models.paddle import Paddle
from Models.game import collision_detection, third_wall_collision_detection, wall_collision_detection

def main():
    """
    Main entry point for the Pong game.
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
   
    
    # 1. Run Menu
    action = menu.show_menu(screen, clock)
    
    # 2. Handle action
    if action == 'QUIT':
        pygame.quit()
        return
        
    elif action == 'PLAY':
        print("Starting the game...")
        # TODO: Initialize Paddles, Ball, and Game Loop here
        # (Insert your friend's paddle logic and ball logic here)
        player_paddle  = Paddle(20, 100, 10, 40, 350)
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
            player_paddle.update(pygame.key.get_pressed(), screen.get_rect())
            player_paddle.draw(screen)
            collision_detection(game_ball, player_paddle)
            wall_collision_detection(game_ball, game_field)
            third_wall_collision_detection(game_ball, game_field)

            if goal_side == 'left':
                result = game_over_screen(screen, "Right player")
                if result == 'RESTART':
                    game_ball.reset()
                    continue
                else: 
                    running = False
                    break
            elif goal_side == 'right':
                result = game_over_screen(screen, "Left player")
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