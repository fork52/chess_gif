from .create_frame import Chess_Image
from chess import pgn as pgn_reader
from chess import flip_vertical,Board
from typing import Iterable
from pprint import pprint
from pygifsicle import optimize as optimize_gif
from imageio import mimwrite
import os
import errno
from pkg_resources import resource_string
from .constants import ice_theme

class Gifmaker:
    '''
    Class for converting a chess ``PGN`` file to a ``GIF``.

    Parameters
    ----------
    pgn_file_path : str
        Path to the source PGN file to be convereted to GIF.

    Other Parameters
    ----------------
    colors : `tuple`, optional
        colors for white and black squares.. Default `` ('#dee3e6','#8ca2ad') ``.
    piece_theme : `str`, optional
        Choose one of the available piece_themes.
        Default ``merida``.
    side : `int`, optional
        Size of the side of a single chess-square in pixels. Default ``70``.
    h_margin : `int`, optional
        Black horizontal margin around the chess_board to be rendered in the GIF. 
        Default ``0``.
    v_margin : `int`, optional
        Black vertical margin around the chess_board to be rendered in the GIF. 
        Default ``0``.


    Example
    --------
    >>> from chess_gif.gif_maker import Gifmaker
    >>> obj = Gifmaker('game.pgn')
    >>> obj.make_gif('chess_game.gif)

    | ``chess_game.gif`` will be created in the current working directory.

    .. image:: ../docs/chess_game.gif

    |
    | The resolution of the images is adjustable by changing the side keyword argument.


    Note
    ----
        Following are the available piece-themes:

        **{ 'alpha', 'california' , 'cardinal' , 'cburnett' , 'chess7' , 'chessnut' , 'companion' , 'dubrovny' , 'fantasy' , 'fresca' , 'gioco' , 'icpieces' , 'kosal' , 'leipzig' , 'letter' , 'libra' , 'maestro' , 'merida' , 'mono' , 'pirouetti' , 'pixel' , 'reillycraig' , 'riohacha' , 'shapes' , 'spatial' , 'staunty' , 'tatiana' }**.
        
        These are the publicly available themes taken from **lichess.org's** amazing `repository-lila <https://github.com/ornicar/lila>`_ .

    '''



    def __init__(self, 
                pgn_file_path:str, 
                **kwargs:dict ):
        """Constructor method
        """

        # Set all the kwargs to default values if not provided
        kwargs.setdefault('colors', ice_theme)
        kwargs.setdefault('piece_theme','merida')
        kwargs.setdefault('side',70)
        kwargs.setdefault('h_margin',0)
        kwargs.setdefault('v_margin',0)

        pprint(kwargs)
        
        self.kwargs = kwargs

        # Check if file exists
        if not os.path.isfile(pgn_file_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pgn_file_path) 

        self.pgn_file_path = pgn_file_path


    def make_gif( self, gif_file_path:str = 'chess.gif' ):
        '''
        Makes the gif of the loaded pgn at the specified destination file path.

        Parameters
        ----------
        gif_file_path : str
            Destination directory to store the gif file.

        '''
        
        pgn_file = open(self.pgn_file_path)

        chess_game = pgn_reader.read_game(pgn_file)

        # Stores the headers in the pgn
        self.header_info = chess_game.headers

        # self.white_player = self.header_info['White']
        # self.black_player = self.header_info['Black']
        # self.BlackElo = self.header_info['BlackElo']
        # self.WhiteElo = self.header_info['WhiteElo']

        # print('White Player:',self.white_player)
        # print('Black Player:',self.black_player,'\n')

        # print( 'WhiteElo:', self.WhiteElo )
        # print( 'BlackElo:', self.BlackElo )

        # get string notation of the game
        # print(str( chess_game.game()).replace('\n','') )

        #get the start position
        # print(chess_game.board() )

        self.white_timeline = []
        self.black_timeline = []
        self.board_states = [Board()]

        main_line_itr = chess_game.mainline()
        for node in main_line_itr:
            if node.parent is not None:
                current_move = node.san()
                time_left = node.clock()

                current_board = node.board()
                self.board_states.append(current_board)
                
                if current_board.turn:
                    self.white_timeline.append(time_left)
                else:
                    self.black_timeline.append(time_left)

                # White's perspective
                # print('\n',current_board)  

                # # Black's perspective
                # print( '\n',current_board.transform( flip_vertical ))
        
        obj = Chess_Image(
                        colors = self.kwargs['colors'],
                        side = self.kwargs['side'], 
                        piece_theme = self.kwargs['piece_theme'],
                        h_margin=self.kwargs['h_margin'],
                        v_margin=self.kwargs['v_margin']
            )
        

        frames =  list( map(lambda x:obj.create_position(x) , self.board_states ) )

        mimwrite( 
            gif_file_path,
            frames, duration = 1,
            subrectangles = True ,
            palettesize = 256 # default = 256
        )
        
        optimize_gif(gif_file_path)

        # print(self.white_timeline)
        # print(self.black_timeline)


if __name__ == "__main__":
'
    # pgn_file_path = r'data\pgn\lichess_pgn_2020.08.01_Mrunank_vs_Blindtakes34.E2og9BtO.pgn'
    # obj = Gifmaker(pgn_file_path, piece_theme = 'merida' )
    # obj.make_gif('hello.gif')

    pass



