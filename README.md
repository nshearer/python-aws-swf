Python Simple Workflow Library
==============================

AWS SWF is an AWS service to orchestrate processes across multiple devices.
Learn more at https://aws.amazon.com/swf/.  Please take a look at that documentation
and make sure you understand these key SWF concepts before proceeding:

 - Deciders
 - Decision Tasks
 - Events
 - Activity Tasks
 - Workers
 
Also, if you're new to SWF, please take the time to run through this awesome tutorial
by Mitch Garnaat: http://boto.cloudhackers.com/en/latest/swf_tut.html

This library isn't so much a direct mapping of Python calls to SWF enpoints, as much as 
an attempt at making it faster to implement the SWF Decider by wrapping common SWF usage
patterns into a more Pythonic model.  The key mechanics that have been developed to
accomplish this is are:

 - The Event Loop
 - The WF Data Extractor


Event Loop
----------

A common pattern seen in the SWF decider is to:

 1. Wait for an event
 2. Examine the workflow history (event list) to determine what the last event was
 3. Decide what activity to do next based on the last event
 
From http://boto.cloudhackers.com/en/latest/swf_tut.html, that looks like:

    history = self.poll()
    if 'events' in history:
        # Get a list of non-decision events to see what event came in last.
        workflow_events = [e for e in history['events']
                           if not e['eventType'].startswith('Decision')]
        decisions = swf.Layer1Decisions()
        # Record latest non-decision event.
        last_event = workflow_events[-1]
        last_event_type = last_event['eventType']
        if last_event_type == 'WorkflowExecutionStarted':
            # Schedule the first activity.
            decisions.schedule_activity_task('%s-%i' % ('ActivityA', time.time()),
               'ActivityA', self.version, task_list='a_tasks')
        elif last_event_type == 'ActivityTaskCompleted':
            # Take decision based on the name of activity that has just completed.
            # 1) Get activity's event id.
            last_event_attrs = last_event['activityTaskCompletedEventAttributes']
            completed_activity_id = last_event_attrs['scheduledEventId'] - 1
            # 2) Extract its name.
            activity_data = history['events'][completed_activity_id]
            activity_attrs = activity_data['activityTaskScheduledEventAttributes']
            activity_name = activity_attrs['activityType']['name']
            # 3) Optionally, get the result from the activity.
            result = last_event['activityTaskCompletedEventAttributes'].get('result')

            # Take the decision.
            if activity_name == 'ActivityA':
                decisions.schedule_activity_task('%s-%i' % ('ActivityB', time.time()),
                    'ActivityB', self.version, task_list='b_tasks', input=result)
            if activity_name == 'ActivityB':
                decisions.schedule_activity_task('%s-%i' % ('ActivityC', time.time()),
                    'ActivityC', self.version, task_list='c_tasks', input=result)
            elif activity_name == 'ActivityC':
                # Final activity completed. We're done.
                decisions.complete_workflow_execution()

        self.complete(decisions=decisions)
        return True
            
This library attempts to abstract that common behaviour into a base class and
allow you to rewrite that code as:

    class MyWorkflowDecider(SWFDecider):
    
        def on_workflow_start():
            self.start_activity('%s-%i' % ('ActivityA', time.time()),
               'ActivityA', self.version, task_list='a_tasks')
            
        def after_activity_a(event, result):
            self.start_activity('%s-%i' % ('ActivityB', time.time()),
                'ActivityB', self.version, task_list='b_tasks', input=result)

        def after_activity_b(event, result):
            self.start_activity('%s-%i' % ('ActivityC', time.time()),
                'ActivityC', self.version, task_list='b_tasks', input=result)

        def after_activity_c(event, result):
            self.complete_workflow()


