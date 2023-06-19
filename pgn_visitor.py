"""
Auteur: Mathis & Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : pgn_visitor
Contacts:
mathis.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""

class PgnVisitor:
    """
    Cette classe est utilisée pour visiter les nœuds de l'arbre syntaxique généré par le parseur PGN.
    Elle contient deux méthodes principales, visit_game et visit_move.
    """
    def __init__(self):
        self.moves = []

    def visit_game(self, node):
        """
        Méthode pour visiter un nœud "game" de l'arbre syntaxique.
        Elle parcourt chaque mouvement dans le nœud "game" et appelle la méthode accept de ce mouvement,
        ce qui entraîne l'appel de la méthode visit_move du visiteur pour ce mouvement.

        :param node: le nœud "game" à visiter.
        """
        for move in node.moves:
            move.accept(self)

    def visit_move(self, node):
        """
        Méthode pour visiter un nœud "move" de l'arbre syntaxique.
        Elle ajoute le mouvement du joueur blanc à la liste self.moves si ce mouvement existe,
        puis fait de même pour le mouvement du joueur noir.

        :param node: le nœud "move" à visiter.
        """
        if node.move_white:
            self.moves.append(node.move_white)
        if node.move_black:
            self.moves.append(node.move_black)
