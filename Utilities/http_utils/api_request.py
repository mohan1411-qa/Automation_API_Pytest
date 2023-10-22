
import requests

from API.Utilities.http_utils.config import HTTP_METHODS


class ApiRequest:

    def __init__(self):
        self.params = None
        self.data = None
        self.files = None
        self.authorization = None
        self.body = None
        self.header = None
        self.http_type = None
        self.url = None

    def set_attribute(self, url, http_type, header, body=None, authorization=None, files=None,
                      data=None, params=None):
        """

        :param url: final url for api request
        :param http_type: http method type
        :param header: header of request
        :param body: payload of request
        :param authorization: token for api request
        :param files: attachment - img/file
        :param data: any data
        :param params: params of request
        :return:
        """
        self.url = url
        self.http_type = http_type
        self.header = header
        self.body = body
        self.authorization = authorization
        self.files = files
        self.data = data
        self.params = params

    def trigger_request(self):
        if self.http_type.lower() == HTTP_METHODS.POST.value:
            resp_obj = requests.post(url=self.url, data=self.body, headers=self.header, params=self.params)

            return resp_obj

        elif self.http_type.lower() == HTTP_METHODS.GET.value:
            resp_obj = requests.get(url=self.url, headers=self.header, params=self.params)

            return resp_obj

        elif self.http_type.lower() == HTTP_METHODS.DELETE.value:
            resp_obj = requests.delete(url=self.url, headers=self.header, params=self.params)

            return resp_obj
