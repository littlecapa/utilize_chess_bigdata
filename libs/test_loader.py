import logging
logging.basicConfig(
    filename="test_loader.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
from redis_db import RedisDB
import csv

myRedis = RedisDB(test=False)

test_fen_file = "test_data.csv"

# Read the CSV file
with open(test_fen_file, "r", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        # Assuming the columns are in the order: fen, cp, mate, line
        fen, cp, mate, line = row
        logging.info(f"fen: {fen}, cp: {cp}, mate: {mate}, line: {line}")
        pos = myRedis.get_position(fen)
        logging.info(f"pos: {pos}")
        if pos == {}:
            raise Exception("Database broken")