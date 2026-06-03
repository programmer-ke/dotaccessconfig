import pytest
from dotconfig import Config


flat_config = {"host": "example.org"}


def test_can_use_dot_notation_on_flat_dict():
    config = Config(flat_config)
    assert config.host == flat_config["host"]


def test_missing_config_name_raises():
    config = Config(flat_config)
    with pytest.raises(AttributeError):
        config.port
