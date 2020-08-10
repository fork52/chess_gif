from chess import pgn as pgn_reader
from chess import flip_vertical,Board
from typing import Iterable
from pprint import pprint
from create_frame import Chess_Image

class Gifmaker:
    '''
    Class for converting a chess PGN file to a GIF 
    '''
    def read_pgn( self, pgn_file_path : str ):
        pgn_file = open(pgn_file_path)

        chess_game = pgn_reader.read_game(pgn_file)

        # Get the meta in formation of the game
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
        
        obj = Chess_Image(('#ffe0b3','#802b00'),side=50 )
        frames =  list( map(lambda x:obj.create_position(x) , self.board_states ) )

        frames[0].save('chess.gif',
               save_all=True,
               append_images=frames[1:],
               duration=500,
               loop=0
            )

        print(self.white_timeline)
        print(self.black_timeline)

    def remove_line_breaks(self):
        pass

if __name__ == "__main__":

    # pgn_file_path = 'data/pgn/MikelOjda_vs_iDontTalkiDoIt_2020.03.19.pgn'
    pgn_file_path = r'data\pgn\lichess_pgn_2020.08.03_Mrunank_vs_prem_singh_bhati.gKZs5DjG.pgn'
    # pgn_file_path = r'data\pgn\lichess_pgn_2020.08.01_Mrunank_vs_Blindtakes34.E2og9BtO.pgn'

    obj = Gifmaker()
    obj.read_pgn(pgn_file_path)

