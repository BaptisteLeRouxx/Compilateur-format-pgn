"""
Auteur: Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : Analyse_partie
Contacts:
baptiste.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""

import os
import sys
from pgn_lexer import PgnLexer
from pgn_parser import PgnParser
from pgn_visitor import *
from pgn_interface import *
from utils import convert_moves

"""
Code principal du projet: renvoie l'analyse lexicale, l'analyse syntaxique et lance la partie d'echec sur une interface graphique
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyse_partie.py filename.pgn")
        sys.exit()

    filename = sys.argv[1]

    # Vérifier si le fichier existe
    if not os.path.exists(filename):
        print(f"Erreur: Le fichier '{filename}' n'existe pas.")
        sys.exit(1)

    # Ouvrir et lire le fichier
    with open(filename, 'r') as f:
        content = f.read()

    # Analyse lexicale
    lexer = PgnLexer()
    tokens = lexer.tokenize(content)
    print("==== Tokens ====")
    print(tokens)

    # Analyse syntaxique
    parser = PgnParser()
    ast = parser.parse(tokens)
    print("==== AST ====")
    print(ast)

    # Création de la partie d'échecs
    visitor = PgnVisitor()
    ast.accept(visitor)
    moves = visitor.moves
    new_moves = []
    for move in moves:
        if move == "OO": #Le move 00 n'est pas reconnu, pb de regex surement, on arrange cela en remplacant la chaine par le resultat attendu: 0-0
            move = move.replace("OO","O-O")
            new_moves.append(move)
        else:
            new_moves.append(move)
    new_moves = convert_moves(new_moves) #on convertit les moves au format d'exemple "e2e4" pour pouvoir exploiter la librairie, ainsi on connait le coup initial et le coup joué
    white_moves = new_moves[::2] #coups pairs
    black_moves = new_moves[1::2] #coups impairs
    game = ChessGame(white_moves, black_moves)
    root = tk.Tk()
    board = ChessBoard(root, game)
    board.pack()
    root.mainloop()

    print("==== Chess Game ====")
    print(game)

if __name__ == '__main__':
    # Appel de la fonction principale
    main()