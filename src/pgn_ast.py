"""
Auteur: Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : Analyse_partie
Contacts:
baptiste.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""
"""
Dans ce fichier on définit une classe pour chaque type de noeuds de l'AST en s'appuyant sur le parseur réalisé auparavant.
Ainsi on créé les noeuds :
- GameNode: il prend pour attribut les coups joués et le resultat final de la partie
- MoveNode: il prend pour attribut le nombre de tour joué, les coups des noirs et des blancs
- ResultNode: il prend pour attribut le résultat de la partie
"""
import re

class GameNode:
    def __init__(self, moves, results):
        self.moves = moves
        self.results = results

    def accept(self, visitor):
        visitor.visit_game(self)


class MoveNode:
    def __init__(self, move_number, move_white, move_black=None):
        self.move_number = move_number
        self.move_white = self.clean_move(move_white)
        self.move_black = self.clean_move(move_black) if move_black else None

    def clean_move(self, move):
        # Enlève tout ce qui n'est pas une lettre ou un chiffre
        return re.sub(r'\W+', '', move)

    def accept(self, visitor):
        visitor.visit_move(self)



class ResultNode:
    def __init__(self, result):
        self.result = result

    def accept(self, visitor):
        visitor.visit_result(self)