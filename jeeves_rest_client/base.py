import base64
import requests

from rest_client_exceptions import JeevesMasterServerError


class HttpClient(object):

    def __init__(self, endpoint_url, username=None, password=None, headers={}):
        self.headers = self._init_headers(username, password, headers)
        self.endpoint_url = endpoint_url

    def _init_headers(self, username, password, headers):
        if username and password:
            auth = base64.b64encode('{username}:{password}'
                                    .format(username=username,
                                            password=password))
            headers.update({'Authorization': 'Basic {0}'.format(auth)})
        return headers

    def get(self, uri, params={}, headers={}, **kwargs):
        return self._do_request(method='GET',
                                uri=uri,
                                headers=headers,
                                params=params,
                                **kwargs)

    def delete(self, uri,
               params={},
               data=None,
               headers={},
               **kwargs):
        return self._do_request(method='DELETE',
                                uri=uri,
                                headers=headers,
                                params=params,
                                data=data,
                                **kwargs)

    def post(self, uri,
             params={},
             data={},
             headers={},
             **kwargs):
        return self._do_request(method='POST',
                                uri=uri,
                                headers=headers,
                                params=params,
                                data=data,
                                **kwargs)

    def put(self, uri,
            params={},
            data={},
            headers={},
            **kwargs):
        return self._do_request(method='PUT',
                                uri=uri,
                                headers=headers,
                                params=params,
                                data=data,
                                **kwargs)

    def _do_request(self,
                    method,
                    uri,
                    headers={},
                    params={},
                    data=None,
                    stream=False,
                    **kwargs):
        base_headers = self.headers.copy()
        base_headers.update(headers)
        url = self._create_url(uri, params)

        res = requests.request(method=method,
                               url=url,
                               headers=headers,
                               data=data,
                               params=params,
                               stream=stream,
                               **kwargs)
        if res.status_code == 500:
            raise JeevesMasterServerError(res)
        return res.json(), res.status_code

    def _create_url(self, uri, params):
        url = '{0}{1}'.format(self.endpoint_url, uri)
        # for param in params:
        #     url += '/{0}'.format(param)
        return url
