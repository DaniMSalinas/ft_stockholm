"""Logger class for the project"""
import logging

class Stockholmlogger():
    """Class to handle the logger of the project"""
    def __init__(self):
        self.logger = logging.getLogger("ft_stockholm_logger")
        self.set_console_handler()

    def set_console_handler(self):
        """function to set console handler"""
        console_handler = logging.StreamHandler()
        self.logger.addHandler(console_handler)

    def set_log_level(self, level):
        """function to set the log level"""
        self.logger.setLevel(level)
