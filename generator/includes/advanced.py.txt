from urllib.parse import quote
import re
import json

def advanced_add_pandastable(self, df, hide_fields, action_buttons):
    cols_to_show = []
    show_actions = False

    if action_buttons is None:
        action_buttons = []

    if len(__get_action_buttons_to_add(action_buttons)) > 0:
        show_actions = True

    for col in df.columns:
        if col not in hide_fields:
            cols_to_show.append(col)

    # Pandas dataframe to html
    html = '''<div class="p-8">'''

    html += '''<div class="relative overflow-x-auto shadow-md sm:rounded-lg">'''

    html += '''<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">'''

    # Pandas DataFrame columns to 
    html += '''<thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">'''

    html += "<tr>"

    # Get df index name
    if df.index.name is not None:
        html += '''<th scope="col" class="px-6 py-3">''' + df.index.name +  "</th>"

    if show_actions:
        html += '''<th scope="col" class="px-6 py-3">Actions</th>'''

    for column in df.columns:
        if column in cols_to_show:
            html += '''<th scope="col" class="px-6 py-3">''' + column + "</th>"

    html += "</tr>"

    html += "</thead>"

    # Pandas DataFrame rows to html
    html += "<tbody>"
    i = 0
    for index, row in df.iterrows():
        record = row.to_dict()

        if i % 2 == 0:
            html += '''<tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">'''
        else:
            html += '''<tr class="bg-gray-50 border-b dark:bg-gray-800 dark:border-gray-700">'''

        if show_actions:
            html += '''<td class="px-6 py-4">'''
        
            action_buttons_to_add = __get_action_buttons_to_add(action_buttons)
            
            for button_to_add in action_buttons_to_add:
                hydrated_label = button_to_add.label.format(**record)
                hydrated_url = button_to_add.url.format(**record)

                if button_to_add.open_in_new_window:
                    html += """<a href='""" + hydrated_url + """' target="_blank" class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap mr-1">""" + hydrated_label + """</button>"""
                else:
                    html += """<a href='""" + hydrated_url + """' class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap mr-1">""" + hydrated_label + """</button>"""


            html += '''</td>'''

        for column in df.columns:
            key = column
            if column in cols_to_show:
                action_button = __find_key_in_action_buttons(key, action_buttons)

                value = __format_python_object_for_json(record[key])

                if action_button is not None:
                    hydrated_label = action_button.label.format(**record)
                    hydrated_url = action_button.url.format(**record)
                    if action_button.open_in_new_window:
                        html += """<td class="px-6 py-4"><a href='""" + hydrated_url + """' target="_blank" class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap">""" + hydrated_label + """</button></td>"""
                    else:
                        html += """<td class="px-6 py-4"><a href='""" + hydrated_url + """' class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap">""" + hydrated_label + """</button></td>"""
                else:
                    html += '''<td class="px-6 py-4">''' + format_input(row[column]) + "</td>"

        html += "</tr>"
        i += 1

    html += "</tbody>"

    html += "</table>"

    html += "</div>"

    html += "</div>"

    self.components.append(HtmlComponent(html))
    return self


"""
A function that formats input into a human-readable string:
Input: An arbitrary type that could be string, integer, floating point, a numpy object, a pandas datetime, or something else
Output: String

Dates should be formatted using ISO-8601. Numbers below 10 should include 2 decimal places. Numbers between 10 and 100 should have 1 decimal place. Numbers between 100 and 1000 should have 0 decimal places. Numbers between 1000 and 1000000 should have 0 decimal places and be formatted with a comma for the thousands separator. Numbers between 1000000 and 1000000000 should be formatted as X.Y million. Numbers above 1000000000 should be formatted as X.Y billion
"""


def format_input(input):
    is_int = "int" in type(input).__name__
    is_float = "float" in type(input).__name__

    if is_float or is_int:
        if input < 10:
            if is_float:
                return '{:.2f}'.format(input)
            else:
                return string_format_with_more(str(input), 10)
        elif input < 100:
            if is_float:
                return '{:.1f}'.format(input)
            else:
                return string_format_with_more(str(input), 10)
        elif input < 1000:
            return '{:.0f}'.format(input)
        elif input < 1000000:
            return '{:,.0f}'.format(input)
        elif input < 1000000000:
            return '{:.1f} million'.format(input / 1000000)
        # Check if it's nan
        elif input != input:
            return "N/A"
        else:
            return '{:.1f} billion'.format(input / 1000000000)
    elif callable(getattr(input, "isoformat", None)):
        iso = input.isoformat()

        if "T00:00:00" in iso:
            return iso[0:10]

        return iso
    else:
        formatted_string = str(input)
        return string_format_with_more(formatted_string, 100)

def string_format_with_more(text: str, max_length: int) -> str:
    if len(text) > max_length:
        return text[0:max_length] + f'... <button data-text-full="{text}" data-text-truncated="{text[0:max_length]}..." onclick="toggleMore(this)" class="text-blue-500">more</button>'
    else:
        return text

