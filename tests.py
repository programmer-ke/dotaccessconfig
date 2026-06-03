import pytest
from dotconfig import Config


flat_config = {"host": "example.org"}

nested_config = {"database": {"host": "example.org", "port": 1234}}


def test_can_use_dot_notation_on_flat_dict():
    config = Config(flat_config)
    assert config.host == flat_config["host"]


def test_missing_config_name_raises():
    config = Config(flat_config)
    with pytest.raises(AttributeError):
        config.port


def test_can_use_dot_notation_nested_dict():
    config = Config(nested_config)
    assert config.database.host == nested_config["database"]["host"]
    assert config.database.port == nested_config["database"]["port"]
