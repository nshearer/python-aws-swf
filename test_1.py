'''
SWF Library Testing

WORKFLOW TYPE
Workflow Type Name:                         test-1
Workflow Type Version:                      1
Default Task List:                          default
Default Execution Start to Close Timeout:   24 hours
Default Task Start to Close Timeout:        24 hours
Default Task Priority:                      10
Default Child Policy:                       Terminate
Default Lambda Role:                        None


+--------------------+    +--------------------------+    +--------------------------+
|Task_1              +---->Task 2                    +---->Task 3                    |
| print "task 1"     |    | print "task 2"           |    | print "task 3: " + data  |
+--------------------+    | Send data to json        |    +------------------+-------+
                          +--------------------------+

ACTIVITY
Domain:                 python-swf-test
Activity Type Name:     Task_1
Activity Type Version:  1
Task List:              default

ACTIVITY
Domain:                 python-swf-test
Activity Type Name:     Task_2
Activity Type Version:  1
Task List:              default

ACTIVITY
Domain:                 python-swf-test
Activity Type Name:     Task_3
Activity Type Version:  1
Task List:              default

'''

import logging

from swf import SWFDecisionHandler, SWFDecider

REGION = 'us-west-2'
DOMAIN = 'python-swf-test'

WORKFLOW = 'test-1'
WF_VER = 1
TASKLKIST = 'default'

class Test1DecsionHandler(SWFDecisionHandler):

    def on_workflow_start(self, wf):
        self.start_activity('Task_1')

    def after_Task_1(self, wf):
        self.start_activity('Task_2')

    def after_Task_2(self, wf):
        print("WF data is " + str(wf.data))
        self.on_workflow_start('Task_3')

    def after_Task_3(self, wf):
        self.complete_workflow()


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)

    decider = SWFDecider('test_1.py', DOMAIN, TASKLKIST)
    decider.add(Test1DecsionHandler(WORKFLOW, WF_VER))
    decider.poll_forever()

