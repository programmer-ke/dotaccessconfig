"""dotconfig - Create config objects from JSON/YAML"""

import json
from pathlib import Path


class Config:
    def __init__(self, config: dict):
        self._config = config

    @classmethod
    def from_json(cls, file):
        try:
            filepath = Path(file)
        except TypeError:
            # treat as filelike
            data = json.load(file)
        else:
            with open(filepath) as f:
                data = json.load(f)
        return cls(data)

    def __getattr__(self, name):
        try:
            value = self._config[name]
        except KeyError as e:
            raise AttributeError(f"No config '{name}' found.") from e

        if isinstance(value, dict):
            return Config(value)
        return value
