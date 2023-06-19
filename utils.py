import chess

def convert_moves(moves):
    board = chess.Board()
    new_moves = []
    for move in moves:
        try:
            move_obj = board.push_san(move)
        except ValueError:
            move_obj = get_castling_move(board, move)
        new_moves.append(move_obj)
    return new_moves

def get_castling_move(board, move):
    if move.lower() == "O-O":
        if board.is_castling(board.kingside_castling(board.turn)):
            return board.kingside_castling(board.turn)
        else:
            raise ValueError("Invalid castling move")
    elif move.lower() == "O-O-O":
        if board.is_castling(board.queenside_castling(board.turn)):
            return board.queenside_castling(board.turn)
        else:
            raise ValueError("Invalid castling move")
    else:
        raise ValueError("Invalid castling move")
