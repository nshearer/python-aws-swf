import json
from datetime import datetime, timedelta

from botocore.errorfactory import ClientError

from .SWF import SWF
from .SWFWorkflowAPI import SWFWorkflowAPI
from .SWFExecution import SWFExecution
from .exceptions import WorkflowNameAlreadyExists, WorkflowNameDoesntExist


class SWFWorkflow(SWFWorkflowAPI):
    '''Handle to represent a workflow'''


    def __str__(self):
        return "{domain}.{wfname}.{ver}".format(
            domain = self.domain,
            wfname = self.wfname,
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

        args = self._get_workflow_parms()

        args['workflowId'] = str(exec_name)

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
            copyfrom=self,
            run_id = result['runId'])


    def find_workflow(self, exec_name):
        """
        Find a workflow from it's name

        SWF Workflows can have a name specified when executing it, and a SWF generated run_id.
        There can be only one *running* workflow with a given name at a time.

        This method locates the workflow by it's name given on execution.

        Only returns active executions started in the last year

        :param exec_name: Name given when executing the workflow.
        :param workflow: SWFWorkflow to look for name in
        """

        args = {
            'domain': self.domain,
        }

        # Filter by exec_name
        args['executionFilter'] = {
            'workflowId': exec_name
        }

        # Have to filter by startTime
        args['startTimeFilter'] = {
            'oldestDate': datetime.now() - timedelta(days=365)
        }

        # Have to filter by workflow name manually since can't specify in filter
        results = list()
        for exec_info in self._paged_swf_request(self.swf.list_open_workflow_executions, args, 'executionInfos'):
            if exec_info['workflowType'] == {'name': self.wfname, 'version': self.version}:
                results.append(exec_info)

        if len(results) == 1:
            return SWFExecution(
                copyfrom=self,
                run_id = results[0]['execution']['runId'],
                exec_name = exec_name)
        elif len(results) == 0:
            raise WorkflowNameDoesntExist()
        else:
            raise Exception("%d results returned when searching for workflow execution '%s'" % (exec_name))


    @staticmethod
    def list_domains(creds, active=True):
        '''
        List domains visible to the current user

        :param creds: Credentials to use to access SWF
        :param active: If True, return active domains, else list deprecated
        :return: list of dict
            See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.list_domains
        '''
        if active:
            args = {'registrationStatus': 'REGISTERED'}
        else:
            args = {'registrationStatus': 'DEPRECATED'}

        swf = SWF(creds=creds)
        for domain in swf._paged_swf_request('list_domains', args, 'domainInfos'):
            yield domain


    @staticmethod
    def list_workflows(domain, creds, active=True):
        '''
        List domains visible to the current user

        :param domain: Name of the domain to look in
        :param creds: Credentials to use to access SWF
        :param active: If True, return active workflows, else list deprecated
        :return:
        '''
        if active:
            args = {'domain': domain, 'registrationStatus': 'REGISTERED'}
        else:
            args = {'domain': domain, 'registrationStatus': 'DEPRECATED'}

        swf = SWF(creds=creds)
        for wfinfo in swf._paged_swf_request('list_workflow_types', args, 'typeInfos'):
            yield SWFWorkflow(
                domain = domain,
                name = wfinfo['workflowType']['name'],
                version = wfinfo['workflowType']['version'],
                creds = creds,
            )


    @property
    def active_execution_count(self):
        '''Get a count of active executions'''

        args = self._get_workflow_filter_parms()
        result = self.swf.count_open_workflow_executions(**args)
        return int(result['count'])


    def list_executions(self):
        '''Get a list of running workflow executions'''

        args = self._get_workflow_filter_parms()

        for exec_info in self._paged_swf_request('list_open_workflow_executions', args, 'executionInfos'):
            yield SWFExecution(
                run_id = exec_info['execution']['runId'],
                exec_name = exec_info['execution']['workflowId'],
                copyfrom = self,
            )

