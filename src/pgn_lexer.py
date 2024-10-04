"""
Auteur: Baptiste LE ROUX
Date: 07/05/2023
Projet: Compilateur
Fichier : Analyse_partie
Contacts:
baptiste.le_roux@ensta-bretagne.org
bapt.leroux29@gmail.com
"""

import re

class PgnLexer:
    """
    Cette classe est utilisée pour transformer le contenu d'un fichier PGN en une série de tokens.
    """
    def __init__(self):
        """
        Constructeur de la classe PgnLexer.
        Initialise une liste vide self.tokens qui stockera les tokens générés.
        """
        self.tokens = []

    def tokenize(self, content):
        """
        Méthode pour transformer le contenu d'un fichier PGN en une série de tokens.
        :param content: le contenu du fichier PGN à analyser.
        :return: une liste de tokens.
        """

        self.tokens = []
        pattern = "|".join(f"(?P<{name}>{regex})" for name, regex in TOKENS)
        for match in re.finditer(pattern, content):
            name = match.lastgroup
            value = match.group(name)
            if name not in IGNORED_TOKENS:
                if name == "MOVE" and value in RESULTS:
                    name = "RESULT"
                self.tokens.append(Token(name, value))
        return self.tokens

"""
Tokens que le lexer peut générer.
"""
TOKENS = [
    ("OPEN_BRACKET", "\["),
    ("CLOSE_BRACKET", "\]"),
    # Keywords
    ("EVENT", "Event"),
    ("SITE", "Site"),
    ("DATE", "Date"),
    ("ROUND", "Round"),
    ("WHITE", "White"),
    ("BLACK", "Black"),

    ("STRING", "\".*?\""),
    ("NUMBER", "\d+\."),
    ("MOVE", "(?<![\d-])(?!1-0|0-1|1/2-1/2)[A-Za-z0-9#+=()!?-]+"),
    ("RESULT", r"\s1-0|0-1|1/2-1/2"),  # nouveau jeton pour les résultats
    ("COMMENT", "{.*?}"),
]


IGNORED_TOKENS = ["COMMENT","RESULT"]

RESULTS = ["1-0", "0-1", "1/2-1/2"]


class Token:
    """
    Cette classe représente un token dans le contexte de l'analyse lexicale.
    """
    def __init__(self, name, value):

        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}({self.value})"
