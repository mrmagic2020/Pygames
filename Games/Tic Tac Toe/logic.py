import re, pygame
import graphics

from typing import TypeAlias


Piece: TypeAlias = graphics.Cross | graphics.Circle | graphics.Placeholder

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?..",
)
        

class Grid:
    def __init__(self, pieces: list[Piece] = [graphics.Placeholder(i) for i in range(0, 9)], starting_mark: Piece = graphics.Cross()) -> None:
        self.pieces = pieces
        self.starting_mark = starting_mark
    
    def reset(self) -> None:
        self.pieces = [graphics.Placeholder(i) for i in range(0, 9)]
        return None

    def current_mark(self) -> Piece:
        # define identifier list for type check
        identifier = [type(piece) for piece in self.pieces]
        if identifier.count(graphics.Cross) == identifier.count(graphics.Circle):
            return self.starting_mark
        else:
            return self.starting_mark.other()

    def move(self, index: int) -> bool:
        """Make a move."""
        if self.pieces[index].alias == graphics.Placeholder().alias:
            self.pieces[index] = graphics.Cross(index) if self.current_mark().alias == graphics.Cross().alias else graphics.Circle(index)
            return True
        return False

    def toString(self) -> str:
        """Returns the string representative of the current position."""
        string = ""
        for piece in self.pieces:
            string += piece.alias
        return string
    
    def winner(self) -> str | None:
        """Returns the winning mark of the current position, or None if nobody is winning."""
        for pattern in WINNING_PATTERNS:
            if re.match(pattern.replace("?", graphics.Cross(0).alias), self.toString()):
                return graphics.Cross(0).alias
            if re.match(pattern.replace("?", graphics.Circle(0).alias), self.toString()):
                return graphics.Circle(0).alias
        return None

    def tie(self) -> bool:
        return self.winner() == None and [type(piece) for piece in self.pieces].count(graphics.Placeholder) == 0
