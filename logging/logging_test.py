import logging

#add filemode="w" to overwrite

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex22")
# logging.debug("This is a debug message")
# logging.info("Informational meesage")
# logging.error("An error has happened")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")
    log.info('gggg')