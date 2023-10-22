from API.Utilities.http_utils.api_request import ApiRequest


def send_request(url, http_type, header, body=None, authorization=None, files=None,
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
    req_obj = ApiRequest()
    req_obj.set_attribute(url=url, http_type=http_type, header=header, body=body, authorization=authorization,
                          files=files, data=data, params=params)
    return req_obj.trigger_request()
