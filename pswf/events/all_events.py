from .ActivityTaskCancelRequestedEvent import ActivityTaskCancelRequestedEvent
from .ActivityTaskCanceledEvent import ActivityTaskCanceledEvent
from .ActivityTaskCompletedEvent import ActivityTaskCompletedEvent
from .ActivityTaskFailedEvent import ActivityTaskFailedEvent
from .ActivityTaskScheduledEvent import ActivityTaskScheduledEvent
from .ActivityTaskStartedEvent import ActivityTaskStartedEvent
from .ActivityTaskTimedOutEvent import ActivityTaskTimedOutEvent
from .CancelTimerFailedEvent import CancelTimerFailedEvent
from .CancelWorkflowExecutionFailedEvent import CancelWorkflowExecutionFailedEvent
from .ChildWorkflowExecutionCanceledEvent import ChildWorkflowExecutionCanceledEvent
from .ChildWorkflowExecutionCompletedEvent import ChildWorkflowExecutionCompletedEvent
from .ChildWorkflowExecutionFailedEvent import ChildWorkflowExecutionFailedEvent
from .ChildWorkflowExecutionStartedEvent import ChildWorkflowExecutionStartedEvent
from .ChildWorkflowExecutionTerminatedEvent import ChildWorkflowExecutionTerminatedEvent
from .ChildWorkflowExecutionTimedOutEvent import ChildWorkflowExecutionTimedOutEvent
from .CompleteWorkflowExecutionFailedEvent import CompleteWorkflowExecutionFailedEvent
from .ContinueAsNewWorkflowExecutionFailedEvent import ContinueAsNewWorkflowExecutionFailedEvent
from .DecisionTaskCompletedEvent import DecisionTaskCompletedEvent
from .DecisionTaskScheduledEvent import DecisionTaskScheduledEvent
from .DecisionTaskStartedEvent import DecisionTaskStartedEvent
from .DecisionTaskTimedOutEvent import DecisionTaskTimedOutEvent
from .ExternalWorkflowExecutionCancelRequestedEvent import ExternalWorkflowExecutionCancelRequestedEvent
from .ExternalWorkflowExecutionSignaledEvent import ExternalWorkflowExecutionSignaledEvent
from .FailWorkflowExecutionFailedEvent import FailWorkflowExecutionFailedEvent
from .LambdaFunctionCompletedEvent import LambdaFunctionCompletedEvent
from .LambdaFunctionFailedEvent import LambdaFunctionFailedEvent
from .LambdaFunctionScheduledEvent import LambdaFunctionScheduledEvent
from .LambdaFunctionStartedEvent import LambdaFunctionStartedEvent
from .LambdaFunctionTimedOutEvent import LambdaFunctionTimedOutEvent
from .MarkerRecordedEvent import MarkerRecordedEvent
from .RecordMarkerFailedEvent import RecordMarkerFailedEvent
from .RequestCancelActivityTaskFailedEvent import RequestCancelActivityTaskFailedEvent
from .RequestCancelExternalWorkflowExecutionFailedEvent import RequestCancelExternalWorkflowExecutionFailedEvent
from .RequestCancelExternalWorkflowExecutionInitiatedEvent import RequestCancelExternalWorkflowExecutionInitiatedEvent
from .ScheduleActivityTaskFailedEvent import ScheduleActivityTaskFailedEvent
from .ScheduleLambdaFunctionFailedEvent import ScheduleLambdaFunctionFailedEvent
from .SignalExternalWorkflowExecutionFailedEvent import SignalExternalWorkflowExecutionFailedEvent
from .SignalExternalWorkflowExecutionInitiatedEvent import SignalExternalWorkflowExecutionInitiatedEvent
from .StartChildWorkflowExecutionFailedEvent import StartChildWorkflowExecutionFailedEvent
from .StartChildWorkflowExecutionInitiatedEvent import StartChildWorkflowExecutionInitiatedEvent
from .StartLambdaFunctionFailedEvent import StartLambdaFunctionFailedEvent
from .StartTimerFailedEvent import StartTimerFailedEvent
from .TimerCanceledEvent import TimerCanceledEvent
from .TimerFiredEvent import TimerFiredEvent
from .TimerStartedEvent import TimerStartedEvent
from .WorkflowExecutionCancelRequestedEvent import WorkflowExecutionCancelRequestedEvent
from .WorkflowExecutionCanceledEvent import WorkflowExecutionCanceledEvent
from .WorkflowExecutionCompletedEvent import WorkflowExecutionCompletedEvent
from .WorkflowExecutionContinuedAsNewEvent import WorkflowExecutionContinuedAsNewEvent
from .WorkflowExecutionFailedEvent import WorkflowExecutionFailedEvent
from .WorkflowExecutionSignaledEvent import WorkflowExecutionSignaledEvent
from .WorkflowExecutionStartedEvent import WorkflowExecutionStartedEvent
from .WorkflowExecutionTerminatedEvent import WorkflowExecutionTerminatedEvent
from .WorkflowExecutionTimedOutEvent import WorkflowExecutionTimedOutEvent

