import sys, pygame
import graphics, logic

pygame.init()
pygame.font.init()


screen = graphics.init()
clock = pygame.time.Clock()


def quit():
    pygame.quit()
    sys.exit()


def title() -> None:
    title_text = graphics.Text(
        "Tic Tac Toe", pygame.font.SysFont("papyrus", 140), (150, 50), screen
    )
    start_button = graphics.AnimatedButton(
        graphics.start_button_size,
        ((graphics.window_size[0] - graphics.start_button_size[0]) / 2, 400),
    )
    start_text = graphics.Text(
        "CLASSIC", pygame.font.SysFont("papyrus", 50), (20, 7), start_button.image
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                    start_text.surface = start_button.hover()
                else:
                    start_button.reset()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                        game()
                        break

        screen.fill(graphics.colors["pale_turquoise"])
        title_text.render()
        start_button.render()
        start_text.render()
        pygame.display.flip()
        clock.tick(60)
    return None


def game() -> None:
    """Start a new pvp tic tac toe classic game."""

    board = graphics.Board(logic.Grid())
    board.grid.reset()
    # dragging = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    for i in range(9):
                        piece = board.grid.pieces[i]
                        if piece.alias == graphics.Placeholder().alias and pygame.Rect(
                            piece.pos, graphics.piece_size
                        ).collidepoint(pygame.mouse.get_pos()):
                            if not board.grid.winner():
                                board.grid.move(i)
                    if board.grid.tie():
                        print("It's a tie!")
                    else:
                        print(
                            "The winner is", board.grid.winner()
                        ) if board.grid.winner() is not None else None
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    print("Exit to menu...")
                    board.grid.reset()
                    title()
                    break

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
        pygame.display.flip()
        # clock.tick(120)
    return None


title()
