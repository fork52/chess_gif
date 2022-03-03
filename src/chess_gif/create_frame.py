from typing import Iterable, List, Tuple
from PIL import Image , ImageDraw
from pprint import pprint
import os
from pyvips import Image as VipsImage
from chess import Board

class Chess_Image:
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
            self, colors:tuple,
            side:int = 70,
            piece_theme:str = 'merida',
            h_margin:int = 0,
            v_margin:int = 0
     ):

        # Changing the directory to read data
        cwd = os.getcwd()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        self.white_color , self.black_color = colors

        # Validating side of the square
        assert isinstance(side, int),'side should be an int.'
        assert side > 10 , 'side should be greater than 10 pixels.'
        #: side of one square on the chessboard in pixels
        self.side = side

        # Validating piece theme
        assert isinstance( piece_theme ,str ),'piece_theme should be a string.'
        print(os.getcwd())
        valid_piece_themes =  os.listdir('data/piece/')   # Get all the available piece_themes
        piece_theme_stmt = f'{piece_theme} is not a valid piece_theme. Choose one of the following piece themes:\n{valid_piece_themes} .'
        assert piece_theme in valid_piece_themes, piece_theme_stmt
        self.piece_theme = piece_theme
        # Load the pieces 
        self.pieces = Chess_Pieces(piece_theme, round(side) )

        #Set horizontal and vertical margin
        self.horizantal_margin = h_margin
        self.vertical_margin = v_margin


        self.create_initial_board()

        os.chdir(cwd)


    def create_initial_board(self) -> Image:
        '''
        Returns a PIL image object of the base chess board without pieces.
        '''

        #: Size of the 8x8 square chess-board
        self.board_size =  8 * self.side
        # self.vertical_margin = round( 0.15 * self.board_size  )
        # self.horizantal_margin = round(0.02 * self.board_size)

        # (Width , Height)
        self.img_size = ( 
                self.board_size + 2 * self.horizantal_margin,
                self.board_size + 2 * self.vertical_margin
             )
        
        # Atrribute which will have the base image of the board
        self.board_img = Image.new( "RGB", self.img_size  )
        ImageDrawer = ImageDraw.Draw(self.board_img)

        for i in range(8):
            y1 = self.vertical_margin + self.side * i
            y2 = y1 + self.side
            for j in range(8):
                x1 = self.horizantal_margin + self.side * j
                x2 =  x1 + self.side
                if (i + j) % 2 == 0:
                    color = self.white_color
                else:
                    color = self.black_color
                ImageDrawer.rectangle( (x1,y1,x2,y2), fill = color, outline =color)

        # self.board_img.save('Images/result.png') # To be removed 
        return self.board_img



    def create_position(self, current_position:Board) -> Image:
        '''
        Renders passed current_postion on to the chess board.
        '''
        board_list = list(map(lambda s:s.split(),str(current_position).split('\n')) )
        base_img = self.board_img.copy()
        for r in range(8):
            for c in range(8):
                piece = board_list[r][c]
                if piece != '.':
                    piece_img = self.pieces.piece_imgs[piece]
                    base_img.paste(piece_img, self.get_location(r,c), mask = piece_img)
        return base_img

    def get_location(self, row:int, col:int) -> Tuple[int, int]:
            x = self.horizantal_margin + col*self.side
            y = self.vertical_margin + row*self.side
            return x, y


class Chess_Pieces:
    """
    Loads the Chess_Pieces from memory in PIL objects.
    """
    def __init__(self, piece_theme : str, size : int = 70):

        piece_dir = os.path.join('data', 'piece', piece_theme)

        #: Maps pieces to their corresponding .svg filenames
        self.pieces_map ={
            'r':'bR', 'q':'bQ', 'n':'bN', 'k':'bK', 'p':'bP', 'b':'bB',
            'R':'wR', 'Q':'wQ', 'N':'wN', 'K':'wK', 'P':'wP', 'B':'wB'
        }

        # Reads the available piece theme's .svg images and save them as .png images of appropraite size
        for piece in self.pieces_map:
            piece_path = os.path.join(piece_dir,  self.pieces_map[piece] + '.svg')
            image = VipsImage.thumbnail(piece_path, size , height=size)
            image.write_to_file(f"Images/{ self.pieces_map[piece]}.png")
        
        
        #: Dictionary where pieces are the keys and corresponding PIL Images are the values
        self.piece_imgs = dict()
        for piece in self.pieces_map:
            self.piece_imgs[piece] = Image.open(f"Images/{ self.pieces_map[piece]}.png")

    
if __name__ == "__main__":
    obj = Chess_Image( ('#ffe0b3','#802b00') , side ='2', piece_theme='dog' )
    obj.create_position(Board())

        
