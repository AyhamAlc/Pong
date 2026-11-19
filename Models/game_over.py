import pygame

def game_over_screen(screen,winner):
    # Set up the game over screen
    font = pygame.font.SysFont("arial", 74)

    # Fill the screen with black
    while True:
        screen.fill((0, 0, 0))
        text = font.render(f"Game Over! {winner} wins!", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - text.get_height() // 2))
        hint = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        screen.blit(hint, (screen.get_width() // 2 - hint.get_width() // 2, screen.get_height() // 2 + text.get_height()))
        pygame.display.flip()
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'QUIT'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'RESTART'
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return 'QUIT'