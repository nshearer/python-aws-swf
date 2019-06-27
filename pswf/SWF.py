from datetime import timedelta
from time import sleep

class SWF:
    '''Provides access to swf service'''

    def __init__(self, creds):
        '''
        :param cred: Credentials to access AWS
        TODO: Make creds optional?
        '''
        self.creds = creds

        self.__cooldown_start = timedelta(seconds=30)
        self.__cooldown_max = timedelta(minutes=15)
        self.__cooldown_current = None



    @property
    def swf(self):
        return self.creds.client('swf')


    def _paged_swf_request(self, boto_method, request_data, list_attr_name):
        '''
        List through a potentially paged set of results

        :param boto_method: Name of swf method to call
        :param request_data: The request details
        :param list_attr_name: The attribute in the returned data that has the list of items to return
        :return: Generator yield items returned
        '''
        boto_method = getattr(self.swf, boto_method)

        while True:
            results = boto_method(**request_data)
            for item in results[list_attr_name]:
                yield item
            if 'nextPageToken' not in results:
                return
            request_data['nextPageToken'] = results['nextPageToken']


    def cooldown(self):
        '''Method to trigger a pause to ensure we don't hammer the APIs'''

        # Record when cooldown cycle was started
        if self.__cooldown_current is None:
            self.__cooldown_current = self.__cooldown_start
        else:
            self.__cooldown_current = self.__cooldown_current * 2
            if self.__cooldown_current > self.__cooldown_max:
                self.__cooldown_current = self.__cooldown_max

        # Wait
        sleep(self.__cooldown_current.total_seconds())


    def reset_cooldown(self):
        '''Resets cooldown timers because a request succeeded'''
        self.__cooldown_current = None