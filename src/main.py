from argparse import ArgumentParser

from Application import Application


def setup_argparse():
    """
    Sets up the command line argument parser.

    Returns:
        None
    """
    parser = ArgumentParser()
    parser.add_argument("--log-level", dest="log_level", choices=["debug", "info", "warning", "error", "critical"], help="The log level to be set.")
    parser.add_argument("--width", dest="width", type=int, help="The width of the game window.")
    parser.add_argument("--height", dest="height", type=int, help="The height of the game window.")
    parser.add_argument("--config-file", dest="configuration_file", help="The path to the configuration file.")
    parser.add_argument("--log-dir", dest="log_directory", help="The directory to store log files.")
    parser.add_argument("--log-file", dest="log_file", help="The name of the log file.")
    
    return parser.parse_args()


if __name__ == "__main__":
    """
    This is the main entry point of the Snake Game.
    """
    args = setup_argparse()
    app = Application(args)
    app.start()
    app.loop()