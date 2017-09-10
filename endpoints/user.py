class GETUserSpecifier(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/users/{userSpecifier}'

    # description of endpoint
    description = 'Fetch the user information for the specified user.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'userSpecifier', 'located': 'query', 'type': 'string', 'description': 'The User Specifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– User information has been successfully provided.'},
    ]

    # error msgs'
    error = ['401', '403', '405']

    # json schema representation
    schema = """
        {
            # 
            # An object containing supplied user information.
            # 
            userInfo : (InstrumentName),
        }
        """

class GETExternalInfo(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/users/{userSpecifier}/externalInfo'

    # description of endpoint
    description = 'Fetch the externally-available user information for the specified user.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'userSpecifier', 'located': 'query', 'type': 'string', 'description': 'The User Specifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– User information has been successfully provided.'},
    ]

    # error msgs'
    error = ['401', '403', '405']

    # json schema representation
    schema = """
        {
            # 
            # An object containing supplied user information.
            # 
            userInfo : (InstrumentName),
        }
        """



