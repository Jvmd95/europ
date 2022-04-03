from load_configuration import load_configuration, validate_configuration
from load_dataframe import load_dataframe
from transformations import transformation_orchestrator
from sink_dataframe import sink_dataframe


def main(configuration_path="../configuration.json"):
    configuration_dict = load_configuration(configuration_path)
    validate_configuration(configuration_dict)
    df = load_dataframe(configuration_dict["source"])
    df = transformation_orchestrator(df, configuration_dict["transforms"])
    sink_dataframe(df, configuration_dict["sink"])


if __name__ == "__main__":
    main()



