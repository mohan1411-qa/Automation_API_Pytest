import json
from enum import Enum

import os

from API.Utilities.config_utils.read_config import ReadConfig


def get_base_url(url_key):
    """Get base url """
    config = ReadConfig.get_config_file()
    url = config.get('common_info', url_key)
    return url


def get_api_endpoint(end_point: Enum, url_key='base_url'):
    """Method to get the endpoint"""
    end_point_val = end_point.value
    base_url = get_base_url(url_key)
    resource_url = get_api_url(end_point_val)
    final_url = resource_url.format(base_url)
    return final_url


def get_api_url(val):
    """Method to get the api
    This method fetches the base url and endpoint and concatenate
    and return the api url"""
    cur_path = os.path.dirname(__file__)
    root_path = os.path.abspath(cur_path)
    json_path = root_path + "\\..\\..\\environment\\endpoints\\url.json"
    with open(json_path, "r") as file:
        data = json.load(file)

    return data[val]

