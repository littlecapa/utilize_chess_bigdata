import chess
import chess.pgn
import io

def create_chess_objects(moves: str) -> (chess.pgn.Game, chess.Board, chess.Move):
    """
    Creates a chess game object from a move string.
    
    :param moves: A string of moves in PGN format, e.g., "1.e4 e5 2.Nf3 Nc6"
    :return: A tuple containing the chess.pgn.Game and a chess.Board object with the moves applied.
    """
    pgn = io.StringIO(moves)
    game = chess.pgn.read_game(pgn)  # Read the PGN game from the string

    if game is None:
        raise ValueError("Invalid PGN string")

    board = game.board()  # Create an initial board
    last_move = None  # Initialize in case no moves are applied

    # Apply the moves sequentially
    for move in game.mainline_moves():
        board.push(move)
        last_move = move
    
    return game, board, last_move

def remove_move_counter(fen: str) -> str:
    """
    Removes the move counter and half-move clock from the FEN string.
    
    :param fen: The FEN string with the move counter and half-move clock.
    :return: A new FEN string without the move counter and half-move clock.
    """
    # Split the FEN string into parts
    parts = fen.split()
    
    # Remove the last two parts (move counter and half-move clock)
    parts = parts[:-2]
    
    # Join the remaining parts back into a FEN string
    return ' '.join(parts)

def board2fen(board: chess.Board) -> str:
    """
    Converts a chess.Board object to a FEN string.
    
    :param board: A chess.Board object.
    :return: The FEN string representing the board position.
    """
    return remove_move_counter(board.fen())

def game2pgn(game: chess.pgn.Game) -> str:
    """
    Converts a chess.pgn.Game object to a PGN string.
    
    :param game: A chess.pgn.Game object.
    :return: The PGN string representing the game.
    """
    exporter = chess.pgn.StringExporter(headers=True, variations=True, comments=True)
    return game.accept(exporter)

def add_comment_move(move: chess.Move, comment: str):
    """
    Adds a comment to the last move of a chess game.
    
    :param game: The chess.pgn.Game object.
    :param comment: The comment to add to the last move.
    """
    move.comment = comment
