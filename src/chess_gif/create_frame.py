from typing import Tuple
from PIL import Image, ImageDraw
import os
from pyvips import Image as VipsImage
import chess
from chess import Board
from importlib import resources


class ChessImage:
    """
    Creates Single Image frames for rendering the GIFs
    as per requirements.

    Parameters
    ----------
    colors : tuple
        Specify white and black square color in the format
        ``(white_color ,black_color)``.

    side : int, optional
        Side of **single square** of the chess_board in **pixels**.
        Defaults to ``70``.

    piece_theme: str, optional.
        Choose one of the available piece-themes mentioned in the notes below.
        Defaults to ``merida``.

    h_margin : `int`, optional
        Black horizontal margin around the chess_board to be rendered in the GIF.
        Default ``0``.

    v_margin : `int`, optional
        Black vertical margin around the chess_board to be rendered in the GIF.
        Default ``0``.

    """

    def __init__(
        self,
        colors: tuple,
        side: int = 70,
        piece_theme: str = "merida",
        h_margin: int = 0,
        v_margin: int = 0,
    ):

        root_path = resources.files("chess_gif")
        self.white_color, self.black_color = colors

        # Validating side of the square
        assert isinstance(side, int), "Board `side` should be an int."
        assert side > 10, "Board `side` should be greater than 10 pixels."

        #: side of one square on the chessboard in pixels
        self.side = side

        # Validating piece theme
        assert isinstance(piece_theme, str), "piece_theme should be a string."
        valid_piece_themes = os.listdir(os.path.join(root_path, "data", "piece"))

        piece_theme_stmt = f"{piece_theme} is not a valid piece_theme. Choose one of the following piece themes:\n{valid_piece_themes} ."
        assert piece_theme in valid_piece_themes, piece_theme_stmt
        self.piece_theme = piece_theme

        # Load the pieces
        self.pieces = PieceImages.get_piece_image_dict(piece_theme, round(side))

        # Set horizontal and vertical margin
        self.horizantal_margin = h_margin
        self.vertical_margin = v_margin

        self.create_initial_board()

    def create_initial_board(self) -> Image.Image:
        """
        Returns a PIL image object of the base chess board without pieces.
        """

        #: Size of the 8x8 square chess-board
        self.board_size = 8 * self.side
        # self.vertical_margin = round( 0.15 * self.board_size  )
        # self.horizantal_margin = round(0.02 * self.board_size)

        # (Width , Height)
        self.img_size = (
            self.board_size + 2 * self.horizantal_margin,
            self.board_size + 2 * self.vertical_margin,
        )

        # Atrribute which will have the base image of the board
        self.board_img = Image.new("RGB", self.img_size)
        ImageDrawer = ImageDraw.Draw(self.board_img)

        for i in range(8):
            y1 = self.vertical_margin + self.side * i
            y2 = y1 + self.side
            for j in range(8):
                x1 = self.horizantal_margin + self.side * j
                x2 = x1 + self.side
                if (i + j) % 2 == 0:
                    color = self.white_color
                else:
                    color = self.black_color
                ImageDrawer.rectangle((x1, y1, x2, y2), fill=color, outline=color)

        return self.board_img

    def create_board_image(self, board: Board) -> Image.Image:
        """
        Renders passed current_postion on to the chess board.
        """
        board_img = self.board_img.copy()
        for rank_index in range(7, -1, -1):
            for file_index in range(8):
                piece = board.piece_at(chess.square(rank_index, file_index))
                if piece is not None:
                    piece_img = self.pieces[piece]
                    board_img.paste(piece_img, self._get_location(7 - file_index, rank_index), mask=piece_img)
        return board_img

    def _get_location(self, row: int, col: int) -> Tuple[int, int]:
        x = self.horizantal_margin + col * self.side
        y = self.vertical_margin + row * self.side
        return x, y


class PieceImages:
    """
    Class to represent a piece image
    """
    @staticmethod
    def get_piece_image_dict(piece_theme: str, size: int = 70):
        root_path = resources.files("chess_gif")
        piece_svg_dir_path = os.path.join(root_path, "data", "piece", piece_theme)

        # Maps pieces to their corresponding .svg filenames
        piece_symbol_to_imgname_dict = {
            chess.Piece(chess.ROOK, chess.BLACK): "bR",
            chess.Piece(chess.QUEEN, chess.BLACK): "bQ",
            chess.Piece(chess.KNIGHT, chess.BLACK): "bN",
            chess.Piece(chess.KING, chess.BLACK): "bK",
            chess.Piece(chess.PAWN, chess.BLACK): "bP",
            chess.Piece(chess.BISHOP, chess.BLACK): "bB",
            chess.Piece(chess.ROOK, chess.WHITE): "wR",
            chess.Piece(chess.QUEEN, chess.WHITE): "wQ",
            chess.Piece(chess.KNIGHT, chess.WHITE): "wN",
            chess.Piece(chess.KING, chess.WHITE): "wK",
            chess.Piece(chess.PAWN, chess.WHITE): "wP",
            chess.Piece(chess.BISHOP, chess.WHITE): "wB",
        }

        #: Dictionary where pieces are the keys and corresponding PIL Images are the values
        piece_to_img_dict = dict()

        # Read the available piece theme's .svg images and save them as .png images of appropriate size
        for piece in piece_symbol_to_imgname_dict:
            piece_svg_path = os.path.join(
                piece_svg_dir_path, piece_symbol_to_imgname_dict[piece] + ".svg"
            )
            image = VipsImage.thumbnail(piece_svg_path, size, height=size)
            image_name = piece_symbol_to_imgname_dict[piece] + ".png"
            image.write_to_file(os.path.join(root_path, "Images", image_name))

            piece_to_img_dict[piece] = Image.open(
                os.path.join(root_path, "Images", image_name)
            )

        return piece_to_img_dict

if __name__ == "__main__":
    obj = ChessImage(("#ffe0b3", "#802b00"), side=15, piece_theme="merida")
    obj.create_board_image(Board())
