import argparse
import json

def generate_configuration_file(path, log_level):
    config = {
        "log_level": log_level
    }
    with open(path, 'w') as file:
        json.dump(config, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a .json configuration file.')
    parser.add_argument('path', type=str, nargs='?', default='.\\res\\settings.json', help='Path of the configuration file')
    parser.add_argument('--log_level', choices=['info', 'debug', 'warning', 'error', 'critical'], help='Log level (info, debug, warning, error, critical)')

    args = parser.parse_args()

    if args.log_level is None:
        log_level = input("Please enter the log level (info, debug, warning, error, critical): ")
        while log_level not in ['info', 'debug', 'warning', 'error', 'critical']:
            log_level = input("Invalid log level. Please enter a valid log level (info, debug, warning, error, critical): ")
    else:
        log_level = args.log_level

    generate_configuration_file(args.path, log_level)
    