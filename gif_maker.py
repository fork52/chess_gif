from create_frame import Chess_Image
from chess import pgn as pgn_reader
from chess import flip_vertical,Board
from typing import Iterable
from pprint import pprint
from pygifsicle import optimize as optimize_gif
from imageio import mimwrite
import os
import errno

class Gifmaker:
    '''
    Class for converting a chess PGN file to a GIF 
    '''

    def __init__(self, pgn_file_path:str, **kwargs:dict ):
        '''
        Constructor of Gifmaker class for setting up options.
        :param pgn_file_path: Path to the pgn file.
        :type pgn_file_path: str

        :Example:

        >>> import Gifmaker
        >>> obj = Gifmaker('game.pgn')
        >>> obj.make_gif('chess.gif)
        '''

        # Set all the kwargs to default values if not provided
        kwargs.setdefault('colors', ( '#9e3725','#ffe0b3' ) )
        kwargs.setdefault('piece_theme','merida')
        kwargs.setdefault('side',70)

        pprint(kwargs)
        
        #: Contains the kwargs for the object
        self.kwargs = kwargs

        if not os.path.isfile(pgn_file_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pgn_file_path) 

        #: Path to the pgn file 
        self.pgn_file_path = pgn_file_path


    def make_gif(self, gif_file_path:str = 'chess.gif' )->None:
        '''
        Makes a gif at the specified destination file path.

        :param gif_file_path: Directory to store the gif file.
        :type pgn_file_path: str
        '''
        
        pgn_file = open(self.pgn_file_path)

        chess_game = pgn_reader.read_game(pgn_file)

        #: Stores the headers in the pgn
        self.header_info = chess_game.headers

        self.white_player = self.header_info['White']
        self.black_player = self.header_info['Black']
        self.BlackElo = self.header_info['BlackElo']
        self.WhiteElo = self.header_info['WhiteElo']

        print('White Player:',self.white_player)
        print('Black Player:',self.black_player,'\n')

        print( 'WhiteElo:', self.WhiteElo )
        print( 'BlackElo:', self.BlackElo )

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
                        piece_theme = self.kwargs['piece_theme']
            )
        

        frames =  list( map(lambda x:obj.create_position(x) , self.board_states ) )

        # frames[0].save ( 
        #        gif_file_path,
        #        save_all=True,
        #        append_images=frames[1:],
        #        duration=800,
        #        loop=0
        #     )

        mimwrite( 
            gif_file_path,
            frames, duration = 1,
            subrectangles = True ,
            palettesize = 256 # default = 256
        )
        optimize_gif(gif_file_path)

        print(self.white_timeline)
        print(self.black_timeline)


if __name__ == "__main__":

    # pgn_file_path = 'data/pgn/MikelOjda_vs_iDontTalkiDoIt_2020.03.19.pgn'
    # pgn_file_path = 'data\\pgn\\lichess_pgn_2020.08.03_Mrunank_vs_prem_singh_bhati.gKZs5DjG.pgn'
    pgn_file_path = r'data\pgn\lichess_pgn_2020.08.01_Mrunank_vs_Blindtakes34.E2og9BtO.pgn'

    yellow_green = (  '#ffffdd','#86a666')
    brown_off_white = ('#f0d9b5', '#b58863')
    blue_white = ('#dee3e6','#8ca2ad')
    

    obj = Gifmaker(pgn_file_path, colors=blue_white, piece_theme = 'merida' )
    obj.make_gif('hello.gif')

