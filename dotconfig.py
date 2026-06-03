"""dotconfig - Create config objects from JSON/YAML"""


class Config:
    def __init__(self, config: dict):
        self._config = config

    def __getattr__(self, name):
        try:
            return self._config[name]
        except KeyError as e:
            raise AttributeError(f"No config '{name}' found.") from e
