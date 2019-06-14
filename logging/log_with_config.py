# log_with_config.py
import logging
import logging.config
import otherMod2

def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """

    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('exampleApp')

    loger.info("Program started")
    result = otherMod2.add(7,8)
    loggeer.info("Done!")

    if __name__ == "__main__":
        main()