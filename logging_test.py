# This code was an old study, so TODO: Review this whole code.

import logging

# Note: parameters for basicConfig method have no order, since is **kwargs (pointer to keyword arguments)

# Available levels:
# logging.CRITICAL
# logging.ERROR
# logging.WARNING
# logging.INFO
# logging.DEBUG
# logging.NOTSET

# logging.basicConfig(level=logging.CRITICAL)

logging.basicConfig(level=logging.NOTSET, filename='logging_test.log')  # Preference: faster than printing (filemode is 'a')
# logging.basicConfig(level=logging.NOTSET, filename='logging_test.log', filemode='w')  # Erasing old log

# 2019-11-10 12:18:44,293  DEBUG:Debug message.
# logging.basicConfig(level=logging.NOTSET, format='%(asctime)s  %(levelname)s:%(message)s')

# 2019-11-10 12:29:15,731  DEBUG:Debug message.
# logging.basicConfig(level=logging.NOTSET, format='%(asctime)s  %(levelname)s:%(message)s', filename='logging_test.log')

# 11/10/2019 12:19:01 PM  DEBUG:Debug message.
# logging.basicConfig(format='%(asctime)s  %(levelname)s:%(message)s',
#                    datefmt='%m/%d/%Y %I:%M:%S %p',
#                    level=logging.NOTSET)

logging.basicConfig()

logging.critical('Critical message.')  # Shows with (NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.error('Error message.')        # Shows with (NOTSET, DEBUG, INFO, WARNING, ERROR)
logging.warning('Warning message.')    # Shows with (NOTSET, DEBUG, INFO, WARNING)
logging.info('Info message.')          # Shows with (NOTSET, DEBUG, INFO)
logging.debug('Debug message.')        # Shows with (NOTSET, DEBUG)
