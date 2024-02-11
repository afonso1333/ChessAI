import eel 
import os

# Change curr dir to python file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

class ChessUI:
    def __init__(self):
        pass

    # Starts UI Window 
    def start(self):
        eel.init(str(os.getcwd())) 
        eel.start('chess_ui.html')
    
    # Draws a chess position in html based on position matrix argumnent
    def draw_position(self, position): 
        html = '<div class="chess">'
        i = 0
        for row in position:
            html += ' <div class="chess-row">'
            for col in row:
                piece_class = self.getPieceClass(col)
                if (i%2) == 0:
                    html += ('<div class="chess-col white-square ' + piece_class + '"></div>')
                else:
                    html += ('<div class="chess-col black-square ' + piece_class + '"></div>')
                i += 1
            i += 1
            html += '</div>'
        html += '</div></div>'
        eel.replaceInnerHTML(html)

    # Returns a piece class string based on a piece type string
    def getPieceClass(self, piece):
        piece_color = ''
        piece_name = ''
        if piece != '':
            if piece[0] == 'W':
                piece_color = 'white'
            elif piece[0] == 'B':
                piece_color = 'black'
            if piece[1] == 'P':
                piece_name = 'pawn'
            elif piece[1] == 'R':
                piece_name = 'rook'
            elif piece[1] == 'N':
                piece_name = 'knight'
            elif piece[1] == 'B':
                piece_name = 'bishop'
            elif piece[1] == 'Q':
                piece_name = 'queen'
            elif piece[1] == 'K':
                piece_name = 'king'
        return piece_color + '-' + piece_name