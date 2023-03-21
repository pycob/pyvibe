import pyvibe as pv
import os
import json
import pandas as pd
from .common.components import navbar, footer, marketing_banner

def argument_value_with_quotes(argument_type, argument_value) -> str:
    if argument_value is None:
        return 'None'

    if argument_type == 'Untyped':
        return argument_value

    if isinstance(argument_value, str):
        return "\'" + argument_value.replace("'", "") + "\'"

    return str(argument_value)

def get_argument_type(name, arguments) -> str:
    for arg in arguments:
        if name == arg['name']:
            return arg['type']

    return None

def example_to_arguments(example, arguments) -> str:
    # print(example)
    if example is None:
        return ''

    return ', '.join(map(lambda x: x['argumentName'] + ' = ' + argument_value_with_quotes( get_argument_type(x['argumentName'], arguments) , x['argumentValue']), example))

def example_to_pyvibe_code(element_type, example, attachableTo, arguments) -> str:
    return attachableTo + '.add_' + element_type + '(' + example_to_arguments(example, arguments) + ')'


# Read spec.json into a dictionary
with open(os.path.join("./spec/", 'spec.json')) as f:
    spec = json.load(f)

page = pv.Page('Component Reference', navbar=navbar, footer=footer)

category_order = [
    'Basic HTML',
    'Layout',
    'Form',
    'Table',
    'Advanced',
    'Internal',
]

categories = {}

# sidebar = page.add_sidebar()

for element in spec:
    category = element['category']

    if category not in categories:
        categories[category] = []
    
    categories[category].append(element)

for category in category_order:
    page.add_section(category, category)
    # sidebar_category = sidebar.add_sidebarcategory(category)
    page.add_header(category, 5)

    for element in categories[category]:
        page.add_section(element['elementType'], element['name'], level=2)
        # sidebar_category.add_sidebarlink(element['name'], "#"+element['name'])
        if element['elementType'] != 'page':
            page.add_header(element['name'] + f" (<code>.add_{element['elementType']}</code>)", 4)
        else:
            page.add_header(element['name'], 4)
        page.add_text(element['description'])

        if 'attachableTo' in element:
            page.add_header("Use With", 3)

        for attachableTo in element['attachableTo']:
            page.add_link(attachableTo, "#"+attachableTo)

        page.add_text("")
        page.add_header('Input', 2)

        table = pv.RawtableComponent()

        tablehead = pv.TableheadComponent()
        tablehead.add_tablecellheader("Name")
        tablehead.add_tablecellheader("Type")
        tablehead.add_tablecellheader("Default Value")
        tablehead.add_tablecellheader("Description")

        table.add_component(tablehead)

        tablebody = pv.TablebodyComponent()

        for argument in element['arguments']:
            row = pv.TablerowComponent()

            row.add_tablecellheader(argument['name'])
            row.add_tablecell(argument['type'])
            if 'defaultValue' in argument:
                if argument['type'] == "String":
                    row.add_tablecell("'" + argument['defaultValue'] + "'")
                else:
                    row.add_tablecell(argument['defaultValue'])
            else:
                row.add_tablecell("")
            row.add_tablecell(argument['description'])

            tablebody.add_component(row)

        table.add_component(tablebody)

        if len(element['arguments']) > 0:
            page.add_component(table)
        else:
            page.add_text("No Inputs")
        # for argument in element['arguments']:
        #     if 'defaultValue' in argument:
        #         page.add_html('<p><code>' + argument['name'] +'</code>: <b>' + argument['type'] + '</b>. Default: ' + argument['defaultValue'] + '. ' + argument['description'] + ' </p>')
        #     else:
        #         page.add_html('<p><code>' + argument['name'] +'</code>: <b>' + argument['type'] + '</b>. ' + argument['description'] + ' </p>')

        if element['category'] != 'Internal':
            page.add_header('Example', 2)

            for exampleWithSetup in element['exampleCode']:
                example = exampleWithSetup['arguments']

                if 'card' in element['attachableTo']:
                    page.add_code(example_to_pyvibe_code(element['elementType'], example, attachableTo, element['arguments']).replace('<', '&lt;').replace('>', '&gt;'))
                    card = pv.CardComponent()
                    if callable(getattr(card, "add_"+ element['elementType'], None)):
                        setup = ""

                        if 'setup' in exampleWithSetup:
                            setup = '\n'.join(exampleWithSetup['setup']) + '\n'                   
                        
                        expression = setup + 'card.add_' + element['elementType'] + '(' + example_to_arguments(example, element['arguments']) + ')'
                        
                        print("Executing = ", expression)
                        try:
                            exec(expression)
                        except Exception as err:
                            print("Error = ", err)
                        
                        page.add_component(card)
                elif 'page' in element['attachableTo']:
                    page.add_code(example_to_pyvibe_code(element['elementType'], example, attachableTo, element['arguments']).replace('<', '&lt;').replace('>', '&gt;'))
                    if callable(getattr(page, "add_"+ element['elementType'], None)):
                        eval('page.add_' + element['elementType'] + '(' + example_to_arguments(example, element['arguments']) + ')')
                elif 'form' in element['attachableTo']:
                    card = pv.CardComponent()

                    form = pv.FormComponent(action="")

                    page.add_code(example_to_pyvibe_code(element['elementType'], example, attachableTo, element['arguments']).replace('<', '&lt;').replace('>', '&gt;'))
                    if callable(getattr(form, "add_"+ element['elementType'], None)):
                        eval('form.add_' + element['elementType'] + '(' + example_to_arguments(example, element['arguments']) + ')')

                    card.add_component(form)

                    page.add_component(card)

        page.add_divider()

page.add_html(marketing_banner)