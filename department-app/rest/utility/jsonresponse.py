"""Provides rest package with utility modules.

Exported modules:
    jsonresponse.py: Provides rest endpoints with response functions and messages.
"""


ERROR_MESSAGES = {
    400: 'Request body is invalid',
    404: 'Id does not exist'
}


def data_response(value):
    """Generates a json response object.

    Returns:
        A json serializable python dict
        with 'data' key.
    """
    return {'data': value}


def error_response(code):
    """Generates an error json response object.

    An error code is provided by user and the 
    error message is extracted from ERROR_MESSAGES
    dictionary.

    Returns:
        A tuple, consisting of and error code
        and a json serializable python dict
        with 'message' key.
    """
    return {'message': ERROR_MESSAGES.get(code)}, code
