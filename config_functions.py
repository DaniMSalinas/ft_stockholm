"""Library to interact with configfile"""
import configparser

class Configlibrary:
    """Class where it's stored the configuration of the program"""
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('configuration/stckhlm.config')

    def get_program_version(self):
        """function returns the current program version"""
        return self.config['program']['version']

    def get_log_level(self):
        """function returns the current log level"""
        return self.config['logger']['level']

    def set_log_level(self, level):
        """function updates the log level version"""
        self.config['log']['level'] = level

    def get_config_dir(self):
        """function returns the infection target directory"""
        return self.config['infection']['directory']
