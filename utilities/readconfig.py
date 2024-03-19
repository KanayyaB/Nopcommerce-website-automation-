import configparser
config = configparser.RawConfigParser()
config.read(".\\config.ini")

class Readconfig():
    @staticmethod
    def getapplicationurl():
        url=config.get('common info','baseURL')
        return url
    def getusername():
        username=config.get('common info','username')
        return username
    def getpassword():
        password=config.get('common info','password')
        return password
