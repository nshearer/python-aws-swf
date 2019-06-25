

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

