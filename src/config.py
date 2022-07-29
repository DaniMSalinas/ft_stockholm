"""Library to interact with configfile"""
import configparser
import argparse

class Configlibrary:
    """Class where it's stored the configuration of the program"""
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('configuration/stckhlm.config')
        self.parser = argparse.ArgumentParser(
            description="""STOCKHOLM RANSOMWARE:\n
                        This program encrypts all the files at home/infection directory""")
        self._set_arguments()

    def _set_arguments(self):
        self.parser.add_argument('-v', '--version', action='store_true',
                                help="show current program version")
        self.parser.add_argument('-s', '--silent', action='store_true',
                                help="silent the console output")
        self.parser.add_argument('-r', '--reverse', metavar='<key>', type=str,
                                help="decrypt all files. Mandatory send the key after reverse keyword: -r <key>")

    def get_program_version(self):
        """function returns the current program version"""
        return self.config['program']['version']

    def get_log_level(self):
        """function returns the current log level"""
        return self.config['logger']['level']

    def set_log_level(self, level):
        """function updates the log level version"""
        self.config['logger']['level'] = level

    def get_infection_dir(self):
        """function returns the infection target directory"""
        return self.config['infection']['directory']

    def get_infection_extensions(self):
        """function returns the infection target extensions"""
        extensions_list = []
        with open(self.config['infection']['extensions'], 'rb') as extensions_file:
            extensions_str = extensions_file.read().decode("utf-8")
        extensions_list = extensions_str.split('\r\n.')
        return extensions_list

    def get_infection_key(self):
        """function returns the key path to cipher files"""
        return self.config['infection']['key']
