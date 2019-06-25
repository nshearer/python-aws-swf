
import boto3

class AWSCredentials:

    def __init__(self, region, aws_key_id, aws_secret):
        '''
        :param region: Region being accessed
        :param key_id: AWS Key ID for accessing SWF service
        :param secret: AWS Secret for accessing SWF service
        '''
        self.__region = region
        self.__aws_key_id = aws_key_id
        self.__aws_secret = aws_secret
        self.__clients = dict()

    @property
    def region(self):
        return self.__region


    def client(self, name):
        if name not in self.__clients:
            self.__clients[name] = boto3.client(name,
                aws_access_key_id = self.__aws_key_id,
                aws_secret_access_key = self.__aws_secret,
                region_name = self.__region)
        return self.__clients[name]
