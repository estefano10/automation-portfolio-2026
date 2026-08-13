import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logging.debug("debugging...")
logging.info("initializing process...")
logging.warning("Unexpected behavior")
logging.error("failed test")
logging.critical("broken DB")