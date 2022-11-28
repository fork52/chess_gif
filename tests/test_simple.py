import pytest
from chess_gif.gif_maker import Gifmaker
from chess_gif.constants import *

pgn_string = """
1. Nf3 Nf6 2. d4 e6 3. c4 b6 4. g3 Bb7 5. Bg2 Be7 6. O-O O-O
7. d5 exd5 8. Nh4 c6 9. cxd5 Nxd5 10. Nf5 Nc7 11. e4 d5
12. exd5 Nxd5 13. Nc3 Nxc3 14. Qg4 g6 15. Nh6+ Kg7 16. bxc3
Bc8 17. Qf4 Qd6 18. Qa4 g5 19. Re1 Kxh6 20. h4 f6 21. Be3 Bf5
22. Rad1 Qa3 23. Qc4 b5 24. hxg5+ fxg5 25. Qh4+ Kg6 26. Qh1
Kg7 27. Be4 Bg6 28. Bxg6 hxg6 29. Qh3 Bf6 30. Kg2 Qxa2 31. Rh1
Qg8 32. c4 Re8 33. Bd4 Bxd4 34. Rxd4 Rd8 35. Rxd8 Qxd8 36. Qe6
Nd7 37. Rd1 Nc5 38. Rxd8 Nxe6 39. Rxa8 Kf6 40. cxb5 cxb5
41. Kf3 Nd4+ 42. Ke4 Nc6 43. Rc8 Ne7 44. Rb8 Nf5 45. g4 Nh6
46. f3 Nf7 47. Ra8 Nd6+ 48. Kd5 Nc4 49. Rxa7 Ne3+ 50. Ke4 Nc4
51. Ra6+ Kg7 52. Rc6 Kf7 53. Rc5 Ke6 54. Rxg5 Kf6 55. Rc5 g5
56. Kd4 1-0 
"""

pgn_string_with_clks = """
[Event "Casual Bullet game"]
[Site "https://lichess.org/2DOVZodA"]
[Date "2022.03.16"]
[White "marakedward"]
[Black "Mrunank"]
[Result "0-1"]
[UTCDate "2022.03.16"]
[UTCTime "05:36:05"]
[WhiteElo "1807"]
[BlackElo "2199"]
[Variant "Standard"]
[TimeControl "60+0"]
[ECO "D38"]
[Opening "Queen's Gambit Declined: Ragozin Defense"]
[Termination "Time forfeit"]

1. d4 { [%clk 0:01:00] } 1... e6 { [%clk 0:01:00] } 2. c4 { [%clk 0:00:59] } 2... d5 { [%clk 0:01:00] } 3. Nc3 { [%clk 0:00:59] } 3... Nf6 { [%clk 0:00:59] } 4. Nf3 { [%clk 0:00:57] } 4... Bb4 { [%clk 0:00:58] } 5. Bg5 { [%clk 0:00:56] } 5... c6 { [%clk 0:00:57] } 6. e3 { [%clk 0:00:52] } 6... Nbd7 { [%clk 0:00:57] } 7. h4 { [%clk 0:00:51] } 7... Qa5 { [%clk 0:00:56] } 8. Qc2 { [%clk 0:00:50] } 8... h6 { [%clk 0:00:55] } 9. Bf4 { [%clk 0:00:48] } 9... Ne4 { [%clk 0:00:53] } 10. Rc1 { [%clk 0:00:44] } 10... Ndf6 { [%clk 0:00:51] } 11. Bd3 { [%clk 0:00:42] } 11... Nxc3 { [%clk 0:00:51] } 12. bxc3 { [%clk 0:00:41] } 12... Ba3 { [%clk 0:00:50] } 13. Rb1 { [%clk 0:00:39] } 13... Bd7 { [%clk 0:00:47] } 14. O-O { [%clk 0:00:37] } 14... O-O { [%clk 0:00:46] } 15. Ne5 { [%clk 0:00:36] } 15... Rfe8 { [%clk 0:00:44] } 16. Nxd7 { [%clk 0:00:31] } 16... Nxd7 { [%clk 0:00:44] } 17. Bh7+ { [%clk 0:00:30] } 17... Kh8 { [%clk 0:00:43] } 18. Bd3 { [%clk 0:00:29] } 18... Kg8 { [%clk 0:00:42] } 19. cxd5 { [%clk 0:00:20] } 19... cxd5 { [%clk 0:00:39] } 20. Be2 { [%clk 0:00:20] } 20... b6 { [%clk 0:00:31] } 21. Qd3 { [%clk 0:00:19] } 21... Nf6 { [%clk 0:00:29] } 22. Bd1 { [%clk 0:00:18] } 22... Rac8 { [%clk 0:00:27] } 23. Rb3 { [%clk 0:00:15] } 23... Be7 { [%clk 0:00:25] } 24. Bc2 { [%clk 0:00:14] } 24... Qxa2 { [%clk 0:00:23] } 25. Be5 { [%clk 0:00:12] } 25... Ne4 { [%clk 0:00:21] } 26. f3 { [%clk 0:00:10] } 26... f5 { [%clk 0:00:19] } 27. fxe4 { [%clk 0:00:09] } 27... dxe4 { [%clk 0:00:19] } 28. Qe2 { [%clk 0:00:09] } 28... Bf6 { [%clk 0:00:16] } 29. Bxf6 { [%clk 0:00:07] } 29... gxf6 { [%clk 0:00:16] } 30. Qh5 { [%clk 0:00:07] } 30... Kg7 { [%clk 0:00:15] } 31. Rf3 { [%clk 0:00:05] } 31... exf3 { [%clk 0:00:14] } 32. Qxf3 { [%clk 0:00:05] } 32... Rg8 { [%clk 0:00:12] } 33. Qg3+ { [%clk 0:00:04] } 33... Kf7 { [%clk 0:00:11] } 34. Qf3 { [%clk 0:00:04] } 34... Qa5 { [%clk 0:00:10] } 35. Rb1 { [%clk 0:00:03] } 35... Qxc3 { [%clk 0:00:08] } 36. Rc1 { [%clk 0:00:01] } 36... Qxc2 { [%clk 0:00:07] } 37. Rxc2 { [%clk 0:00:00] } 37... Rxc2 { [%clk 0:00:07] } 38. Kh2 { [%clk 0:00:00] } 38... Rcxg2+ { [%clk 0:00:06] } 0-1

"""

