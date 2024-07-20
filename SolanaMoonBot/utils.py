from pathlib import Path

def get_root_dir():
    """ Get the root directory of the application
    
        Retunrs:
            pathlib.Path the root directory of the 
            application
    """
    return Path.cwd().parent


def create_dir_in_root_dir(dirname: str):
    """ Make directory in the root directory
    
        Args:
            dirname: Name of the directory to be created
    """
    try:
        path = Path.joinpath(get_root_dir(), dirname)
        Path.mkdir(path)
    except FileExistsError as e:
        pass


def attach_file_extention(file_name: str, ext: str):
    """ Append extension to the file
    
        Args:
            file_name: Name of the source file 
            ext: Extention to attach to the file
            
        Returns:
            str: a complete string of the file with it's 
            extension
    """
    
    return f"{file_name}.{ext}"
    