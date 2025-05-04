import sys

def error_message_detail(error, error_detail: sys):
    '''
    This function takes an error and its details as input and retuns a 
    formatted string containing the error message and its details.
    '''

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}]"
    error_message += f"\n error message [{error}]"

    return error_message

class CustomException(Exception):
    '''
    This is a custom exception class that inherits from the built-in Exception Class.
    It takes an error message and its details as input and returns a formatted string
    containing the error message and its details.
    '''

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message) # calling the constructor of the parent class
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
