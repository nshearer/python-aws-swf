
from .SWFWorkflowAPI import SWFWorkflowAPI


class SWFExecution(SWFWorkflowAPI):
    '''Handle to represent a single execution of a workflow'''
    def __init__(self, run_id, domain=None, wfname=None, exec_name=None, version=1, creds=None, copyfrom=None):
        '''
        :param domain: Domain the workflow is in
        :param wfname: Name to identify the workflow
        :param version: Version of the workflow
        :param exec_name: User provided ID for execution
        :param run_id: SWF generated run ID to identify the execution
        :param copyfrom: If specified, copy Workflow parameters from this SWFWorkflow object
        '''
        super(SWFExecution, self).__init__(
            domain = domain,
            name = wfname,
            version = version,
            creds = creds,
            copyfrom = copyfrom,
        )

        # Execution details
        self.run_id = run_id
        self.exec_name = exec_name


    def __str__(self):
        return "{wfname}.{wfver}.{ver}[{exec_id}]".format(
            wfname = self.domain,
            wfver = self.wfname,
            ver = str(self.version),
            exec_id = self.exec_id)

