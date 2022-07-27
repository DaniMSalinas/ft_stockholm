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

    def get_infection_dir(self):
        """function returns the infection target directory"""
        return self.config['infection']['directory']

    def get_infection_extensions(self):
        """function returns the infection target extensions"""
        return self.config['infection']['extensions']

    def get_infection_key(self):
        """function returns the key path to cipher files"""
        return self.config['infection']['key']
