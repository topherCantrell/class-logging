import logging
from packone import mod_a
from packthree import mod_c

def expensive_func1():
    return 'hello'

def expensive_func2():
    return 'world'

logging.basicConfig(level=logging.DEBUG)

LOGGER = logging.getLogger('top')

LOGGER.error('Error from top')
LOGGER.info('Info from top')
LOGGER.debug('Debug from top')
logging.getLogger('one').setLevel('ERROR')

LOGGER.debug('Here is some info %s %s',expensive_func1(),expensive_func2())

if LOGGER.isEnabledFor(logging.DEBUG):
    # Lots of expensive calculations
    pass

mod_a.do_logs_a()
mod_c.do_logs_c()