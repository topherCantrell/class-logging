import logging

LOGGER = logging.getLogger('three.c')

def do_logs_c():
    LOGGER.error('Error from do_logs_c')
    LOGGER.info('Info from do_logs_c')
    LOGGER.debug('Debug from do_logs_c')