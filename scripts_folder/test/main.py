
# Written By Thor AI Script Builder

import logging
import sys

def script_handler(logger,*args, **kwargs):
    pass


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    output_file_handler = logging.FileHandler("output.log")
    stdout_handler = logging.StreamHandler(sys.stdout)

    logger.addHandler(output_file_handler)
    logger.addHandler(stdout_handler)
    script_handler(logger)
