import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getStudentUseremail():
        studentUsername = config.get('common info', 'studentUsermail')
        return studentUsername

    @staticmethod
    def getStudentPassword():
        StudentPassword = config.get('common info', 'studentPassword')
        return StudentPassword

