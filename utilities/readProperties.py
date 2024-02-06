import configparser
import os

config = configparser.RawConfigParser()
# config.read(f"{os.getcwd()}\\Configuraions\\config.ini")
# config.read(".\\Configuraions\\config.ini")
config.read("C:\\Users\\SAI-PC\\Desktop\\pythonProject001\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        email = config.get('common_info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

