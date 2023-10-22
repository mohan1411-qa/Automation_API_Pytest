from API.Utilities.env_utils.envir_utils import get_api_endpoint
from API.Utilities.http_utils.requests_utils import send_request
from API.environment.endpoints.Constant import UserConstants


def list_users(page_number=2):
    url = get_api_endpoint(UserConstants.LIST_USERS)
    api_url = url + "page=" + str(page_number)
    resp_obj = send_request(url=api_url, http_type='get', header={})

    print(resp_obj)
    return resp_obj


def list_all_users():
    json_data = []
    i = 0
    while True:
        resp_obj = list_users(page_number=i)
        if resp_obj.status_code == 200:

            response = resp_obj.json()
            i += 1
            if len(response['data']) == 0:
                break
            for item in response['data']:
                json_data.append(item)

    return json_data
