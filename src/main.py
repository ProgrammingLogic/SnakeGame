from argparse import ArgumentParser

from Application import Application


if __name__ == "__main__":
    """
    This is the main entry point of the Snake Game.
    """
    parser = ArgumentParser(description='Play SnakeGame.')
    parser.add_argument('configuration_file', type=str, nargs='?', default='.\\res\\settings.json', help='Path of the configuration file')
    parser.add_argument('--log_level', choices=['info', 'debug', 'warning', 'error', 'critical'], help='Log level (info, debug, warning, error, critical)')

    args = parser.parse_args()

    app = Application(**vars(args))
    app.start()
    app.loop()