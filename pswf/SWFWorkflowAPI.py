import json

from botocore.errorfactory import ClientError

from .SWF import SWF
from .exceptions import WorkflowNameAlreadyExists


class SWFWorkflowAPI(SWF):
    '''Base class for accessing Workflow details through SWF'''

    def __init__(self, domain=None, name=None, version=1, creds=None, copyfrom=None):
        '''
        :param domain: Domain the workflow is in
        :param name: Name to identify the workflow
        :param version: Version of the workflow
        :param copyfrom: If specified, copy parameters from this SWFWorkflow object
        '''

        if copyfrom is not None:
            domain = copyfrom.domain
            name = copyfrom.wfname
            version = copyfrom.version
            creds = copyfrom.creds

        super(SWFWorkflowAPI, self).__init__(creds)

        if domain is None:
            raise Exception("domain is required")
        if name is None:
            raise Exception("name is required")
        if version is None:
            raise Exception("version is required")

        self.domain = domain
        self.wfname = name
        self.version = str(version)


    def __str__(self):
        return "{wfname}.{wfver}.{ver}".format(
            wfname = self.domain,
            wfver = self.name,
            ver = str(self.version))


    def _get_workflow_parms(self):
        '''
        Get typical paramters to identify workflow in a request
        :return: dict
        '''
        return {
            'domain':       self.domain,
            'workflowType': {
                'name': self.wfname,
                'version': str(self.version),
            },
        }


    def _add_workflow_parms(self, request_dict):
        '''
        Add workflow identification parameters to request data
        '''
        for k, v in self._get_workflow_parms():
            request_dict[k] = v
