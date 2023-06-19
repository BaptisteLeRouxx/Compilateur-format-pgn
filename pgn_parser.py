"""
Auteur: Mathis & Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : pgn_parser
Contacts:
mathis.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""

from pgn_ast import *

"""
Ce fichier implémente le parseur pour analyser les tokens générés par le lexer et construire un arbre syntaxique.
Il contient la classe PgnParser.
Note à nous-meme, pb avec le token result
"""

class PgnParser:
    """
    Cette classe est utilisée pour analyser une liste de tokens et construire un arbre syntaxique.
    """
    def __init__(self):
        self.current_token = None
        self.token_index = -1
        self.tokens = []

    def parse(self, tokens):
        """
        Méthode pour analyser une liste de tokens et construire un arbre syntaxique.

        :param tokens: une liste de tokens à analyser.
        :return: un nœud de jeu qui représente la racine de l'arbre syntaxique.
        """
        self.tokens = tokens
        self.token_index = -1
        self.current_token = None
        self.advance()
        return self.parse_game()

    def parse_game(self):
        """
        Méthode pour analyser les tokens et construire l'AST des coups et des résultats.

        :return: un noeud de type GameNode représentant l'AST.
        """
        moves = []
        results = []
        while self.current_token is not None:
            if self.current_token.name == "NUMBER":
                move_number, move_white, move_black = self.parse_move()
                moves.append(MoveNode(move_number, move_white, move_black))
            elif self.current_token is not None and self.current_token.name == "RESULT":
                result = self.current_token.value
                results.append(ResultNode(result))
            self.advance()
        return GameNode(moves, results)

    def parse_move(self):
        """
        Méthode pour analyser les tokens et construire l'AST pour un coup.

        :return: un tuple contenant le numéro du coup, le coup des blancs et le coup des noirs.
        """
        move_number = self.current_token.value[:-1]
        self.advance()
        move_white = self.parse_single_move()
        self.advance()
        if self.current_token is None or self.current_token.name == "RESULT":
            move_black = None
        else:
            move_black = self.parse_single_move()
        return move_number, move_white, move_black

    def parse_single_move(self):
        """
        Méthode pour analyser un token représentant un coup individuel.

        :return: la valeur du token représentant le coup.
        """
        if self.current_token is None:
            return None
        move = self.current_token.value
        return move

    def advance(self):
        """
        Méthode pour avancer au token suivant dans la liste des tokens.
        """
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None
