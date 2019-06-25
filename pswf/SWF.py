


class SWF:
    '''Provides access to swf service'''

    def __init__(self, creds):
        '''
        :param cred: Credentials to access AWS
        TODO: Make creds optional?
        '''
        self.creds = creds


    @property
    def swf(self):
        return self.creds.client('swf')

