from chess import pgn as pgn_reader
from typing import Iterable
# import chess

class Gifmaker:
    def read_pgn( self, pgn_file_path : str ):
        pgn = open(pgn_file_path)
        chess_game = pgn_reader.read_game(pgn)

        # Get the meta in formation of the game
        print(chess_game.headers)
        
        # get string notation of the game
        # print(chess_game.game())

        #get the start position
        print(chess_game.board() )

        main_line_itr = chess_game.mainline()
        for node in main_line_itr:
            if node.parent is not None:
                current_move = node.san()
                time_left = node.clock()
                current_board = node.board()
                # print( node.san() , node.clock()  )
                pass
                # print(node.board(),'\n')
    

if __name__ == "__main__":
    pgn_file_path = 'data/pgn/lichess_pgn_2020.08.03_Mrunank_vs_prem_singh_bhati.gKZs5DjG.pgn'
    obj = Gifmaker()
    obj.read_pgn(pgn_file_path)

