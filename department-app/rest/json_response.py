ERROR_MESSAGES = {
    400: 'Request body is invalid',
    404: 'Id does not exist'
}

def data_response(value):
    return {'data': value}

def error_response(code):
    return {'message': ERROR_MESSAGES.get(code)}, code