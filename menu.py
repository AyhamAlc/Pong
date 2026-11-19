import pygame

def show_menu(screen, clock):
    # load button images
    play_img = pygame.image.load("images/buttons/play/play.png")
    play_hover_img = pygame.image.load("images/buttons/play/play_outline.png")
    play_shiny_img = pygame.image.load("images/buttons/play/shiny/play_shiny.png") # load shiny
    
    quit_img = pygame.image.load("images/buttons/quit/quit.png")
    quit_hover_img = pygame.image.load("images/buttons/quit/quit_outline.png")
    quit_shiny_img = pygame.image.load("images/buttons/quit/shiny/quit_shiny.png")
    
    # just stretch images, might look weird but it works
    play_img = pygame.transform.scale(play_img, (200, 80))
    play_hover_img = pygame.transform.scale(play_hover_img, (200, 80))
    play_shiny_img = pygame.transform.scale(play_shiny_img, (200, 80))
    
    quit_img = pygame.transform.scale(quit_img, (200, 80))
    quit_hover_img = pygame.transform.scale(quit_hover_img, (200, 80))
    quit_shiny_img = pygame.transform.scale(quit_shiny_img, (200, 80))
    
    # hardcoded positions
    play_rect = pygame.Rect(300, 200, 200, 80)
    quit_rect = pygame.Rect(300, 320, 200, 80)
    
    font = pygame.font.SysFont("arial", 60)
    
    # use a counter for blinking effect
    blink_counter = 0 
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        # increase counter every frame
        blink_counter += 1 
        # reset counter to 0 after 60 frames (about 1 second)
        if blink_counter >= 60:
            blink_counter = 0
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if play_rect.collidepoint(mouse_pos):
                        return "PLAY"
                    if quit_rect.collidepoint(mouse_pos):
                        return "QUIT"
                        
        screen.fill((30, 30, 40))
        
        title = font.render("PONG", True, (255, 255, 255))
        screen.blit(title, (320, 80))
        
        # --- Draw Play Button ---
        if play_rect.collidepoint(mouse_pos):
            screen.blit(play_hover_img, play_rect)
        else:
            screen.blit(play_img, play_rect)
            
        # draw shiny layer only if counter is small (makes it blink)
        if blink_counter < 30:
            screen.blit(play_shiny_img, play_rect)
            
        # --- Draw Quit Button ---
        if quit_rect.collidepoint(mouse_pos):
            screen.blit(quit_hover_img, quit_rect)
        else:
            screen.blit(quit_img, quit_rect)
            
        if blink_counter < 30:
            screen.blit(quit_shiny_img, quit_rect)
            
        pygame.display.flip()
        clock.tick(60)