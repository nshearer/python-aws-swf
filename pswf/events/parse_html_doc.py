import os, sys
import re
from textwrap import dedent, wrap
from pprint import pprint

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


def abort(msg):
    print("ERROR: " + msg)
    sys.exit(2)


def get_help_page():
    if not os.path.exists('swf.html'):
        r = requests.get('https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html')
        with open('swf.html', 'wb') as fh:
            fh.write(r.content)
    with open('swf.html', 'rb') as fh:
        return fh.read()


def get_element_text(o):
    if o.__class__ == NavigableString:
        return str(o)
    return o.get_text()


def children_of(o, tag=None):
    try:
        for child in o.children:
            if tag is None or (child.__class__ is Tag and child.name.lower() == tag.lower()):
                yield child
    except AttributeError:
        return


def first_child(o, tag=None):
    for child in children_of(o):
        if tag is None or (child.__class__ is Tag and child.name.lower() == tag.lower()):
            return child


def find_element_with_text(element, text, tag=None, immediate_only=False):
    '''
    Find an element with the given text

    There's probably a bs4 way to do this, but this is working for me

    :param element: Element to start searching from
    :param text: Text to look for
    :param tag: If true, find a tag element with this name
    :param immediate_only: If true, only dearch direct children (don't recurse)
    '''

    # Search children
    for e in children_of(element):
        if e.__class__ is Tag:

            # Is this element a match
            if tag is None or e.name == tag:
                if text in get_element_text(e):

                    # Found
                    if immediate_only:
                        return e

                    # See if the text is in a sub element
                    grandchild = find_element_with_text(e, text, tag)
                    if grandchild is not None:
                        return grandchild
                    else:
                        return e

            # Is there a sub-element that could be a match?
            if text in get_element_text(e):
                grandchild = find_element_with_text(e, text, tag)
                if grandchild is not None:
                        return grandchild


def next_tag(o, tag = None):
    next = o.next_sibling
    while next.__class__ is not Tag or (tag is not None and next.name != tag):
        next = next.next_sibling
    return next


def parse_help_path(help_page):

    # Parse HTML
    soup = BeautifulSoup(help_page, "html.parser")

    # Find "poll_for_decision_task(**kwargs)" section
    section =  soup.find(id='SWF.Client.poll_for_decision_task')

    # Select dt that goes with the dd
    while section.name != 'dd':
        section = section.next_sibling

#    if section is None:
#        abort("Failed to find section for poll_for_decision by id #SWF.Client.get_workflow_execution_historyw")

    return section


def sumerize_content(o):
    lines = wrap(get_element_text(o))
    if len(lines) > 1:
        return lines[0] + '...'
    try:
        return lines[0]
    except IndexError:
        return ''


def sumerize_object(o):
    if o.__class__ is NavigableString:
        return 'T: ' + sumerize_content(o)

    return '{type} "{tag}": {contents}'.format(
        type=type(o).__name__,
        tag=o.name,
        contents = sumerize_content(o).rstrip())


def print_element_tree(o, levels=1, indent = 0):

    print(' '*indent + sumerize_object(o))

    if levels > 1:

        for child in children_of(o):
            print_element_tree(child, levels-1, indent + 4)


def indent(txt, spaces=4):
    if txt is None:
        return ''
    def _indented_lines():
        for line in dedent(txt).split("\n"):
            yield ' '*spaces + line
    return "\n".join(_indented_lines())


def aws_to_py_name(aw_name):
    '''newExecutionRunId -> new_execution_run_id'''
    def _py_name_chars():
        for c in aw_name:
            if c == c.upper():
                yield '_' + c.lower()
            else:
                yield c
    return ''.join(_py_name_chars())


def parse_examples_txt(examples):
    '''See scrape/5.example.txt'''

    in_events = False
    common_attrs = list()
    event_type = None

    attr_pat = re.compile("^            '(\w+)': (.*),?:?$")

    event_types = dict()
    for line in examples.split("\n"):
        if not in_events:
            if line == "    'events': [":
                in_events = True
        else:
            m = attr_pat.match(line)
            if m:

                attr_name = m.group(1)
                attr_value = m.group(2)

                if attr_name.endswith('EventAttributes'):
                    event_type = attr_name[:-15]
                    event_types[event_type] = list()

            if event_type is not None:
                event_types[event_type].append(line)

            if line == '            },':
                event_type = None


    for event_type in event_types:
        event_types[event_type] = dedent("\n".join(event_types[event_type]))

    return event_types