def __format_python_object_for_json(t):
    if callable(getattr(t, "isoformat", None)):
        iso = t.isoformat()

        if "T00:00:00" in iso:
            return iso[0:10]

        return iso
    
    return t

def advanced_add_emgithub(self, url):
    quoted_url = quote(url)

    emgithub = '''
    <script src="https://emgithub.com/embed-v2.js?target=''' + quoted_url +  '''&style=vs2015&type=code&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on&fetchFromJsDelivr=on"></script>
    '''

    self.components.append(HtmlComponent(emgithub))

def __format_column_header(x: str) -> str:
    # Insert undersore between camel case
    x = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', x)

    # Capitalize the beginning of each word
    x = x.title()

    # Replace underscores with spaces
    x = x.replace('_', ' ')

    return x

def __get_action_buttons_to_add(action_buttons):
    action_buttons_to_add = []

    for action_button in action_buttons:
        # If the label is not of the form "{key}", then add it to the list of action buttons to add
        if action_button.label[0] != '{' or action_button.label[-1] != '}' and '{' not in action_button.label[1:-1]:        
            action_buttons_to_add.append(action_button)

    return action_buttons_to_add

def __find_key_in_action_buttons(key: str, action_buttons):
    for action_button in action_buttons:
        if action_button.label == '{' + key + '}' :
            return action_button

    return None

def __replace_text_with_button(record: dict, action_buttons) -> dict:
    new_record = {}

    for key in record.keys():
        action_button = __find_key_in_action_buttons(key, action_buttons)

        value = __format_python_object_for_json(record[key])

        if action_button is not None:
            hydrated_label = action_button.label.format(**record)
            hydrated_url = action_button.url.format(**record)
            if action_button.open_in_new_window:
                new_record[key] = """<a href='""" + hydrated_url + """' target="_blank" class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap mr-1">""" + hydrated_label + """</button>"""
            else:
                new_record[key] = """<a href='""" + hydrated_url + """' class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap mr-1">""" + hydrated_label + """</button>"""
        else:
            new_record[key] = value
    
    action_buttons_html = ''

    action_buttons_to_add = __get_action_buttons_to_add(action_buttons)
    for button_to_add in action_buttons_to_add:
        hydrated_label = button_to_add.label.format(**record)
        hydrated_url = button_to_add.url.format(**record)

        if button_to_add.open_in_new_window:
            action_buttons_html += """<a href='""" + hydrated_url + """' target="_blank" class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap">""" + hydrated_label + """</button>"""
        else:
            action_buttons_html += """<a href='""" + hydrated_url + """' class="px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 whitespace-nowrap">""" + hydrated_label + """</button>"""

    new_record['Actions'] = action_buttons_html

    return new_record

def advanced_add_datagrid(page, dataframe, action_buttons):
    if action_buttons is None:
        action_buttons = []

    cols = list(map(lambda x: {'headerName': __format_column_header(x), 'field': x} , dataframe.columns.to_list()))

    if len(__get_action_buttons_to_add(action_buttons)) > 0:
        cols.append({'headerName': 'Actions', 'field': 'Actions'})

    datagridHtml = '''
        <script>
        var columnDefsasdf = {columns};
        '''.format(columns = cols)

    records = list (map(lambda x: __replace_text_with_button(x, action_buttons=action_buttons), dataframe.to_dict(orient='records')))

    datagridHtml += '''
    columnDefsasdf.forEach( (x) => { x.cellRenderer = function(params) { return params.value ? params.value : '' } } )
    '''

    datagridHtml += '''
        var rowDataasdf = {records};
        '''.format(records = json.dumps( records ) )

    datagridHtml += '''
        var gridOptionsasdf = {
            columnDefs: columnDefsasdf,
            rowData: rowDataasdf,
            defaultColDef: {
                sortable: true,
                filter: true,
                resizable: true,
                floatingFilter: true,
                autoHeight: true,
                wrapText: true,
                autoSizePadding: 10,
                cellStyle: {
                    'white-space': 'normal'
                },
            },
            pagination: true
        };
        document.addEventListener('DOMContentLoaded', function() {
            var gridDivasdf = document.querySelector('#divid_aggrid_asdf');
            new agGrid.Grid(gridDivasdf, gridOptionsasdf);
        });

        function expand(e) {
            e.parentElement.children[1].style.height = 'calc( 100vh )';
            e.scrollIntoView();
        }
        </script>
        <div>
            <button onclick="expand(this)" class="mb-4 px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Expand</button>
            <div id="divid_aggrid_asdf" style="height: 500px; max-height: calc( 100vh - 60px ); " class="data-grid ag-theme-alpine-dark "></div>
        </div>
    '''

    page.components.append(HtmlComponent(datagridHtml))

