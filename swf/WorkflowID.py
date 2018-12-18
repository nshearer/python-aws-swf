
class WorkflowID:
    '''Identify a workflow'''
    def __init__(self, wfname, wfver, wfid):
        self.__wfname = wfname
        self.__wfver = wfver
        self.__wfid = wfid

    @property
    def wfname(self):
        '''The user friendly name of the workflow'''
        return self.__wfname
    @property
    def wfid(self):
        '''The unique ID of the workflow'''
        return self.__wfid
    @property
    def wfver(self):
        '''The version of the workflow'''
        return self.__wfver

    def __str__(self):
        return "{wfname}.{wfver} ({wfid})".format(
            wfname = self.workflow_name,
            wfver = self.workflow_version,
            wfid=self.workflow_id)

    def hash(self, wfid):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)

    @property
    def workflow(self):
        '''Used if you want the workflow ID, not the subclassed ID'''
        return WorkflowID(self.__wfname, self.__wfver, self.__wfid)


class WokflowExecutionID(WorkflowID):
    '''Identify an execution of a workflow'''
    def __init__(self, wfname, wfver, wfid, run_id):
        super().__init__(wfname, wfver, wfid)
        self.__run_id = run_id
    @property
    def run_id(self):
        '''Unique ID of this workflow execution'''
        return self.__run_id

    def __str__(self):
        return "{wf} instance {run_id}".format(
            wf = super().__str__(),
            run_id=self.run_id)
