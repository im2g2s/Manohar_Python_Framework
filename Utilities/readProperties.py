import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\manoh\PycharmProjects\Manohar_Hybrid_Framework\Configurations\config.ini")

class Readconfig():

    @staticmethod
    def getApplicationURl():
        url = config.get('common','BaseURl')
        return url


    @staticmethod
    def getusername():
        username = config.get('common', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common', 'password')
        return  password

