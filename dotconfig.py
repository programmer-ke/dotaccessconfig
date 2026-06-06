"""dotconfig - Create config objects from JSON/YAML"""

import json
from pathlib import Path

import yaml


class Config:

    def __new__(cls, config):
        if isinstance(config, list):
            return [cls(c) if isinstance(c, (list, dict)) else c for c in config]
        return super().__new__(cls)

    def __init__(self, config: dict):
        self._config = config

    @classmethod
    def from_json(cls, file):
        data = cls._get_data(file, json.load)
        return cls(data)

    @classmethod
    def from_yaml(cls, file):
        data = cls._get_data(file, yaml.safe_load)
        return cls(data)

    @staticmethod
    def _get_data(source, loader):
        try:
            filepath = Path(source)
        except TypeError:
            # treat as filelike
            data = loader(source)
        else:
            with open(filepath) as f:
                data = loader(f)
        return data

    def __getattr__(self, name):
        try:
            value = self._config[name]
        except KeyError as e:
            raise AttributeError(f"No config '{name}' found.") from e

        if isinstance(value, (dict, list)):
            return Config(value)
        return value
