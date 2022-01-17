import logging
import sys

def script_handler(logger,*args, **kwargs):
    for _ in range(0, 10):
        logger.debug("Thor Script Testing")


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    output_file_handler = logging.FileHandler("output.log")
    stdout_handler = logging.StreamHandler(sys.stdout)

    logger.addHandler(output_file_handler)
    logger.addHandler(stdout_handler)
    script_handler(logger)