import json


class JeevesMasterServerError(Exception):
    def __init__(self, res):
        response = json.loads(res.content)
        self.message = response.get('message')
        super(JeevesMasterServerError, self).__init__(self.message)
