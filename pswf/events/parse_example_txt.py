import re
from textwrap import dedent
from pprint import pprint

event_type_pat = re.compile(r"^            '(.*)Attributes': {$")
attr_name_pat = re.compile(r"^                '(.*)': .*,")
end_event_pat = re.compile(r"^            },$")

events = dict()


def chars_in(s):
    prior = None
    for c in s:
        yield prior, c
        prior = c

def aws_to_py_name(aw_name):
    '''newExecutionRunId -> new_execution_run_id'''
    def _py_name_chars():
        for c in aw_name:
            if c == c.upper():
                yield '_' + c.lower()
            else:
                yield c
    return ''.join(_py_name_chars())


summaries = dict()
with open('event-types.txt', 'rt') as fh:
    for i, line in enumerate(fh.readlines()):
        if i > 1 and len(line.strip()) > 0:
            parts = line.split(" - ")
            if len(parts) == 2:
                summaries[parts[0].strip()] = parts[1].strip()

with open("example_events.txt", 'rt') as fh:
    aws_event_name = None
    for line in fh.readlines():

        # Parse event type
        m = event_type_pat.match(line)
        if m:
            aws_event_name = m.group(1)
            event_cls = aws_event_name[0].upper() + aws_event_name[1:]

            events[aws_event_name] = {
                'event_cls': event_cls,
                'attrs': list(),
                'constants': set(),
                'example': list(),
                'aws_event_name': aws_event_name,
            }

        # Parse attr name
        m = attr_name_pat.match(line)
        if m:
            events[aws_event_name]['attrs'].append({
                'aws_attr_name': m.group(1),
                'py_attr_name': aws_to_py_name(m.group(1))
            })

        # Collect example lines
        if aws_event_name is not None:
            events[aws_event_name]['example'].append(line.rstrip())

        # Find constants
        if aws_event_name is not None:
            parts = line.replace(",", '').replace("'", '').split()
            for part in parts:
                if '|' in part:
                    for cons in part.split("|"):
                        events[aws_event_name]['constants'].add(cons)

        # Detect end of the event
        m = end_event_pat.match(line)
        if m:
            aws_event_name = None



def indent(txt, spaces=4):
    def _indented_lines():
        for line in dedent(txt).split("\n"):
            yield ' '*spaces + line
    return "\n".join(_indented_lines())



def format_attribute(py_name, aws_name):
    return dedent("""\
        @property
        def {py_name}(self):
            return self._get_data_attr('{aws_name}')
        """.format(py_name=py_name, aws_name=aws_name))


all_events_imports = list()
all_events_dict = list()


for event in events.values():
    filename = "{clsname}.py".format(clsname=event['event_cls'])
    print(filename)

    src = list()

    try:
        event_name = event['event_cls'][:-5]
        summary = summaries[event_name]
    except KeyError:
        summary = "%s event" % (event['event_cls'])

    with open(filename, 'wt') as fh:

        fh.write(dedent("""\
            from .SWFEvent import SWFEvent
    
            class {clsname}(SWFEvent):
                '''
                {summary}
                
            {example}
                '''
                
            {constants}
                
            {attributes}
            """).format(
                clsname = event['event_cls'],
                summary = summary,
                example = indent("\n".join(event['example'])),
                constants = indent("\n".join(["{name} = '{name}'".format(name=name) for name in sorted(event['constants'])])),
                attributes = indent("\n".join([format_attribute(a['py_attr_name'], a['aws_attr_name']) for a in event['attrs']]))
            ))

    all_events_imports.append("from .{module} import {module}".format(module=event['event_cls']))
    all_events_dict.append("    '{aws_name}': {cls_name},".format(
        aws_name = event['aws_event_name'],
        cls_name = event['event_cls'],
    ))


with open('all_events.py', 'wt') as fh:
    fh.write("\n".join(sorted(all_events_imports)))
    fh.write("\n")
    fh.write("\n")
    fh.write("SWF_EVENT_CLASSES = {\n")
    for line in sorted(all_events_dict):
        fh.write(line + "\n")
    fh.write("}")

