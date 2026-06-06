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


def test_can_load_json_from_path():
    config = Config.from_json("data/nested_config.json")
    assert config.database.host == nested_config["database"]["host"]
    assert config.database.port == nested_config["database"]["port"]


def test_can_load_json_from_filelike():
    with open("data/nested_config.json") as f:
        config = Config.from_json(f)

    assert config.database.host == nested_config["database"]["host"]
    assert config.database.port == nested_config["database"]["port"]


def test_can_load_yaml_from_path():
    config = Config.from_yaml("data/nested_config.yaml")
    assert config.database.host == "example.org"
    assert config.database.port == 1234


def test_can_load_yaml_from_filelike():
    with open("data/nested_config.yaml") as f:
        config = Config.from_yaml(f)

    assert config.database.host == "example.org"
    assert config.database.port == 1234


dict_inside_list = {
    "databases": [{"host": "example.org", "port": 1234, "tags": {"env": "dev"}}]
}


def test_dict_inside_list():
    config = Config(dict_inside_list)
    assert config.databases[0].host == "example.org"
    assert config.databases[0].port == 1234
    assert config.databases[0].tags.env == "dev"


nested_lists = {
    "tables": [
        [{"row": 0}, {"row": 1}],
        [{"row": 5}, {"row": 6}],
    ]
}


def test_nested_lists():
    config = Config(nested_lists)
    assert config.tables[0][0].row == 0
    assert config.tables[1][1].row == 6


list_raw_values = {"zones": [1, 2, 3]}


def test_list_raw_values():

    config = Config(list_raw_values)
    assert config.zones == list_raw_values["zones"]


mixed_list_items = {"zones": [1, 2, {"name": 3}, [2, 3]]}


def test_mixed_list_items():

    config = Config(mixed_list_items)
    assert config.zones[0] == 1
    assert config.zones[2].name == 3
    assert config.zones[3][1] == 3
