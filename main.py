"""Ransomware that emulates wannacry attack ciphering files with .DOC, .MPG, or .PDF extensions"""
import sys
from logger import Stockholmlogger
from config_functions import Configlibrary

def main():
    """main function of the program"""
    config = Configlibrary()
    st_logger = Stockholmlogger()
    st_logger.set_log_level(config.get_log_level())

    if sys.argv[1] == "-s":
        config.set_log_level("NOTSET")
        st_logger.logger.propagate = False
    if sys.argv[1] == "-h":
        st_logger.logger.info("imprimiendo manual de ayuda")
    elif sys.argv[1] == "-v":
        st_logger.logger.info(config.get_program_version())
    elif sys.argv[1] == "-r":
        if sys.argv[2]:
            st_logger.logger.info("gracias por la clave")
        else:
            st_logger.logger.error("no puedo revertir el cifrado si no me das la clave")
    else:
        print("a hacer cositas")

if __name__ == "__main__":
    main()
    