if __name__ == '__main__':
    help_page = get_help_page()

    # Explore to "poll_for_decision" section of help page and find events list

    poll_for_decision_section = parse_help_path(help_page)
    with open('scrape/0.poll_for_decision_section.html', 'wt') as fh:
        fh.write(str(poll_for_decision_section))

    response_structure_header = find_element_with_text(poll_for_decision_section, 'Response Structure', tag='p')
    response_structure = next_tag(response_structure_header, tag='ul')
    with open('scrape/1.response_structure.html', 'wt') as fh:
        fh.write(str(response_structure))

    # Example structure
    example_div = find_element_with_text(poll_for_decision_section, 'taskToken', tag='pre')
    with open('scrape/5.example.html', 'wt') as fh:
        fh.write(str(example_div))

    example_txt = get_element_text(example_div)
    with open('scrape/5.example.txt', 'wt') as fh:
        fh.write(str(example_txt))

    examples = parse_examples_txt(example_txt)


    # 1) Create a list of the types of events that can be in the history

    events_attribute = find_element_with_text(response_structure, "A history event can be one of these types", tag='ul')
    with open('scrape/2.events_attribute.html', 'wt') as fh:
        fh.write(str(events_attribute))

    events_list_ul = find_element_with_text(events_attribute, "decision was received by the system", tag="ul")
    with open('scrape/3.events_list_ul.html', 'wt') as fh:
        fh.write(str(events_list_ul))

    events = dict()
    for event_type_li in children_of(events_list_ul, tag='li'):

        # Event type is in tt
        try:
            aws_event_name = get_element_text(first_child(event_type_li, 'tt')).strip()
        except Exception as e:
            raise Exception("Failed to find tt under li for event type: %s\n%s" % (str(e), str(event_type_li)))

        # Description after special - character (split char is a unicode char)
        summary = '-'.join(get_element_text(event_type_li).split('–')[1:]).strip()

        events[aws_event_name] = {
            'event_cls': aws_event_name[0].upper() + aws_event_name[1:] + 'Event', # cap first letter
            'summary': summary,
            'attrs': list(),
            'constants': set(),
            'example': None,
            'aws_event_name': aws_event_name[0].lower() + aws_event_name[1:], # cap first letter
        }

        try:
            events[aws_event_name]['example'] = examples[events[aws_event_name]['aws_event_name']]
        except KeyError:
            pass

        # Attributes for the event type under a li
        event_type_attrs_heading = events[aws_event_name]['aws_event_name'] + 'EventAttributes'
        event_type_attrs_detail = find_element_with_text(response_structure, event_type_attrs_heading, tag='li')
        with open('scrape/4.%s.event_type_attrs_detail.html' % (aws_event_name), 'wt') as fh:
            fh.write(str(event_type_attrs_detail))

        # Event type attributes are under li
        event_type_attrs_ul = first_child(event_type_attrs_detail, tag='ul')
        for event_type_attr_li in children_of(event_type_attrs_ul, tag='li'):

            # Name of attribute
            attr_name_pat = re.compile(r'^([a-zA-Z]+)\s+\((.*)\) --$') # scheduledEventId (integer) --
            attr_name_p = first_child(event_type_attr_li, tag='p')
            m = attr_name_pat.match(get_element_text(attr_name_p))
            if not m:
                raise Exception("Failed to parse event type %s attribute name:\n%s" % (aws_event_name, str(attr_name_p)))

            attr_name = m.group(1)
            attr_type = m.group(2)

            # Detail are all the other elements besides the first
            attr_detail = list()
            for i, child in enumerate(filter(lambda t: t.__class__ is Tag, children_of(event_type_attr_li))):
                if i > 0:
                    attr_detail.append(get_element_text(child))

            events[aws_event_name]['attrs'].append({
                'name': attr_name,
                'type': attr_type,
                'detail': "\n".join(attr_detail),
            })


        #
        # all_events_imports = list()
        # all_events_dict = list()

        # Write out event class
        event = events[aws_event_name]
        filename = "{clsname}.py".format(clsname=event['event_cls'])
        print(filename)

        src = list()

        try:
            event_name = event['event_cls'][:-5]
        except KeyError:
            summary = "%s event" % (event['event_cls'])

        with open(filename, 'wt', encoding='utf-8') as fh:

            cls_format = dedent("""\
                # coding=utf-8
                from .SWFEvent import SWFEvent
        
                class {clsname}(SWFEvent):
                    '''
                    {summary}
                    
                {example}
                    '''
                    
                {constants}
                    
                {attributes}
                """)

            def format_attribute(attr):
                return dedent("""\
                    @property
                    def {py_name}(self):
                        '''
                    {detail}
                        
                        :return {type}:
                        '''
                        return self._get_{type}_data_attr('{aws_name}')
                        
                        """).format(
                            py_name=aws_to_py_name(attr['name']),
                            aws_name=attr['name'],
                            type=attr['type'],
                            detail = indent(attr['detail'], 4).rstrip(),
                            )


            fh.write(cls_format.format(
                clsname = event['event_cls'],
                summary = event['summary'],
                example = indent(event['example']),
                constants = indent("\n".join(["{name} = '{name}'".format(name=name) for name in sorted(event['constants'])])),
                attributes = indent("\n".join([format_attribute(a) for a in event['attrs']]))
                ))

        # all_events_imports.append("from .{module} import {module}".format(module=event['event_cls']))
        # all_events_dict.append("    '{aws_name}': {cls_name},".format(
        #     aws_name = event['aws_event_name'],
        #     cls_name = event['event_cls'],
        # ))


    # Explore
    #print_element_tree(events_list_ul, levels=2)
