
import config
import utils

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
    
    log_file = utils.attach_file_extention(file_name, 'log')
    handler_path = os.path.join(utils.get_root_dir(), 
                                config.log_dir, log_file)
    
    return handler_path

def get_bot_logger() -> logging.Logger:
    """ Set up logger for the application

        Returns:
            logging.Logger a logger instances configured with
            custom formatter and handlers added from the application's
            logging module.
    """
    logger = logging.getLogger(config.bot_logger)
    
    handler_name = log_handler_path(config.bot_log_filename)
    
    if not os.path.exists(handler_name):
        utils.create_dir_in_root_dir(config.log_dir)
    
    handler = logging.FileHandler(handler_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    
    log_level = os.getenv('LOG_LEVEL') or config.log_level
    logger.setLevel(log_level)
    
    return logger