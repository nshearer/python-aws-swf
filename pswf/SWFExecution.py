
from .SWF import SWF

class SWFExecution(SWF):
    '''Handle to represent a single execution of a workflow'''
    def __init__(self, domain, wfname, exec_name, run_id, version=1, creds=None):
        '''
        :param domain: Domain the workflow is in
        :param wfname: Name to identify the workflow
        :param version: Version of the workflow
        :param exec_name: User provided ID for execution
        :param run_id: SWF generated run ID to identify the execution
        '''
        super(SWFExecution, self).__init__(creds)
        self.domain = domain
        self.wfname = wfname
        self.version = version
        self.exec_name = exec_name
        self.run_id = run_id

    def __str__(self):
        return "{wfname}.{wfver}.{ver}[{exec_id}]".format(
            wfname = self.domain,
            wfver = self.wfname,
            ver = str(self.version),
            exec_id = self.exec_id)


