import base64


class Login(dict):

    def __init__(self, login):
        super(Login, self).__init__()
        self.update(login)

    @property
    def access_token(self):
        return self.get('access_token')


class LoginClient(object):

    def __init__(self, api):
        self.api = api

    def login(self, username, password):
        assert username, password
        uri = 'login'
        headers = {}
        auth = base64.b64encode('{username}:{password}'
                                .format(username=username,
                                        password=password))
        headers.update({'Authorization': 'Basic {0}'.format(auth)})
        result, status = self.api.post(uri, headers=headers)
        self.api.headers.update({'Authorization':
                                 'Bearer ' + result['access_token']})
        return Login(result), status
