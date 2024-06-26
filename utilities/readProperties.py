import configparser
import os
import yaml

config = configparser.RawConfigParser()
# config.read(f"{os.getcwd()}\\Configuraions\\config.ini")
# config.read(".\\Configuraions\\config.ini")
config.read(f"{os.getcwd()}\\Configurations\\config.ini")


# ONLY FOR YAML
def load_yaml_file(file):
    with open(file, "r") as file:
        return yaml.safe_load(file)


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        email = config.get('common_info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password