pgn_string_with_clks_chess = """
[Event "Live Chess - chess"]
[Site "Chess.com"]
[Date "2022.03.16"]
[Round "?"]
[White "BENlTO"]
[Black "Fork52"]
[Result "0-1"]
[TimeControl "180"]
[WhiteElo "1891"]
[BlackElo "1815"]
[Termination "Fork52 won by resignation"]

1. e4 {[%clk 0:03:00][%timestamp 1]} 1... c5 {[%clk 0:02:59.4][%timestamp 6]} 2.
f4 {[%clk 0:02:59.9][%timestamp 1]} 2... d5 {[%clk 0:02:57.3][%timestamp 21]} 3.
Nf3 {[%clk 0:02:59.8][%timestamp 1]} 3... dxe4 {[%clk 0:02:56][%timestamp 13]}
4. Ne5 {[%clk 0:02:56.8][%timestamp 30]} 4... Nf6 {[%clk 0:02:51.2][%timestamp
48]} 5. Bc4 {[%clk 0:02:56.1][%timestamp 7]} 5... e6 {[%clk
0:02:49.1][%timestamp 21]} 6. f5 {[%clk 0:02:54.8][%timestamp 13]} 6... Qc7
{[%clk 0:02:44.2][%timestamp 49]} 7. d4 {[%clk 0:02:43][%timestamp 118]} 7...
cxd4 {[%clk 0:02:42.1][%timestamp 21]} 8. Qxd4 {[%clk 0:02:40.9][%timestamp 21]}
8... Bc5 {[%clk 0:02:33.7][%timestamp 84]} 9. Qc3 {[%clk 0:02:39.2][%timestamp
17]} 9... Nc6 {[%clk 0:02:20.5][%timestamp 132]} 10. Bf4 {[%clk
0:02:37.6][%timestamp 16]} 10... Bb4 {[%clk 0:02:18.5][%timestamp 20]} 11. Nxc6
{[%clk 0:02:18.8][%timestamp 188]} 11... Bxc3+ {[%clk 0:02:17.3][%timestamp 12]}
12. Nxc3 {[%clk 0:02:16.8][%timestamp 20]} 12... Qxf4 {[%clk
0:01:58.4][%timestamp 189]} 13. Rf1 {[%clk 0:01:59.8][%timestamp 170]} 13...
Qe3+ {[%clk 0:01:54.3][%timestamp 41]} 14. Be2 {[%clk 0:01:49.2][%timestamp
106]} 14... bxc6 {[%clk 0:01:53.2][%timestamp 11]} 15. fxe6 {[%clk
0:01:47.1][%timestamp 21]} 15... Bxe6 {[%clk 0:01:51.9][%timestamp 13]} 16. Nd1
{[%clk 0:01:42.3][%timestamp 48]} 16... Qc5 {[%clk 0:01:39.8][%timestamp 121]}
17. Nc3 {[%clk 0:01:39.9][%timestamp 24]} 17... O-O {[%clk 0:01:35.4][%timestamp
44]} 18. O-O-O {[%clk 0:01:38.8][%timestamp 11]} 18... Rfd8 {[%clk
0:01:34][%timestamp 14]} 0-1"""

# def test_basic_test():
#     try:
#         obj = Gifmaker(delay=2)
#         obj.make_gif_from_pgn_string(pgn_string, 'sample.gif')
#         assert True
#     except:
#         assert False


def test_clocks_test():
    try:
        obj = Gifmaker(delay=2)
        obj.make_gif_from_pgn_string(pgn_string_with_clks_chess, 'sample.gif')
        assert True
    except:
        assert False

