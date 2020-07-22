import logging

LOGGER = logging.getLogger('one.two.b')

def do_logs_b():    
    LOGGER.error('Error from do_logs_b')
    LOGGER.info('Info from do_logs_b')
    LOGGER.debug('Debug from do_logs_b')