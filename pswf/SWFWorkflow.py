import json

from botocore.errorfactory import ClientError

from .SWF import SWF
from .SWFExecution import SWFExecution
from .exceptions import WorkflowNameAlreadyExists


class SWFWorkflow(SWF):
    '''Handle to represent a workflow'''
    def __init__(self, domain, name, version=1, creds=None):
        '''
        :param domain: Domain the workflow is in
        :param name: Name to identify the workflow
        :param version: Version of the workflow
        '''
        super(SWFWorkflow, self).__init__(creds)
        self.domain = domain
        self.name = name
        self.version = version

    def __str__(self):
        return "{wfname}.{wfver}.{ver}".format(
            wfname = self.domain,
            wfver = self.name,
            ver = str(self.version))


    def execute(self, exec_name, data=None, decision_task_list=None, priority=None, encode_data_json=True):
        '''
        Start a new execution of the workflow

        :param exec_name: ID to identify this execution
        :param data: Data to submit to the workflow
        :param decision_task_list:
            Override the default decision task list
            (perhaps to change which decider picks it up)
        :param priority:
            change WF decision task priority
            (default 0, > = higher priority)
        :param encode_data_json: Whether to encode data into json
        :return: SWFExecution
        '''

        args = {
            'domain':       self.domain,
            'workflowId':   str(exec_name),
            'workflowType': {
                'name': self.name,
                'version': str(self.version),
            },
        }

        if decision_task_list is not None:
            args['taskList'] = {'name': decision_task_list}

        if priority is not None:
            args['taskPriority'] = str(priority)

        if encode_data_json and data is not None:
            data = json.dumps(data)

        if data is not None:
            args['input'] = data

        try:
            result = self.swf.start_workflow_execution(**args)
        except ClientError as e:
            if e.__class__.__name__ == 'WorkflowExecutionAlreadyStartedFault':
                raise WorkflowNameAlreadyExists(str(e))

        return SWFExecution(
            domain = self.domain,
            wfname = self.name,
            exec_name = exec_name,
            run_id = result['runId'],
            creds = self.creds)