SWF_EVENT_CLASSES = {
    'activityTaskCancelRequestedEvent': ActivityTaskCancelRequestedEvent,
    'activityTaskCanceledEvent': ActivityTaskCanceledEvent,
    'activityTaskCompletedEvent': ActivityTaskCompletedEvent,
    'activityTaskFailedEvent': ActivityTaskFailedEvent,
    'activityTaskScheduledEvent': ActivityTaskScheduledEvent,
    'activityTaskStartedEvent': ActivityTaskStartedEvent,
    'activityTaskTimedOutEvent': ActivityTaskTimedOutEvent,
    'cancelTimerFailedEvent': CancelTimerFailedEvent,
    'cancelWorkflowExecutionFailedEvent': CancelWorkflowExecutionFailedEvent,
    'childWorkflowExecutionCanceledEvent': ChildWorkflowExecutionCanceledEvent,
    'childWorkflowExecutionCompletedEvent': ChildWorkflowExecutionCompletedEvent,
    'childWorkflowExecutionFailedEvent': ChildWorkflowExecutionFailedEvent,
    'childWorkflowExecutionStartedEvent': ChildWorkflowExecutionStartedEvent,
    'childWorkflowExecutionTerminatedEvent': ChildWorkflowExecutionTerminatedEvent,
    'childWorkflowExecutionTimedOutEvent': ChildWorkflowExecutionTimedOutEvent,
    'completeWorkflowExecutionFailedEvent': CompleteWorkflowExecutionFailedEvent,
    'continueAsNewWorkflowExecutionFailedEvent': ContinueAsNewWorkflowExecutionFailedEvent,
    'decisionTaskCompletedEvent': DecisionTaskCompletedEvent,
    'decisionTaskScheduledEvent': DecisionTaskScheduledEvent,
    'decisionTaskStartedEvent': DecisionTaskStartedEvent,
    'decisionTaskTimedOutEvent': DecisionTaskTimedOutEvent,
    'externalWorkflowExecutionCancelRequestedEvent': ExternalWorkflowExecutionCancelRequestedEvent,
    'externalWorkflowExecutionSignaledEvent': ExternalWorkflowExecutionSignaledEvent,
    'failWorkflowExecutionFailedEvent': FailWorkflowExecutionFailedEvent,
    'lambdaFunctionCompletedEvent': LambdaFunctionCompletedEvent,
    'lambdaFunctionFailedEvent': LambdaFunctionFailedEvent,
    'lambdaFunctionScheduledEvent': LambdaFunctionScheduledEvent,
    'lambdaFunctionStartedEvent': LambdaFunctionStartedEvent,
    'lambdaFunctionTimedOutEvent': LambdaFunctionTimedOutEvent,
    'markerRecordedEvent': MarkerRecordedEvent,
    'recordMarkerFailedEvent': RecordMarkerFailedEvent,
    'requestCancelActivityTaskFailedEvent': RequestCancelActivityTaskFailedEvent,
    'requestCancelExternalWorkflowExecutionFailedEvent': RequestCancelExternalWorkflowExecutionFailedEvent,
    'requestCancelExternalWorkflowExecutionInitiatedEvent': RequestCancelExternalWorkflowExecutionInitiatedEvent,
    'scheduleActivityTaskFailedEvent': ScheduleActivityTaskFailedEvent,
    'scheduleLambdaFunctionFailedEvent': ScheduleLambdaFunctionFailedEvent,
    'signalExternalWorkflowExecutionFailedEvent': SignalExternalWorkflowExecutionFailedEvent,
    'signalExternalWorkflowExecutionInitiatedEvent': SignalExternalWorkflowExecutionInitiatedEvent,
    'startChildWorkflowExecutionFailedEvent': StartChildWorkflowExecutionFailedEvent,
    'startChildWorkflowExecutionInitiatedEvent': StartChildWorkflowExecutionInitiatedEvent,
    'startLambdaFunctionFailedEvent': StartLambdaFunctionFailedEvent,
    'startTimerFailedEvent': StartTimerFailedEvent,
    'timerCanceledEvent': TimerCanceledEvent,
    'timerFiredEvent': TimerFiredEvent,
    'timerStartedEvent': TimerStartedEvent,
    'workflowExecutionCancelRequestedEvent': WorkflowExecutionCancelRequestedEvent,
    'workflowExecutionCanceledEvent': WorkflowExecutionCanceledEvent,
    'workflowExecutionCompletedEvent': WorkflowExecutionCompletedEvent,
    'workflowExecutionContinuedAsNewEvent': WorkflowExecutionContinuedAsNewEvent,
    'workflowExecutionFailedEvent': WorkflowExecutionFailedEvent,
    'workflowExecutionSignaledEvent': WorkflowExecutionSignaledEvent,
    'workflowExecutionStartedEvent': WorkflowExecutionStartedEvent,
    'workflowExecutionTerminatedEvent': WorkflowExecutionTerminatedEvent,
    'workflowExecutionTimedOutEvent': WorkflowExecutionTimedOutEvent,
}