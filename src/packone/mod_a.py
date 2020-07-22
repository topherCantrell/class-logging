import logging

from packone.packtwo import mod_b

LOGGER = logging.getLogger('one.a')

def do_logs_a():
        
    LOGGER.error('Error from do_logs_a')
    LOGGER.info('Info from do_logs_a')
    LOGGER.debug('Debug from do_logs_a')
    
    mod_b.do_logs_b()
    