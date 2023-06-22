from __future__ import annotations
from typing import TYPE_CHECKING

import os, pygame

if TYPE_CHECKING:
    import logic


piece_size = (200, 200)
board_size = window_size = (800, 800)
img_path = {
    "Placeholder": os.path.join("Assets", "Placeholder.png"),
    "Cross": os.path.join("Assets", "cross.png"),
    "Circle": os.path.join("Assets", "circle.png"),
    "Board": os.path.join("Assets", "board.png"),
}
colours = {"pale_turquoise": (175, 238, 238)}


def init() -> pygame.Surface:
    """Initialise the graphics.
    Returns the screen object.
    """
    global screen
    screen = pygame.display.set_mode(window_size)
    return screen


def getPos(index: int) -> tuple[int, int]:
    pos = tuple()
    match index:
        case -1:
            pos = (None, None)
        case 0:
            pos = (50, 50)
        case 1:
            pos = (304, 50)
        case 2:
            pos = (565, 50)
        case 3:
            pos = (50, 304)
        case 4:
            pos = (304, 304)
        case 5:
            pos = (565, 304)
        case 6:
            pos = (50, 565)
        case 7:
            pos = (304, 565)
        case 8:
            pos = (565, 565)
    return pos


class Placeholder:
    def __init__(
        self, index: int = -1, image=pygame.image.load(img_path["Placeholder"]), scale=piece_size
    ) -> None:
        self.index = index
        self.image = pygame.transform.scale(image, scale)
        self.pos = getPos(index)
        self.alias = "."


class Cross:
    def __init__(
        self, index: int = -1, image=pygame.image.load(img_path["Cross"]), scale=piece_size
    ) -> None:
        self.index = index
        self.image = pygame.transform.scale(image, scale)
        self.pos = getPos(index)
        self.alias = "X"

    def other(self):
        return Circle(self.index)


class Circle:
    def __init__(
        self, index: int = -1, image=pygame.image.load(img_path["Circle"]), scale=piece_size
    ) -> None:
        self.index = index
        self.image = pygame.transform.scale(image, scale)
        self.pos = getPos(index)
        self.alias = "O"

    def other(self):
        return Cross(self.index)


class Board:
    def __init__(
        self,
        grid: logic.Grid,
        image=pygame.image.load(img_path["Board"]),
        scale=board_size,
    ) -> None:
        self.grid = grid
        self.image = pygame.transform.scale(image, scale)
    
    def render(self) -> None:
        screen.fill(colours["pale_turquoise"])
        screen.blit(self.image, self.image.get_rect())

        for piece in self.grid.pieces:
            screen.blit(piece.image, piece.pos)
            # if piece != None:
            #     screen.blit(piece.image, piece.pos)
            # else:
            #     placeholder = Placeholder(index)
            #     screen.blit(placeholder.image, placeholder.rect)
            # index += 1

        pygame.display.flip()
        return None
