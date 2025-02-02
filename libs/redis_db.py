import redis
import logging
from itertools import chain

class RedisDB:

    DEFAULT_REDIS_DB = 6
    DEFAULT_REDIS_TESTDB = 7

    def __init__(self, host='192.168.178.25', port=6379, test=False, password=""):
        db = self.DEFAULT_REDIS_TESTDB if test else self.DEFAULT_REDIS_DB
        self.r = redis.StrictRedis(
            host=host, port=port, db=db, decode_responses=True, password=password
        )

    def set_position(self, fen, cp, mate, line):
        """Store position in Redis"""
        try:
            key = f"pos:{fen}"
            mapping = {"mate": mate, "line": line, "cp": cp}
            print(f"Storing {key} {mapping}")

            # Corrected hset usage
            self.r.hset(key, *chain.from_iterable(mapping.items()))  # ✅ Correct

        except Exception as e:
            logging.error(f"Error storing {key} {mapping}: {e}")
            raise

    def get_position(self, fen):
        """Retrieve position from Redis"""
        key = f"pos:{fen}"
        return self.r.hgetall(key)

    def save(self):
        """Save the Redis database"""
        self.r.save()
        return self.r.info('persistence')
