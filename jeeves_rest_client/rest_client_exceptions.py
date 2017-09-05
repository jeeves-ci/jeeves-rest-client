import json


class JeevesHttpError(IOError):
    def __init__(self, res, status_code):
        response = json.loads(res.content)
        self.message = response.get('message')
        self.status_code = status_code
        super(JeevesHttpError, self).__init__(self.message)


class JeevesMasterServerError(JeevesHttpError):
    def __init__(self, res, status_code):
        super(JeevesMasterServerError, self).__init__(res, status_code)


class JeevesClientError(JeevesHttpError):
    def __init__(self, res, status_code):
        super(JeevesClientError, self).__init__(res, status_code)
