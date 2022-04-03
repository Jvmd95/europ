import pytest
from europcar.load_configuration import load_configuration, validate_configuration


def test_load_json():
    configuration_dict = load_configuration("tests/test_good_format.json")
    assert isinstance(configuration_dict, dict)


def test_validate_configuration_schema():
    configuration_dict = load_configuration("tests/test_good_format.json")
    validate_configuration(configuration_dict)


def test_validate_configuration_schema_raised():
    with pytest.raises(Exception):
        configuration_dict = load_configuration("tests/test_good_format_invalid.json")
        validate_configuration(configuration_dict)