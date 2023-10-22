import pytest

from API.Utilities.env_utils.envir_utils import get_api_url, get_api_endpoint
from API.environment.endpoints.Constant import UserConstants
from API.TestSuite.UserDetailsTest.usecases import user_details
from API.TestSuite.UserCreationTest.usecases import user_creation
from API.assertions.validate_list_user_api import assert_list_user, assert_specific_user_in_list_user
import logging

import API.Utilities.log_utils.customLogger as cl


@pytest.mark.usefixtures("setUp")
class TestUserDetails:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.log = cl.custom_logger(logging.DEBUG)

    @pytest.mark.Regression
    def test_list_user(self):
        list_user_resp_data = user_details.list_all_users()
        assert_list_user(list_user_resp_data)

        self.log.info(f'User Data List = {list_user_resp_data}')
        assert_specific_user_in_list_user(list_user_resp_data,
                                          user_id=6,
                                          email='tracey.ramos@reqres.in',
                                          first_name='Tracey',
                                          last_name='Ramos')
