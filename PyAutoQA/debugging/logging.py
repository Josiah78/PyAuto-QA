import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')
logging.disable(logging.DEBUG)
logging.debug # doesn't log bc log is disabled/better than deleting print statements/logging.DEBUG/INFO/WARNING/ERROR/CRITICAL