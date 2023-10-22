from enum import Enum
import os

cur_path = os.path.dirname(__file__)
root_path = os.path.abspath(cur_path)


class JSONPATH(Enum):
    CREATE_USER = root_path + "\\CreateUser\\create_user.json"
