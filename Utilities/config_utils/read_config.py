import configparser
import os


class ReadConfig:

    @staticmethod
    def get_config_file():
        """Load the file based on environment"""
        os.environ["env"] = 'stg'
        if os.environ["env"] == 'prod':
            config = configparser.RawConfigParser()
            config.read("environment/stg/config.ini")
            return config
        else:
            config = configparser.RawConfigParser()
            config.read("API/environment/stg/config.ini")
            return config
