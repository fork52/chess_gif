from typing import Iterable,List
from PIL import Image , ImageDraw
import os , sys

vipshome = 'C:\\pyVips\\vips-dev-8.9\\bin'
os.environ['PATH'] = vipshome + ';' + os.environ['PATH']

from pyvips import Image as VipsImage


# Setting path to binaries


class Chess_Image:
    def __init__(self, colors:tuple , side:int = 70):
        """Creates an single Chess frame.

        :param colors: ( 'white_color' , 'black_color') 
        :param side: side of single square of the chess_board in **pixels**
        :returns: Object of class Chess_Image
        """
        self.white_color , self.black_color = colors
        self.side = side

    def create_board(self):
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

        self.board_img.save('Images/result.png')


class Chess_Pieces:
    """Loads the Chess_Pieces from memory in PIL objects.

    :param colors: ( 'white_color' , 'black_color') 
    :param side: side of single square of the chess_board in **pixels**
    :returns: Object of class Chess_Image
    """
    def __init__(self,theme:str):
        piece_dir = os.path.join( 'data','piece',theme)

        self.pieces ={
            'r':'bR.svg' , 'q':'bQ.svg' , 'n':'bN.svg' , 'k' : 'bK.svg' , 'p':'bP.svg',
            'R':'wR.svg' , 'Q':'wQ.svg' , 'N':'wN.svg' , 'K' : 'wK.svg' , 'P':'wP.svg'
        }

        # read the image
        for piece in self.pieces:
            piece_path = os.path.join(piece_dir,self.pieces[piece])
            image = VipsImage.thumbnail(piece_path, 200, height=200)
            image.write_to_file(f"Images/{self.pieces[piece][:2]}.png")



if __name__ == "__main__":
    obj = Chess_Image( ('#ffe0b3','#802b00') )
    obj.create_board()
    obj2 = Chess_Pieces('gioco')
    