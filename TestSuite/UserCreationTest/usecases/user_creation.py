from API.Utilities.env_utils.envir_utils import get_api_endpoint
from API.Utilities.http_utils.requests_utils import send_request
from API.environment.endpoints.Constant import UserConstants
from API.Utilities.json_utils.json_utils import get_payload_json
from API.payloads.config import JSONPATH


def create_user(name, job):
    url = get_api_endpoint(UserConstants.LIST_USERS)
    payload = get_payload_json(JSONPATH.CREATE_USER.value)
    payload['name'] = name
    payload['job'] = job
    resp_obj = send_request(url=url, http_type='post', header={}, body=payload)

    return resp_obj
