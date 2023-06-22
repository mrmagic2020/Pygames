import sys, pygame
import graphics, logic

pygame.init()


def game():
    screen = graphics.init()
    clock = pygame.time.Clock()

    board = graphics.Board(logic.Grid())
    # dragging = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    for i in range(9):
                        piece = board.grid.pieces[i]
                        if piece.alias == graphics.Placeholder().alias and pygame.Rect(piece.pos, graphics.piece_size).collidepoint(pygame.mouse.get_pos()):
                            if not board.grid.winner():
                                board.grid.move(i)
                    if board.grid.tie(): print("It's a tie!")
                    else: print("The winner is", board.grid.winner()) if board.grid.winner() is not None else None
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    print("New Game...")
                    board.grid.reset()

            # if event.type == pygame.KEYDOWN:
            #     print(board.grid.winner())
        #     elif event.type == pygame.MOUSEBUTTONDOWN:
        #         if pygame.mouse.get_pressed(num_buttons=3)[0] and cross.image.get_rect().collidepoint(pygame.mouse.get_pos()):
        #             dragging = True
        #             mouse_x, mouse_y = pygame.mouse.get_pos()
        #             offset_x = mouse_x - cross.image.get_rect().x
        #             offset_y = mouse_y - cross.image.get_rect().y
        #     elif event.type == pygame.MOUSEBUTTONUP:
        #         if not pygame.mouse.get_pressed(num_buttons=3)[0]:
        #             print(cross.pos)
        
        # if not pygame.mouse.get_pressed(num_buttons=3)[0]:
        #     dragging = False
        # if dragging:
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     cross.pos = mouse_x - offset_x, mouse_y - offset_y
        
        board.render()
        clock.tick(30)

game()