
class SWFDecisionHandler:
    '''
    Base class for defining handlers that make the decisions to direct SWF Workflows
    '''

    def __init__(self, workflow_name, workflow_version=None):
        '''
        :param workflow_name:
            Name of the workflow to handle decisions for.
        :param workflow_version:
            Version of the workflow to handle decisions for.
            If None, will match any version
        '''
        self.__workflow_name = workflow_name
        self.__workflow_ver = workflow_version


    def should_handle(self, task):
        '''
        Decide if this handler should handle the decision

        :param task: SWFDecisionTask
        :return: bool
        '''

        if task.workflow_name == self.__workflow_name:
            if task.workflow_version == self.__workflow_ver:
                return True
        return False
