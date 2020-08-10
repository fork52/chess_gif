from typing import Iterable,List
from PIL import Image , ImageDraw
from pprint import pprint
import os 
from pyvips import Image as VipsImage
from chess import Board

class Chess_Image:
    def __init__(self, colors:tuple , side:int = 60,theme:str = 'merida'):
        """
        Creates frame for Chess Gif.
        :param colors: ( white_color , black_color) 
        :param side: side of single square of the chess_board in **pixels**
        :returns: Object of class Chess_Image
        """
        self.white_color , self.black_color = colors
        self.side = side
        self.theme = theme
        self.pieces = Chess_Pieces(theme, round(side) )
        self.create_initial_board()


    def create_initial_board(self)->Image:
        '''
        Returns a PIL image object of the base chess board without pieces
        '''
        self.board_size =  8 * self.side
        self.vertical_margin = round( 0.15 * self.board_size  )
        self.horizantal_margin = round(0.02 * self.board_size)

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
                if (i+j) % 2 == 0:
                    color = self.white_color
                else:
                    color = self.black_color
                ImageDrawer.rectangle( (x1,y1,x2,y2), fill =color, outline =color)

        self.board_img.save('Images/result.png') # To be removed 
        return self.board_img

    def create_position(self,current_position:Board)->Image:
        '''
        Renders the current_postion on to the chess board
        '''
        board_list = list( map( lambda s:s.split(),str(current_position).split('\n')) )
        base_img = self.board_img.copy()
        for r in range(8):
            for c in range(8):
                piece = board_list[r][c]
                if  piece!= '.':
                    piece_img = self.pieces.piece_imgs[piece]
                    base_img.paste( piece_img, self.get_location(r,c), mask=piece_img )
        base_img.save('board_pieces.png') #To be removed
        return base_img

    def get_location(self,row:int,col:int):
            x = self.horizantal_margin + col*self.side
            y = self.vertical_margin + row*self.side
            return x,y


class Chess_Pieces:
    """
    Loads the Chess_Pieces from memory in PIL objects.
    """
    def __init__(self,theme:str , size:int = 70 ):
        piece_dir = os.path.join( 'data','piece', theme )

        #piece_mapper
        self.pieces_map ={
            'r':'bR' , 'q':'bQ' , 'n':'bN' , 'k' : 'bK' , 'p':'bP', 'b':'bB',
            'R':'wR' , 'Q':'wQ' , 'N':'wN' , 'K' : 'wK' , 'P':'wP', 'B':'wB'
        }

        # Read the .svg images and save them as .png
        for piece in self.pieces_map:
            piece_path = os.path.join(piece_dir,  self.pieces_map[piece]+'.svg')
            image = VipsImage.thumbnail(piece_path, size , height=size)
            image.write_to_file(f"Images/{ self.pieces_map[piece]}.png")
        
        # Read the png images and store them in piece_imgs dictionary
        self.piece_imgs = {}
        for piece in  self.pieces_map:
            self.piece_imgs[piece] = Image.open(f"Images/{ self.pieces_map[piece]}.png")
    
if __name__ == "__main__":
    obj = Chess_Image( ('#ffe0b3','#802b00') )
    obj.create_position(Board())

