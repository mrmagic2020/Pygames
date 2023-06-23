from __future__ import annotations
from typing import TYPE_CHECKING

import os, pygame
from enum import Enum

if TYPE_CHECKING:
    import logic


pygame.font.init()

piece_size = (200, 200)
board_size = window_size = (800, 800)
start_button_size = (200, 80)
img_path = {
    "Placeholder": os.path.join("Assets", "Placeholder.png"),
    "Cross": os.path.join("Assets", "cross.png"),
    "Circle": os.path.join("Assets", "circle.png"),
    "Board": os.path.join("Assets", "board.png"),
    "Buttons": {
        "button_rect_fillet_blue": os.path.join(
            "Assets", "Buttons", "button_rect_fillet_blue.png"
        ),
        "button_rect_fillet_blue_hover": os.path.join(
            "Assets", "Buttons", "button_rect_fillet_blue_hover.png"
        ),
    },
}
colors = {"black": (0, 0, 0), "pale_turquoise": (175, 238, 238)}
draw = {"rect": pygame.draw.rect}


def init() -> pygame.Surface:
    """Initialise the graphics.
    Returns the screen object.
    """
    global screen
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Tic Tac Toe")
    return screen


def clearScreen(background="pale_turquoise") -> None:
    screen.fill(colors[background])
    pygame.display.flip()
    return None


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
        self,
        index: int = -1,
        image=pygame.image.load(img_path["Placeholder"]),
        scale=piece_size,
    ) -> None:
        self.index = index
        self.image = pygame.transform.scale(image, scale)
        self.pos = getPos(index)
        self.alias = "."


class Cross:
    def __init__(
        self,
        index: int = -1,
        image=pygame.image.load(img_path["Cross"]),
        scale=piece_size,
    ) -> None:
        self.index = index
        self.image = pygame.transform.scale(image, scale)
        self.pos = getPos(index)
        self.alias = "X"

    def other(self):
        return Circle(self.index)


class Circle:
    def __init__(
        self,
        index: int = -1,
        image=pygame.image.load(img_path["Circle"]),
        scale=piece_size,
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
        """Draws the board onto the screen. Does not update display."""
        screen.fill(colors["pale_turquoise"], self.image.get_rect())
        screen.blit(self.image, self.image.get_rect())

        for piece in self.grid.pieces:
            screen.blit(piece.image, piece.pos)
            # if piece != None:
            #     screen.blit(piece.image, piece.pos)
            # else:
            #     placeholder = Placeholder(index)
            #     screen.blit(placeholder.image, placeholder.rect)
            # index += 1

        # pygame.display.flip()
        return None


class Text:
    """
    `content` the text being displayed

    `font` the font being used

    `pos` the position relative to `surface`

    `surface` the surface the text will be rendered on
    """

    def __init__(
        self,
        content: str,
        font: pygame.font.Font,
        pos: tuple[int, int],
        surface: pygame.Surface,
        color: tuple[int, int, int] = colors["black"],
        background: pygame.Color = None,
    ) -> None:
        self.content = content
        self.pos = pos
        self.font = font
        self.color = color
        self.background = background
        self.surface = surface
        return None

    def render(self) -> None:
        """Draws the text onto the screen. Does not update display."""
        surf = self.font.render(self.content, True, self.color, self.background)
        self.surface.blit(surf, self.pos)
        return None


class Interactive(Enum):
    BUTTON = 0
    BUTTON_ANIMATED = 1


class Button:
    def __init__(
        self,
        scale: tuple[int, int],
        pos: tuple[int, int],
        image: pygame.Surface = pygame.image.load(
            img_path["Buttons"]["button_rect_fillet_blue"]
        ),
    ) -> None:
        self.type = Interactive.BUTTON
        self.image = pygame.transform.scale(image, scale)
        self.rect = pygame.rect.Rect(pos, scale)
        self.pos = pos
        return None

    def render(self) -> None:
        """Draws the button onto the screen. Does not update display."""
        screen.fill(colors["pale_turquoise"], pygame.rect.Rect(self.rect))
        screen.blit(self.image, self.pos)
        return None


class AnimatedButton(Button):
    def __init__(
        self,
        scale: tuple[int, int],
        pos: tuple[int, int],
        image: pygame.Surface = pygame.image.load(
            img_path["Buttons"]["button_rect_fillet_blue"]
        ),
        hover_image: pygame.Surface = pygame.image.load(
            img_path["Buttons"]["button_rect_fillet_blue_hover"]
        ),
    ) -> None:
        super().__init__(scale, pos, image)
        self.type = Interactive.BUTTON_ANIMATED
        self.isHover = False
        self.hover_image = pygame.transform.scale(hover_image, scale)
        return None

    def render(self) -> None:
        screen.fill(colors["pale_turquoise"], pygame.rect.Rect(self.rect))
        image = self.image
        if self.isHover:
            image = self.hover_image
        screen.blit(image, self.pos)
        return None

    def reset(self) -> pygame.Surface:
        self.isHover = False
        return self.image

    def hover(self) -> pygame.Surface:
        self.isHover = True
        return self.hover_image

    def press(self) -> pygame.Surface:
        return None
