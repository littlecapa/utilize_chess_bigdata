import chess.pgn
import os
import sys
import logging
logging.basicConfig(
    filename="redis_book.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from libs.config_reader import ConfigReader
from libs.redis_db import RedisDB
from libs.chess import create_chess_objects, board2fen, game2pgn, add_comment_move

if __name__ == "__main__":
    # Get the PGN file path and output folder from the command line arguments
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
        pgn_output_path = sys.argv[2]
    else:
        config_file = "/Users/littlecapa/GIT/python/utilize_chess_bigdata/config/first_test.json"
        pgn_output_path= "/Users/littlecapa/GIT/python/utilize_chess_bigdata/output"
    file_name = os.path.basename(config_file).replace
    pgn_output_file = os.path.join(pgn_output_path, f"{file_name}.pgn")
    # Load the configuration
    config = ConfigReader(config_file)
    r = RedisDB()
    game, position, last_move = create_chess_objects(config["Moves"])
    result = r.get_position(board2fen(position))
    print(f"Result: {result}")
    add_comment_move(last_move, str(result))    
    with open(pgn_output_file , "w") as file:
        file.write(game2pgn(game))
