import requests

from rest_client_exceptions import (JeevesMasterServerError,
                                    JeevesClientError)


class HttpClient(object):

    def __init__(self, endpoint_url, headers={}):
        self.headers = headers
        self.endpoint_url = endpoint_url

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
        headers.update({'Content-Type': 'application/json'})
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
                               headers=base_headers,
                               data=data,
                               params=params,
                               stream=stream,
                               **kwargs)
        if res.status_code >= 500:
            raise JeevesMasterServerError(res, res.status_code)
        if res.status_code >= 400:
            raise JeevesClientError(res, res.status_code)
        return res.json(), res.status_code

    def _create_url(self, uri, params):
        url = '{0}{1}'.format(self.endpoint_url, uri)
        # for param in params:
        #     url += '/{0}'.format(param)
        return url
