# ft_stockholm
ransomware emulating wannacry attack

# Ways of working:
- normal mode: encrypt files at the directory
- reverse mode: '-r <key>', '--reverse <key>'
                 decrypt files using the provided key
- silent mode:  '-s', '--silent' mutes the program console output 
- current version:  '-v', '--version' prints the version of the current program
- help:  '-h', '--help', prints the help manual of the program

# directory
This ransomware have been programmed to ecrypt files with specific extension located at $USER/home/infection.

# AES256
In the current version of the program the ecryption system chosen is AES256 based on CBC model. Hexadecimal key with at least 64 hex characters is used.
