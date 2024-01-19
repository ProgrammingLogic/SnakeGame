import json

from argparse import ArgumentParser
from pathlib import Path


def save_configuration_file(path, configuration):
    configuration_file = Path(path)

    # If the configuration file's parent directory does not exist, create it.
    # By default, this will create the res directory if it does not exist.
    # This is useful for when the user wants to specify a custom path for the
    # configuration file.
    if not configuration_file.parent.exists():
        configuration_file.parent.mkdir(parents=True)

    with open(path, 'w') as file:
        json.dump(configuration, file, indent=4)


def get_configuration(args):
    # Get log_level, width, height, log_dir, and log_file from the user if not provided as command line arguments
    if not args["log_level"]:
        args["log_level"] = get_log_level(None)

    if not args["width"]:
        args["width"] = int(input("Please enter the width of the game window: "))

    if not args["height"]:
        args["height"] = int(input("Please enter the height of the game window: "))

    if not args["log_directory"]:
        args["log_directory"] = input("Please enter the directory to store log files: ")

    if not args["log_file"]:
        args["log_file"] = input("Please enter the name of the log file: ")

    return args


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

    return log_level


if __name__ == "__main__":
    parser = ArgumentParser(description='Generate a .json configuration file.')
    parser.add_argument('path', type=str, nargs='?', default='.\\res\\settings.json', help='Path of the configuration file')
    parser.add_argument("--log-level", dest="log_level", choices=["debug", "info", "warning", "error", "critical"], help="The log level to be set.")
    parser.add_argument("--width", dest="width", type=int, help="The width of the game window.")
    parser.add_argument("--height", dest="height", type=int, help="The height of the game window.")
    parser.add_argument("--log-dir", dest="log_directory", help="The directory to store log files.")
    parser.add_argument("--log-file", dest="log_file", help="The name of the log file.")
    args = parser.parse_args()


    args = vars(args)
    configuration = get_configuration(args)
    save_configuration_file(configuration.pop("path"), configuration)
    