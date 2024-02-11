import os
import time
#Change curr dir to python file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import threading

import Modules.ChessUI.chess_ui as chui

chess_ui = chui.ChessUI()
t = threading.Thread(target=chess_ui.start, daemon=True)
t.start()
time.sleep(5)

while True:
    position = [
    ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'], 
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'], 
    ['', '', '', '', '', '', '', ''], 
    ['', '', '', '', '', '', '', ''], 
    ['', '', '', '', '', '', '', ''], 
    ['', '', '', '', '', '', '', ''], 
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'], 
    ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'], 
    ]

    chess_ui.draw_position(position)
    time.sleep(5)

    position = [
    ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'], 
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'], 
    ['', '', '', '', '', '', '', ''], 
    ['', '', '', '', '', '', '', ''], 
    ['', '', '', 'WP', '', '', '', ''], 
    ['', '', '', '', '', '', '', ''], 
    ['WP', 'WP', 'WP', '', 'WP', 'WP', 'WP', 'WP'], 
    ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR'], 
    ]

    chess_ui.draw_position(position)

    time.sleep(5)
    
    
    break