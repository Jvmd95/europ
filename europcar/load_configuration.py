import json
from schema import Schema, And, Use, Optional, SchemaError


def load_configuration(path):
    try:
        configuration_dict = json.load(open(path))
        if isinstance(configuration_dict, dict):
            return configuration_dict
        else:
            raise Exception(
                "Wrong format on the json configuration file. Please look at the example configuration file")
    except IOError:
        print(f"ERROR: Can not find {path} file. Make sure the configuration file its on the same directory as this "
              f"executable.")
        raise


conf_schema = Schema({
    'source': {
        "path": And(Use(str)),
        "dataset": And(Use(str)),
        "format": And(Use(str))
    },
    "transforms": [
        {
            "transform": And(Use(str)),
            "fields": And(Use(list))
        }
    ],
    'sink': {
        "path": And(Use(str)),
        "dataset": And(Use(str)),
        "format": And(Use(str))
    }
})


def validate_configuration(conf):
    conf_schema.validate(conf)
    return True

