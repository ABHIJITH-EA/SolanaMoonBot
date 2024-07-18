
import config

import os
import logging

class Formatter(logging.Formatter):
    pass


def log_handler_path(file_name: str):
    """ set up log file destination path
    
        Args:
            file_name:
                Name of the log file
                
        Returns:
            str:
                A path like string

    """
    
    log_file = file_name + '.log'
    handler_path = os.path.join(config.log_dir, log_file)
    
    return handler_path

def get_bot_logger() -> None:
    """ Set up logger for the application

        Returns:
            logging.Logger a logger instances configured with
            custom formatter and handlers added from the application's
            logging module.
    """
    logger = logging.getLogger(config.bot_logger)
    
    handler_name = log_handler_path(config.bot_log_filename)
    logger.addHandler(handler_name)
    
    log_level = os.getenv('LOG_LEVEL') or config.log_level
    
    logger.setLevel(log_level)
    
    return logger