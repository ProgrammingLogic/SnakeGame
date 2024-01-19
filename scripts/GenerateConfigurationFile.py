import json

from argparse import ArgumentParser
from pathlib import Path


def save_configuration_file(path, configuration):
    configuration_file = Path(args.path)

    # If the configuration file's parent directory does not exist, create it.
    # By default, this will create the res directory if it does not exist.
    # This is useful for when the user wants to specify a custom path for the
    # configuration file.
    if not configuration_file.parent.exists():
        configuration_file.parent.mkdir(parents=True)

    with open(path, 'w') as file:
        json.dump(configuration, file, indent=4)


def get_configuration(args):
    configuration = {}
    configuration['log_level'] = get_log_level(args.log_level)
    configuration['resolution'] = args.resolution

    return configuration


# Option Parsing Functions
def get_log_level(log_level):
    """
    Parse the log level.

    Args:
        log_level (str): The log level.

    Returns:
        str: The log level.
    """
    while log_level not in ['info', 'debug', 'warning', 'error', 'critical']:
        log_level = input("Please enter the log level (info, debug, warning, error, critical): ")
        # log_level = input("Invalid log level. Please enter a valid log level (info, debug, warning, error, critical): ")

    # if log_level is None:
    #     log_level = input("Please enter the log level (info, debug, warning, error, critical): ")

    #     while log_level not in ['info', 'debug', 'warning', 'error', 'critical']:
    #         log_level = input("Invalid log level. Please enter a valid log level (info, debug, warning, error, critical): ")

    return log_level


if __name__ == "__main__":
    parser = ArgumentParser(description='Generate a .json configuration file.')
    parser.add_argument('path', type=str, nargs='?', default='.\\res\\settings.json', help='Path of the configuration file')
    parser.add_argument('--log_level', choices=['info', 'debug', 'warning', 'error', 'critical'], help='Log level (info, debug, warning, error, critical)')
    parser.add_argument('--resolution', type=tuple, default=(800, 600), help='Resolution of the game window (width, height)')

    args = parser.parse_args()

    configuration = get_configuration(args)
    save_configuration_file(args.path, configuration)
    