import json
import logging

class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self._load_config()

    def _load_config(self):
        """Load JSON config file"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error loading config: {e}")
            raise

    def __getitem__(self, key):
        if key not in self.config:
            logging.error(f"Key '{key}' not found in configuration")
            raise KeyError(f"Key '{key}' not found in configuration")
        return self.config.get(key, None)