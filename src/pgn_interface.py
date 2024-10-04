"""
Auteur: Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : Analyse_partie
Contacts:
baptiste.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""


import chess
import tkinter as tk
"""
Ce fichier contient la logique du jeu d'échecs et l'interface graphique pour l'afficher à l'aide de Tkinter.
"""
class Board:
    """
    Classe représentant un plateau d'échecs.
    """
    def __init__(self):
        self.board = chess.Board()

class ChessGame:
    """
    Classe représentant une partie d'échecs.
    """
    def __init__(self, white_moves, black_moves):
        self.board = Board()
        self.white_moves = white_moves
        self.black_moves = black_moves
        self.current_move = 0

    piece_symbols = {
        'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
        'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚',
        None: ' '
    }

    def make_move(self, move):
        player_moves = self.white_moves if self.get_current_player() == 'white' else self.black_moves

        if move not in player_moves:
            print("Invalid move:", move)
            return

        self.board.board.push(move)
        self.current_move += 1

    def get_board(self):
        rows = []
        for i in range(8):
            row = []
            for j in range(8):
                piece = self.board.board.piece_at(chess.square(j, 7 - i))
                if piece:
                    row.append(self.piece_symbols[piece.symbol()])
                else:
                    row.append(self.piece_symbols[None])
            rows.append(row)
        return rows

    def get_current_player(self):
        return 'white' if self.current_move % 2 == 0 else 'black'

    def is_game_over(self):
        return self.board.board.is_game_over()

    def get_moves(self):
        return self.white_moves + self.black_moves

class ChessBoard(tk.Frame):
    """
    Classe représentant l'interface graphique d'un plateau d'échecs.
    """
    def __init__(self, parent, game):
        tk.Frame.__init__(self, parent, width=400, height=400)
        self.parent = parent
        self.game = game
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.draw_pieces()
        self.current_player = 'white'
        self.next_button = tk.Button(self.parent, text="Suivant", command=self.next_move)
        self.next_button.pack()
        self.quit_button = tk.Button(self.parent, text="Quitter", command=self.quit_game)
        self.quit_button.pack()
        self.canvas.bind("<Button-1>", self.on_click)


    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = 'white' if (i + j) % 2 == 0 else 'gray'
                x1, y1 = j * 50, i * 50
                x2, y2 = (j + 1) * 50, (i + 1) * 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_pieces(self):
        pieces = self.game.get_board()
        for i in range(8):
            for j in range(8):
                piece = pieces[i][j]
                if piece != '.':
                    x, y = j * 50 + 25, i * 50 + 25
                    self.canvas.create_text(x, y, text=piece, font=('Arial', 24), tags='piece')

    def on_click(self, event):
        x, y = event.x, event.y
        col, row = x // 50, y // 50
        square = chess.square(col, 7 - row)
        move = self.get_move_to_square(square)
        if move:
            self.game.make_move(move)
            self.canvas.delete('piece')
            self.draw_pieces()
        else:
            print("Invalid move:", move)

    def get_move_to_square(self, square):
        player_moves = self.game.get_moves()
        for move in player_moves:
            if move.to_square == square:
                return move
        return None

    def next_move(self):
        current_player = self.game.get_current_player()
        player_moves = self.game.white_moves if current_player == 'white' else self.game.black_moves
        if self.game.current_move // 2 < len(player_moves):
            move = player_moves[self.game.current_move // 2]
            self.game.make_move(move)
            self.canvas.delete('piece')
            self.draw_pieces()
            self.current_player = self.game.get_current_player()
            if not self.game.is_game_over():
                self.parent.title("Tour des " + self.current_player + "s")
            else:
                result = self.game.board.board.result()
                result_message = {
                    "1-0": "Les Blancs ont gagné",
                    "0-1": "Les Noirs ont gagné",
                    "1/2-1/2": "La partie est nulle",
                }.get(result, "La partie est terminée")
                self.parent.title(result_message)
        if self.game.current_move >= len(self.game.get_moves()):
            self.parent.title("Fin de la partie")
            end_label = tk.Label(self.parent, text="Fin de la partie", font=('Arial', 30))
            end_label.pack()

    def quit_game(self):
        self.parent.destroy()