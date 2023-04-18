from __future__ import annotations
from .component_interface import *
import uuid



class AlertComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_alert` method of the parent component.
  """
  def __init__(self, text: str, badge: str = '', color: str = 'indigo'):    
    self.text = text
    self.badge = badge
    self.color = color
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="text-center py-4 lg:px-4">
<div class="p-2 bg-''' + self.color + '''-800 items-center text-''' + self.color + '''-100 leading-none lg:rounded-full flex lg:inline-flex" role="alert">
    <span class="flex rounded-full bg-''' + self.color + '''-500 uppercase px-2 py-1 text-xs font-bold mr-3">''' + self.badge + '''</span>
    <span class="font-semibold mr-2 text-left flex-auto">''' + self.text + '''</span>            
</div>
</div>'''

class CardComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_card` method of the parent component.
  """
  def __init__(self, center_content: bool = False, classes: str = '', components: list = None):    
    self.center_content = center_content
    self.classes = classes
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="block p-6 mb-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700 overflow-x-auto max-w-fit mx-auto ''' + self.classes + '''">
    <div class="flex flex-col h-full ">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </div>
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_html(self, value: str) -> HtmlComponent:
    """Renders raw HTML. This is meant to be an escape hatch for when you need to render something that isn't supported by PyVibe.

    Args:
        value (str): Raw HTML code to be rendered
    
    Returns:
        HtmlComponent: The new component
    """
    new_component = HtmlComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_text(self, value: str) -> TextComponent:
    """Renders a paragraph of text

    Args:
        value (str): Text to be rendered
    
    Returns:
        TextComponent: The new component
    """
    new_component = TextComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_link(self, text: str, url: str, classes: str = '') -> LinkComponent:
    """Renders a link

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        LinkComponent: The new component
    """
    new_component = LinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_plainlink(self, text: str, url: str, classes: str = '') -> PlainlinkComponent:
    """Renders a link without any styling

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        PlainlinkComponent: The new component
    """
    new_component = PlainlinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_list(self, show_dots: bool = True, classes: str = '', components: list = None) -> ListComponent:
    """Renders a list of items

    Args:
        show_dots (bool): Optional. Whether or not to show dots
        classes (str): Optional. Classes to be applied to the list
        components (list): Items to be rendered
    
    Returns:
        ListComponent: The new component
    """
    new_component = ListComponent(show_dots, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_image(self, url: str, alt: str, classes: str = '') -> ImageComponent:
    """Renders an image

    Args:
        url (str): URL of the image
        alt (str): Alt text for the image
        classes (str): Optional. Classes to be applied to the image
    
    Returns:
        ImageComponent: The new component
    """
    new_component = ImageComponent(url, alt, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_header(self, text: str, size: int = 5, classes: str = '') -> HeaderComponent:
    """Renders a header

    Args:
        text (str): Text to be rendered
        size (int): Optional. Size of the header. Choose 1-9
        classes (str): Optional. Classes to be applied to the header
    
    Returns:
        HeaderComponent: The new component
    """
    new_component = HeaderComponent(text, size, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_card(self, center_content: bool = False, classes: str = '', components: list = None) -> CardComponent:
    """Renders a card

    Args:
        center_content (bool): Optional. Whether the card contents should be centered
        classes (str): Optional. Classes to be applied to the card
        components (list): Components to be rendered inside the card
    
    Returns:
        CardComponent: The new component
    """
    new_component = CardComponent(center_content, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_container(self, grid_columns: int = None, classes: str = '', components: list = None) -> ContainerComponent:
    """Renders a container to help with layout

    Args:
        grid_columns (int): Optional. Number of columns (if any) to use. 1-12
        classes (str): Optional. Classes to be applied to the container
        components (list): Components to be rendered inside the container
    
    Returns:
        ContainerComponent: The new component
    """
    new_component = ContainerComponent(grid_columns, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_alert(self, text: str, badge: str = '', color: str = 'indigo') -> AlertComponent:
    """Renders an alert

    Args:
        text (str): Text to be rendered
        badge (str): Optional. Text to be rendered inside the badge
        color (str): Optional. Color of the. Choose 'indigo', 'orange', or 'red'
    
    Returns:
        AlertComponent: The new component
    """
    new_component = AlertComponent(text, badge, color)    
    self.components.append(new_component)
    return new_component
    

  def add_code(self, value: str, header: str = '', prefix: str = '>>>') -> CodeComponent:
    """Renders a block of code

    Args:
        value (str): Code to be rendered
        header (str): Optional. Header to be rendered above the code block
        prefix (str): Optional. Prefix to be rendered before the code block
    
    Returns:
        CodeComponent: The new component
    """
    new_component = CodeComponent(value, header, prefix)    
    self.components.append(new_component)
    return new_component
    

  def add_divider(self) -> DividerComponent:
    """Renders a divider

    
    
    Returns:
        DividerComponent: The new component
    """
    new_component = DividerComponent()    
    self.components.append(new_component)
    return new_component
    

  def add_form(self, action: str = '?', method: str = 'GET', components: list = None) -> FormComponent:
    """Renders a form

    Args:
        action (str): Optional. Action for the form. This is the page that the form will submit to. Defaults to the current page
        method (str): Optional. Method for the form (i.e. GET, POST)
        components (list): List of Component of the form
    
    Returns:
        FormComponent: The new component
    """
    new_component = FormComponent(action, method, components)    
    self.components.append(new_component)
    return new_component
    

  def add_formtext(self, label: str, name: str, placeholder: str = '', value: str = '') -> FormtextComponent:
    """Renders a form

    Args:
        label (str): Label for the form text
        name (str): Name for the form text
        placeholder (str): Optional. Placeholder
        value (str): Optional. Value if you want to pre-populate
    
    Returns:
        FormtextComponent: The new component
    """
    new_component = FormtextComponent(label, name, placeholder, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formemail(self, label: str = 'Your E-mail', name: str = 'email', placeholder: str = 'user@example.com') -> FormemailComponent:
    """Renders a form email

    Args:
        label (str): Optional. Label for the form email
        name (str): Optional. Name for the form email
        placeholder (str): Optional. Placeholder
    
    Returns:
        FormemailComponent: The new component
    """
    new_component = FormemailComponent(label, name, placeholder)    
    self.components.append(new_component)
    return new_component
    

  def add_formpassword(self, label: str = 'Password', name: str = 'password', placeholder: str = 'password') -> FormpasswordComponent:
    """Renders a form password

    Args:
        label (str): Optional. Label for the form password
        name (str): Optional. Name for the form password
        placeholder (str): Optional. Placeholder
    
    Returns:
        FormpasswordComponent: The new component
    """
    new_component = FormpasswordComponent(label, name, placeholder)    
    self.components.append(new_component)
    return new_component
    

  def add_formselect(self, label: str, name: str, options, value: str = '') -> FormselectComponent:
    """Renders a form select

    Args:
        label (str): Label for the form select
        name (str): Name for the form select
        options: Options for the form select
        value (str): Optional. Selected value
    
    Returns:
        FormselectComponent: The new component
    """
    new_component = FormselectComponent(label, name, options, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formtextarea(self, label: str = 'Your Message', name: str = 'message', placeholder: str = 'Leave a comment...', value: str = '') -> FormtextareaComponent:
    """Renders a text area

    Args:
        label (str): Optional. Label for the text area
        name (str): Optional. Name for the text area
        placeholder (str): Optional. Placeholder
        value (str): Optional. Value if you want to pre-populate
    
    Returns:
        FormtextareaComponent: The new component
    """
    new_component = FormtextareaComponent(label, name, placeholder, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formsubmit(self, label: str = 'Submit') -> FormsubmitComponent:
    """Renders a form submit button

    Args:
        label (str): Optional. Label for the form submit button
    
    Returns:
        FormsubmitComponent: The new component
    """
    new_component = FormsubmitComponent(label)    
    self.components.append(new_component)
    return new_component
    

  def add_rawtable(self, components: list = None) -> RawtableComponent:
    """Renders a table manually by constructing the table header, body, content, etc.. This is useful if you want to customize the table more than what the other table functions allow. Most of the time you'll use the other table functions instead of this one.

    Args:
        components (list): Components to render in the table
    
    Returns:
        RawtableComponent: The new component
    """
    new_component = RawtableComponent(components)    
    self.components.append(new_component)
    return new_component
    


  def add_pandastable(self, dataframe, hide_fields: list = [], action_buttons: list = None):
    """Renders a pandas table

    Args:
        dataframe: Dataframe to render
        hide_fields (list): List of fields to hide
        action_buttons (list): Row actions to render
    
    Returns:
        PandastableComponent: The new component
    """
    advanced_add_pandastable(self, dataframe, hide_fields, action_buttons)
    return self
    

  def add_plotlyfigure(self, fig, id: str = '') -> PlotlyfigureComponent:
    """Renders a plotly figure

    Args:
        fig: Figure to render
        id (str): Optional. Unique ID for this element. Will default to a UUID.
    
    Returns:
        PlotlyfigureComponent: The new component
    """
    new_component = PlotlyfigureComponent(fig, id)    
    self.components.append(new_component)
    return new_component
    


  def add_datagrid(self, dataframe, action_buttons: list = None):
    """Renders a data grid

    Args:
        dataframe: Dataframe to render
        action_buttons (list): Row actions to render
    
    Returns:
        DatagridComponent: The new component
    """
    advanced_add_datagrid(self, dataframe, action_buttons)
    return self
    


  def add_emgithub(self, url: str):
    """Renders a block of code from a github URL

    Args:
        url (str): URL of the GitHub file to be rendered
    
    Returns:
        EmgithubComponent: The new component
    """
    advanced_add_emgithub(self, url)
    return self
    

  def add_scriptstatus(self, job_id: str, redirect_url: str) -> ScriptstatusComponent:
    """Shows the status of a script execution and redirects to a new page when complete

    Args:
        job_id (str): Job id to check the status of
        redirect_url (str): URL to redirect to when the script is complete
    
    Returns:
        ScriptstatusComponent: The new component
    """
    new_component = ScriptstatusComponent(job_id, redirect_url)    
    self.components.append(new_component)
    return new_component
    

class CodeComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_code` method of the parent component.
  """
  def __init__(self, value: str, header: str = '', prefix: str = '>>>'):    
    self.value = value
    self.header = header
    self.prefix = prefix
    # Replace < and > in prefix:
    self.prefix = self.prefix.replace("<", "&lt;").replace(">", "&gt;")

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="mx-auto my-10 max-w-3xl">
    <div class="flex h-11 w-full items-center justify-start space-x-1.5 rounded-t-lg bg-gray-900 px-3">
        <span class="h-3 w-3 rounded-full bg-red-400"></span>
        <span class="h-3 w-3 rounded-full bg-yellow-400"></span>
        <span class="h-3 w-3 rounded-full bg-green-400"></span>
        <code class="pl-5 text-lime-500">''' + self.header + '''</code>
    </div>
    <div class="w-full border-t-0 bg-gray-700 pb-5 rounded-b-lg whitespace-nowrap overflow-x-auto p-2">
        <code class="text-gray-500">''' + self.prefix + '''</code>
        <code class="text-white" style="white-space: break-spaces">''' + self.value + '''</code>
    </div>
</div>'''

class CodeeditorComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_codeeditor` method of the parent component.
  """
  def __init__(self, value: str, language: str = 'python'):    
    self.value = value
    self.language = language
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<style type="text/css" media="screen">
#editorContainer {
    // width: calc( 100vw - 40px );
    height: 500px;
    max-height: calc( 80vh - 60px );
    position: relative;
    background-color: red;
}
#editor { 
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}
</style>

<div id="editorContainer">
    <div id="editor">''' + self.value + '''</div> 
</div>
<script src="https://cdn.jsdelivr.net/gh/ajaxorg/ace-builds/src-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
<script>
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/''' + self.language + '''");

    // const savedCode = localStorage.getItem('code');

    // if (savedCode) {
    //     editor.setValue(savedCode);
    // }
</script>'''

class ContainerComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_container` method of the parent component.
  """
  def __init__(self, grid_columns: int = None, classes: str = '', components: list = None):    
    self.grid_columns = grid_columns
    self.classes = classes
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    if grid_columns is not None:
        self.classes += " grid gap-6 md:grid-cols-" + str(grid_columns)

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class=" ''' + self.classes + '''">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_html(self, value: str) -> HtmlComponent:
    """Renders raw HTML. This is meant to be an escape hatch for when you need to render something that isn't supported by PyVibe.

    Args:
        value (str): Raw HTML code to be rendered
    
    Returns:
        HtmlComponent: The new component
    """
    new_component = HtmlComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_text(self, value: str) -> TextComponent:
    """Renders a paragraph of text

    Args:
        value (str): Text to be rendered
    
    Returns:
        TextComponent: The new component
    """
    new_component = TextComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_link(self, text: str, url: str, classes: str = '') -> LinkComponent:
    """Renders a link

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        LinkComponent: The new component
    """
    new_component = LinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_plainlink(self, text: str, url: str, classes: str = '') -> PlainlinkComponent:
    """Renders a link without any styling

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        PlainlinkComponent: The new component
    """
    new_component = PlainlinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_list(self, show_dots: bool = True, classes: str = '', components: list = None) -> ListComponent:
    """Renders a list of items

    Args:
        show_dots (bool): Optional. Whether or not to show dots
        classes (str): Optional. Classes to be applied to the list
        components (list): Items to be rendered
    
    Returns:
        ListComponent: The new component
    """
    new_component = ListComponent(show_dots, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_image(self, url: str, alt: str, classes: str = '') -> ImageComponent:
    """Renders an image

    Args:
        url (str): URL of the image
        alt (str): Alt text for the image
        classes (str): Optional. Classes to be applied to the image
    
    Returns:
        ImageComponent: The new component
    """
    new_component = ImageComponent(url, alt, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_header(self, text: str, size: int = 5, classes: str = '') -> HeaderComponent:
    """Renders a header

    Args:
        text (str): Text to be rendered
        size (int): Optional. Size of the header. Choose 1-9
        classes (str): Optional. Classes to be applied to the header
    
    Returns:
        HeaderComponent: The new component
    """
    new_component = HeaderComponent(text, size, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_card(self, center_content: bool = False, classes: str = '', components: list = None) -> CardComponent:
    """Renders a card

    Args:
        center_content (bool): Optional. Whether the card contents should be centered
        classes (str): Optional. Classes to be applied to the card
        components (list): Components to be rendered inside the card
    
    Returns:
        CardComponent: The new component
    """
    new_component = CardComponent(center_content, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_container(self, grid_columns: int = None, classes: str = '', components: list = None) -> ContainerComponent:
    """Renders a container to help with layout

    Args:
        grid_columns (int): Optional. Number of columns (if any) to use. 1-12
        classes (str): Optional. Classes to be applied to the container
        components (list): Components to be rendered inside the container
    
    Returns:
        ContainerComponent: The new component
    """
    new_component = ContainerComponent(grid_columns, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_alert(self, text: str, badge: str = '', color: str = 'indigo') -> AlertComponent:
    """Renders an alert

    Args:
        text (str): Text to be rendered
        badge (str): Optional. Text to be rendered inside the badge
        color (str): Optional. Color of the. Choose 'indigo', 'orange', or 'red'
    
    Returns:
        AlertComponent: The new component
    """
    new_component = AlertComponent(text, badge, color)    
    self.components.append(new_component)
    return new_component
    

  def add_code(self, value: str, header: str = '', prefix: str = '>>>') -> CodeComponent:
    """Renders a block of code

    Args:
        value (str): Code to be rendered
        header (str): Optional. Header to be rendered above the code block
        prefix (str): Optional. Prefix to be rendered before the code block
    
    Returns:
        CodeComponent: The new component
    """
    new_component = CodeComponent(value, header, prefix)    
    self.components.append(new_component)
    return new_component
    

  def add_form(self, action: str = '?', method: str = 'GET', components: list = None) -> FormComponent:
    """Renders a form

    Args:
        action (str): Optional. Action for the form. This is the page that the form will submit to. Defaults to the current page
        method (str): Optional. Method for the form (i.e. GET, POST)
        components (list): List of Component of the form
    
    Returns:
        FormComponent: The new component
    """
    new_component = FormComponent(action, method, components)    
    self.components.append(new_component)
    return new_component
    

  def add_formtext(self, label: str, name: str, placeholder: str = '', value: str = '') -> FormtextComponent:
    """Renders a form

    Args:
        label (str): Label for the form text
        name (str): Name for the form text
        placeholder (str): Optional. Placeholder
        value (str): Optional. Value if you want to pre-populate
    
    Returns:
        FormtextComponent: The new component
    """
    new_component = FormtextComponent(label, name, placeholder, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formemail(self, label: str = 'Your E-mail', name: str = 'email', placeholder: str = 'user@example.com') -> FormemailComponent:
    """Renders a form email

    Args:
        label (str): Optional. Label for the form email
        name (str): Optional. Name for the form email
        placeholder (str): Optional. Placeholder
    
    Returns:
        FormemailComponent: The new component
    """
    new_component = FormemailComponent(label, name, placeholder)    
    self.components.append(new_component)
    return new_component
    

  def add_formpassword(self, label: str = 'Password', name: str = 'password', placeholder: str = 'password') -> FormpasswordComponent:
    """Renders a form password

    Args:
        label (str): Optional. Label for the form password
        name (str): Optional. Name for the form password
        placeholder (str): Optional. Placeholder
    
    Returns:
        FormpasswordComponent: The new component
    """
    new_component = FormpasswordComponent(label, name, placeholder)    
    self.components.append(new_component)
    return new_component
    

  def add_formselect(self, label: str, name: str, options, value: str = '') -> FormselectComponent:
    """Renders a form select

    Args:
        label (str): Label for the form select
        name (str): Name for the form select
        options: Options for the form select
        value (str): Optional. Selected value
    
    Returns:
        FormselectComponent: The new component
    """
    new_component = FormselectComponent(label, name, options, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formtextarea(self, label: str = 'Your Message', name: str = 'message', placeholder: str = 'Leave a comment...', value: str = '') -> FormtextareaComponent:
    """Renders a text area

    Args:
        label (str): Optional. Label for the text area
        name (str): Optional. Name for the text area
        placeholder (str): Optional. Placeholder
        value (str): Optional. Value if you want to pre-populate
    
    Returns:
        FormtextareaComponent: The new component
    """
    new_component = FormtextareaComponent(label, name, placeholder, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formsubmit(self, label: str = 'Submit') -> FormsubmitComponent:
    """Renders a form submit button

    Args:
        label (str): Optional. Label for the form submit button
    
    Returns:
        FormsubmitComponent: The new component
    """
    new_component = FormsubmitComponent(label)    
    self.components.append(new_component)
    return new_component
    


  def add_pandastable(self, dataframe, hide_fields: list = [], action_buttons: list = None):
    """Renders a pandas table

    Args:
        dataframe: Dataframe to render
        hide_fields (list): List of fields to hide
        action_buttons (list): Row actions to render
    
    Returns:
        PandastableComponent: The new component
    """
    advanced_add_pandastable(self, dataframe, hide_fields, action_buttons)
    return self
    

  def add_plotlyfigure(self, fig, id: str = '') -> PlotlyfigureComponent:
    """Renders a plotly figure

    Args:
        fig: Figure to render
        id (str): Optional. Unique ID for this element. Will default to a UUID.
    
    Returns:
        PlotlyfigureComponent: The new component
    """
    new_component = PlotlyfigureComponent(fig, id)    
    self.components.append(new_component)
    return new_component
    

  def add_scriptstatus(self, job_id: str, redirect_url: str) -> ScriptstatusComponent:
    """Shows the status of a script execution and redirects to a new page when complete

    Args:
        job_id (str): Job id to check the status of
        redirect_url (str): URL to redirect to when the script is complete
    
    Returns:
        ScriptstatusComponent: The new component
    """
    new_component = ScriptstatusComponent(job_id, redirect_url)    
    self.components.append(new_component)
    return new_component
    

class DividerComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_divider` method of the parent component.
  """
  def __init__(self):    
    pass
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<hr class="my-5 border-gray-300 w-full">'''

class Footer(Component):
  """Renders a footer
  """
  def __init__(self, title: str = '', subtitle: str = '', logo: str = '', link: str = '', components: list = None):    
    self.title = title
    self.subtitle = subtitle
    self.logo = logo
    self.link = link
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<footer class="text-gray-600 body-font">
    <div class="container px-5 mx-auto flex md:items-center lg:items-start md:flex-row md:flex-nowrap flex-wrap flex-col">
        <a href="''' + self.link + '''" class="w-64 flex-shrink-0 md:mx-0 mx-auto text-center md:text-left">
            <span class="flex title-font font-medium items-center md:justify-start justify-center text-gray-900 dark:text-white"><img class="object-scale-down h-10" src="''' + self.logo + '''"><span class="ml-3 text-xl">''' + self.title + '''</span></span>
            <p class="mt-2 text-sm text-gray-500">''' + self.subtitle + '''</p>
        </a>
        <div class="flex-grow flex flex-wrap md:pl-20 -mb-10 md:mt-0 mt-10 md:text-left text-center">
            ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
        </div>
    </div>
</footer>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_footercategory(self, title: str, components: list = None) -> FootercategoryComponent:
    """Renders a category in the footer

    Args:
        title (str): Title of the category
        components (list): List of Footer Link in the category
    
    Returns:
        FootercategoryComponent: The new component
    """
    new_component = FootercategoryComponent(title, components)    
    self.components.append(new_component)
    return new_component
    

class FootercategoryComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_footercategory` method of the parent component.
  """
  def __init__(self, title: str, components: list = None):    
    self.title = title
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="lg:w-1/4 md:w-1/2 w-full px-4">
    <h2 class="title-font font-medium text-gray-900 dark:text-white tracking-widest text-sm mb-3 uppercase">''' + self.title + '''</h2>
    <nav class="list-none mb-10">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </nav>
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_footerlink(self, title: str, url: str) -> FooterlinkComponent:
    """Renders a link in the footer

    Args:
        title (str): Title of the link
        url (str): URL of the link
    
    Returns:
        FooterlinkComponent: The new component
    """
    new_component = FooterlinkComponent(title, url)    
    self.components.append(new_component)
    return new_component
    

class FooterlinkComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_footerlink` method of the parent component.
  """
  def __init__(self, title: str, url: str):    
    self.title = title
    self.url = url
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<li><a href="''' + self.url + '''" class="text-gray-600 hover:text-gray-800 dark:hover:text-white">''' + self.title + '''</a></li>'''

class FormComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_form` method of the parent component.
  """
  def __init__(self, action: str = '?', method: str = 'GET', components: list = None):    
    self.action = action
    self.method = method
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<form class="max-w-full" style="width: 500px" onsubmit="setLoading(this)" action="''' + self.action + '''" method="''' + self.method + '''">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</form>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_text(self, value: str) -> TextComponent:
    """Renders a paragraph of text

    Args:
        value (str): Text to be rendered
    
    Returns:
        TextComponent: The new component
    """
    new_component = TextComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_link(self, text: str, url: str, classes: str = '') -> LinkComponent:
    """Renders a link

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        LinkComponent: The new component
    """
    new_component = LinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_list(self, show_dots: bool = True, classes: str = '', components: list = None) -> ListComponent:
    """Renders a list of items

    Args:
        show_dots (bool): Optional. Whether or not to show dots
        classes (str): Optional. Classes to be applied to the list
        components (list): Items to be rendered
    
    Returns:
        ListComponent: The new component
    """
    new_component = ListComponent(show_dots, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_image(self, url: str, alt: str, classes: str = '') -> ImageComponent:
    """Renders an image

    Args:
        url (str): URL of the image
        alt (str): Alt text for the image
        classes (str): Optional. Classes to be applied to the image
    
    Returns:
        ImageComponent: The new component
    """
    new_component = ImageComponent(url, alt, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_container(self, grid_columns: int = None, classes: str = '', components: list = None) -> ContainerComponent:
    """Renders a container to help with layout

    Args:
        grid_columns (int): Optional. Number of columns (if any) to use. 1-12
        classes (str): Optional. Classes to be applied to the container
        components (list): Components to be rendered inside the container
    
    Returns:
        ContainerComponent: The new component
    """
    new_component = ContainerComponent(grid_columns, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_code(self, value: str, header: str = '', prefix: str = '>>>') -> CodeComponent:
    """Renders a block of code

    Args:
        value (str): Code to be rendered
        header (str): Optional. Header to be rendered above the code block
        prefix (str): Optional. Prefix to be rendered before the code block
    
    Returns:
        CodeComponent: The new component
    """
    new_component = CodeComponent(value, header, prefix)    
    self.components.append(new_component)
    return new_component
    

  def add_formtext(self, label: str, name: str, placeholder: str = '', value: str = '') -> FormtextComponent:
    """Renders a form

    Args:
        label (str): Label for the form text
        name (str): Name for the form text
        placeholder (str): Optional. Placeholder
        value (str): Optional. Value if you want to pre-populate
    
    Returns:
        FormtextComponent: The new component
    """
    new_component = FormtextComponent(label, name, placeholder, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formemail(self, label: str = 'Your E-mail', name: str = 'email', placeholder: str = 'user@example.com') -> FormemailComponent:
    """Renders a form email

    Args:
        label (str): Optional. Label for the form email
        name (str): Optional. Name for the form email
        placeholder (str): Optional. Placeholder
    
    Returns:
        FormemailComponent: The new component
    """
    new_component = FormemailComponent(label, name, placeholder)    
    self.components.append(new_component)
    return new_component
    

  def add_formpassword(self, label: str = 'Password', name: str = 'password', placeholder: str = 'password') -> FormpasswordComponent:
    """Renders a form password

    Args:
        label (str): Optional. Label for the form password
        name (str): Optional. Name for the form password
        placeholder (str): Optional. Placeholder
    
    Returns:
        FormpasswordComponent: The new component
    """
    new_component = FormpasswordComponent(label, name, placeholder)    
    self.components.append(new_component)
    return new_component
    

  def add_formselect(self, label: str, name: str, options, value: str = '') -> FormselectComponent:
    """Renders a form select

    Args:
        label (str): Label for the form select
        name (str): Name for the form select
        options: Options for the form select
        value (str): Optional. Selected value
    
    Returns:
        FormselectComponent: The new component
    """
    new_component = FormselectComponent(label, name, options, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formhidden(self, name: str, value: str) -> FormhiddenComponent:
    """Renders a hidden field on a form. This is useful for carrying state between pages without having to store data in the database.

    Args:
        name (str): Name for the form hidden
        value (str): Value for the form hidden
    
    Returns:
        FormhiddenComponent: The new component
    """
    new_component = FormhiddenComponent(name, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formtextarea(self, label: str = 'Your Message', name: str = 'message', placeholder: str = 'Leave a comment...', value: str = '') -> FormtextareaComponent:
    """Renders a text area

    Args:
        label (str): Optional. Label for the text area
        name (str): Optional. Name for the text area
        placeholder (str): Optional. Placeholder
        value (str): Optional. Value if you want to pre-populate
    
    Returns:
        FormtextareaComponent: The new component
    """
    new_component = FormtextareaComponent(label, name, placeholder, value)    
    self.components.append(new_component)
    return new_component
    

  def add_formsubmit(self, label: str = 'Submit') -> FormsubmitComponent:
    """Renders a form submit button

    Args:
        label (str): Optional. Label for the form submit button
    
    Returns:
        FormsubmitComponent: The new component
    """
    new_component = FormsubmitComponent(label)    
    self.components.append(new_component)
    return new_component
    

  def add_rawtable(self, components: list = None) -> RawtableComponent:
    """Renders a table manually by constructing the table header, body, content, etc.. This is useful if you want to customize the table more than what the other table functions allow. Most of the time you'll use the other table functions instead of this one.

    Args:
        components (list): Components to render in the table
    
    Returns:
        RawtableComponent: The new component
    """
    new_component = RawtableComponent(components)    
    self.components.append(new_component)
    return new_component
    

class FormemailComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_formemail` method of the parent component.
  """
  def __init__(self, label: str = 'Your E-mail', name: str = 'email', placeholder: str = 'user@example.com'):    
    self.label = label
    self.name = name
    self.placeholder = placeholder
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <input type="email" name="''' + self.name + '''" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="''' + self.placeholder + '''" required>
</div>'''

class FormhiddenComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_formhidden` method of the parent component.
  """
  def __init__(self, name: str, value: str):    
    self.name = name
    self.value = value
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<input type="hidden" name="''' + self.name + '''" value="''' + self.value + '''">'''

class FormpasswordComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_formpassword` method of the parent component.
  """
  def __init__(self, label: str = 'Password', name: str = 'password', placeholder: str = 'password'):    
    self.label = label
    self.name = name
    self.placeholder = placeholder
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <input type="password" name="''' + self.name + '''" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="''' + self.placeholder + '''" required>
</div>'''

class FormselectComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_formselect` method of the parent component.
  """
  def __init__(self, label: str, name: str, options, value: str = ''):    
    self.label = label
    self.name = name
    self.options = options
    self.value = value
    self.components = []
    
    if value == "":
        self.components.append(HtmlComponent('<option value="" selected disabled hidden>Select an option</option>'))
    
    for option in self.options:
        if isinstance(option, str):
            if option == value:
                self.components.append(SelectoptionComponent(label=option, value=option, selected='selected'))
            else:
                self.components.append(SelectoptionComponent(label=option, value=option))
        else:
            if option['value'] == value:
                self.components.append(SelectoptionComponent(label=option['label'], value=option['value'], selected='selected'))
            else:
                self.components.append(SelectoptionComponent(label=option['label'], value=option['value']))

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <select id="''' + self.name + '''" name="''' + self.name + '''" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </select>
</div>'''

  def add_selectoption(self, label: str, value: str, selected: str = '') -> SelectoptionComponent:
    """Renders a select option

    Args:
        label (str): Label for the select option
        value (str): Value for the select option
        selected (str): Optional. Use 'selected' if this is selected
    
    Returns:
        SelectoptionComponent: The new component
    """
    new_component = SelectoptionComponent(label, value, selected)    
    self.components.append(new_component)
    return new_component
    

class FormsubmitComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_formsubmit` method of the parent component.
  """
  def __init__(self, label: str = 'Submit'):    
    self.label = label
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">''' + self.label + '''</button>'''

class FormtextComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_formtext` method of the parent component.
  """
  def __init__(self, label: str, name: str, placeholder: str = '', value: str = ''):    
    self.label = label
    self.name = name
    self.placeholder = placeholder
    self.value = value
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <input type="text" name="''' + self.name + '''" value="''' + self.value + '''" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="''' + self.placeholder + '''" required>
</div>'''

class FormtextareaComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_formtextarea` method of the parent component.
  """
  def __init__(self, label: str = 'Your Message', name: str = 'message', placeholder: str = 'Leave a comment...', value: str = ''):    
    self.label = label
    self.name = name
    self.placeholder = placeholder
    self.value = value
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="mb-6">
    <label for="''' + self.name + '''" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">''' + self.label + '''</label>
    <textarea name="''' + self.name + '''" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="''' + self.placeholder + '''">''' + self.value + '''</textarea>
</div>'''

class HeaderComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_header` method of the parent component.
  """
  def __init__(self, text: str, size: int = 5, classes: str = ''):    
    self.text = text
    self.size = size
    self.classes = classes
    if size == 1:
        self.classes += " text-lg sm:text-xl"
    elif size == 2:
        self.classes += " text-lg sm:text-2xl"
    elif size == 3:
        self.classes += " text-lg sm:text-3xl"
    elif size == 4:
        self.classes += " text-lg sm:text-4xl"
    elif size == 5:
        self.classes += " text-xl sm:text-5xl"
    elif size == 6:
        self.classes += " text-2xl sm:text-6xl"
    elif size == 7:
        self.classes += " text-3xl sm:text-7xl"
    elif size == 8:
        self.classes += " text-4xl sm:text-8xl"
    elif size == 9:
        self.classes += " text-5xl sm:text-9xl"
    else:
        raise ValueError("Header size must be between 1 and 9")

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<p class="mb-4 font-extrabold leading-none tracking-tight text-gray-900 dark:text-white ''' + self.classes + ''' ">''' + self.text + '''</p>'''

class HtmlComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_html` method of the parent component.
  """
  def __init__(self, value: str):    
    self.value = value
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''''' + self.value + ''''''

class ImageComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_image` method of the parent component.
  """
  def __init__(self, url: str, alt: str, classes: str = ''):    
    self.url = url
    self.alt = alt
    self.classes = classes
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<img class="max-w-fit h-auto rounded-lg ''' + self.classes + ''' " src="''' + self.url + '''" alt="''' + self.alt + '''">'''

class LinkComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_link` method of the parent component.
  """
  def __init__(self, text: str, url: str, classes: str = ''):    
    self.text = text
    self.url = url
    self.classes = classes
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<p class="text-gray-500 dark:text-gray-400 ''' + self.classes + '''">
    <a href="''' + self.url + '''" class="inline-flex items-center font-medium text-blue-600 dark:text-blue-500 hover:underline">
    ''' + self.text + '''
    <svg aria-hidden="true" class="w-5 h-5 ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
    </a>
</p>'''

class ListComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_list` method of the parent component.
  """
  def __init__(self, show_dots: bool = True, classes: str = '', components: list = None):    
    self.show_dots = show_dots
    self.classes = classes
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    if self.show_dots:
        self.classes += "list-disc"
    else:
        self.classes += "list-none"

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<ul class="max-w-md space-y-1 text-gray-500 list-inside dark:text-gray-400 ''' + self.classes + '''">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</ul>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_listitem(self, value: str, classes: str = '', svg: str = '', is_checked: bool = None) -> ListitemComponent:
    """Renders an item in a list

    Args:
        value (str): Text to be rendered
        classes (str): Optional. Classes to be applied to the list item
        svg (str): Optional. SVG to render inside the list
        is_checked (bool): Optional. Whether or not the item is checked
    
    Returns:
        ListitemComponent: The new component
    """
    new_component = ListitemComponent(value, classes, svg, is_checked)    
    self.components.append(new_component)
    return new_component
    

class ListitemComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_listitem` method of the parent component.
  """
  def __init__(self, value: str, classes: str = '', svg: str = '', is_checked: bool = None):    
    self.value = value
    self.classes = classes
    self.svg = svg
    self.is_checked = is_checked
    if self.is_checked is not None:
        if self.is_checked:
            self.svg = '''<svg class="w-4 h-4 mr-1.5 text-green-500 dark:text-green-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>'''
        else:
            self.svg = '''<svg class="w-4 h-4 mr-1.5 text-gray-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path></svg>'''

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<li class="flex items-center ''' + self.classes + '''">
    ''' + self.svg + '''
    ''' + self.value + '''
</li>'''

class Navbar(Component):
  """Renders a navbar
  """
  def __init__(self, title: str, logo: str = 'https://cdn.pycob.com/pyvibe.png', components: list = None):    
    self.title = title
    self.logo = logo
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<script>
    function toggleNav() {
        var nav = document.getElementById("navbar-sticky");
        if (nav.classList.contains("hidden")) {
            nav.classList.remove("hidden");
        } else {
            nav.classList.add("hidden");
        }
    }
</script>
<nav class="gradient-background top-0 left-0 z-20 w-full bg-white px-2 py-2.5 dark:border-gray-600 sm:px-4">
    <div class="container mx-auto flex flex-wrap items-center justify-between">
      <a href="/" class="flex items-center">
        <img src="''' + self.logo + '''" class="mr-3 h-6 sm:h-9" alt="Logo" />
        <span class="self-center whitespace-nowrap md:text-4xl font-semibold text-white">''' + self.title + '''</span>
      </a>
      <div class="flex md:order-2">
        <button onclick="toggleDarkMode()" type="button" class="mx-3 px-3 py-2 text-xs font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500">
            <svg id="sun" data-toggle-icon="sun" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
            <svg id="moon" data-toggle-icon="moon" class="w-4 h-4 hidden" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>        </button>

        <button onclick="toggleNav()" data-collapse-toggle="navbar-sticky" type="button" class="inline-flex items-center rounded-lg p-2 text-sm text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-600 md:hidden" aria-controls="navbar-sticky" aria-expanded="true">
          <span class="sr-only">Open main menu</span>
          <svg class="h-6 w-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
        </button>
      </div>
      <div class="w-full items-center justify-between md:order-1 md:flex md:w-auto hidden" id="navbar-sticky">
        <ul class="mt-4 flex flex-col rounded-lg md:mt-0 md:flex-row md:space-x-8 md:border-0 md:text-sm md:font-medium">
          ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
        </ul>
      </div>
    </div>
  </nav>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_link(self, text: str, url: str, classes: str = '') -> LinkComponent:
    """Renders a link

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        LinkComponent: The new component
    """
    new_component = LinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_plainlink(self, text: str, url: str, classes: str = '') -> PlainlinkComponent:
    """Renders a link without any styling

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        PlainlinkComponent: The new component
    """
    new_component = PlainlinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_navbarlink(self, text: str, url: str, classes: str = '') -> NavbarlinkComponent:
    """Renders a link in the navbar

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        NavbarlinkComponent: The new component
    """
    new_component = NavbarlinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

class NavbarlinkComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_navbarlink` method of the parent component.
  """
  def __init__(self, text: str, url: str, classes: str = ''):    
    self.text = text
    self.url = url
    self.classes = classes
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<a class="block rounded-lg py-2 pl-3 pr-4 text-white hover:bg-blue-800 md:p-2 ''' + self.classes + '''" href="''' + self.url + '''">''' + self.text + '''</a>'''

class Page(Component):
  """A page is the top level component of a website. It contains the navbar, the main content, and the footer.
  """
  def __init__(self, title: str = '', description: str = '', image: str = '', additional_head: str = '', navbar: Navbar = Navbar(title='PyVibe App'), footer: Footer = Footer(title='Made with PyVibe', logo='https://cdn.pycob.com/pyvibe.png', link='https://www.pyvibe.com'), sidebar: Sidebar = None, components: list = None):    
    self.title = title
    self.description = description
    self.image = image
    self.additional_head = additional_head
    self.navbar = navbar
    self.footer = footer
    self.sidebar = sidebar
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    if self.sidebar is None:
        self.sidebar = HtmlComponent('')
    if self.navbar is None:
        self.navbar = HtmlComponent('')
    if self.footer is None:
        self.footer = HtmlComponent('')

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<!doctype html>
    <html>
    <head>
    <meta charset="UTF-8">
    <link rel="apple-touch-icon" sizes="180x180" href="https://cdn.pycob.com/pyvibe/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="https://cdn.pycob.com/pyvibe/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="https://cdn.pycob.com/pyvibe/favicon-16x16.png">
    <link rel="mask-icon" href="https://cdn.pycob.com/pyvibe/safari-pinned-tab.svg" color="#5bbad5">
    <link rel="shortcut icon" href="https://cdn.pycob.com/pyvibe/favicon.ico">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="msapplication-config" content="https://cdn.pycob.com/pyvibe/browserconfig.xml">
    <meta name="theme-color" content="#ffffff">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + self.title + '''</title>
    <meta property="og:title" content="''' + self.title + '''">
    <meta property="og:description" content="''' + self.description + '''">
    <meta property="og:image" content="''' + self.image + '''">
    ''' + self.additional_head + '''
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/ag-grid-community/dist/ag-grid-community.min.js"></script>
    <script src="https://cdn.plot.ly/plotly-2.18.2.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        clifford: '#da373d',
                    }
                }
            },
            darkMode: 'class'
        }
    </script>
    <script>
    function toggleDarkMode() {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark')
            document.getElementById("moon").classList.add("hidden")
            document.getElementById("sun").classList.remove("hidden")
        } else {
            document.documentElement.classList.add('dark')
            document.getElementById("sun").classList.add("hidden")
            document.getElementById("moon").classList.remove("hidden")
        }
    }

    function setLoading(el) {
        el.querySelectorAll("button[type=submit]").forEach((button) => {
            button.innerHTML = '<svg aria-hidden="true" role="status" class="inline w-4 h-4 mr-3 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/><path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/></svg>Loading...';
            button.disabled = true;
        });
    }

    function toggleMore(button) {
        x = button

        if (x.innerHTML === "more") {
            x.innerHTML = "less";
            text_full = x.getAttribute("data-text-full")
            text_truncated = x.getAttribute("data-text-truncated")

            x.parentElement.innerHTML = text_full + ' <button data-text-full="' + text_full + '" data-text-truncated="' + text_truncated + '" onclick="toggleMore(this)" class="text-blue-500">less</button>'
        } else {
            x.innerHTML = "more";
            text_full = x.getAttribute("data-text-full")
            text_truncated = x.getAttribute("data-text-truncated")

            x.parentElement.innerHTML = text_truncated + ' <button data-text-full="' + text_full + '" data-text-truncated="' + text_truncated + '" onclick="toggleMore(this)" class="text-blue-500">more</button>'
        }
    }
    </script>
    <style>
    .gradient-background {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 180s ease infinite;
    }

    .gradient-text {
        color: transparent;
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-clip: text;
        -webkit-background-clip: text;
        animation: gradient 2s ease infinite;
    }

    @keyframes gradient {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    </style>
    </head>
    <body class="flex flex-col h-screen dark:bg-gray-900 ">
        ''' + self.navbar.to_html() + '''
        <div class="flex">
            ''' + self.sidebar.to_html() + '''
            <div id="page-container" class="container px-5 my-5 mx-auto">
                ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
            </div>
        </div>
        ''' + self.footer.to_html() + '''
    </body>
</html>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_html(self, value: str) -> HtmlComponent:
    """Renders raw HTML. This is meant to be an escape hatch for when you need to render something that isn't supported by PyVibe.

    Args:
        value (str): Raw HTML code to be rendered
    
    Returns:
        HtmlComponent: The new component
    """
    new_component = HtmlComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_text(self, value: str) -> TextComponent:
    """Renders a paragraph of text

    Args:
        value (str): Text to be rendered
    
    Returns:
        TextComponent: The new component
    """
    new_component = TextComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_link(self, text: str, url: str, classes: str = '') -> LinkComponent:
    """Renders a link

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        LinkComponent: The new component
    """
    new_component = LinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_plainlink(self, text: str, url: str, classes: str = '') -> PlainlinkComponent:
    """Renders a link without any styling

    Args:
        text (str): Text to be rendered
        url (str): URL to link to
        classes (str): Optional. Classes to be applied to the link
    
    Returns:
        PlainlinkComponent: The new component
    """
    new_component = PlainlinkComponent(text, url, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_list(self, show_dots: bool = True, classes: str = '', components: list = None) -> ListComponent:
    """Renders a list of items

    Args:
        show_dots (bool): Optional. Whether or not to show dots
        classes (str): Optional. Classes to be applied to the list
        components (list): Items to be rendered
    
    Returns:
        ListComponent: The new component
    """
    new_component = ListComponent(show_dots, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_image(self, url: str, alt: str, classes: str = '') -> ImageComponent:
    """Renders an image

    Args:
        url (str): URL of the image
        alt (str): Alt text for the image
        classes (str): Optional. Classes to be applied to the image
    
    Returns:
        ImageComponent: The new component
    """
    new_component = ImageComponent(url, alt, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_header(self, text: str, size: int = 5, classes: str = '') -> HeaderComponent:
    """Renders a header

    Args:
        text (str): Text to be rendered
        size (int): Optional. Size of the header. Choose 1-9
        classes (str): Optional. Classes to be applied to the header
    
    Returns:
        HeaderComponent: The new component
    """
    new_component = HeaderComponent(text, size, classes)    
    self.components.append(new_component)
    return new_component
    

  def add_card(self, center_content: bool = False, classes: str = '', components: list = None) -> CardComponent:
    """Renders a card

    Args:
        center_content (bool): Optional. Whether the card contents should be centered
        classes (str): Optional. Classes to be applied to the card
        components (list): Components to be rendered inside the card
    
    Returns:
        CardComponent: The new component
    """
    new_component = CardComponent(center_content, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_container(self, grid_columns: int = None, classes: str = '', components: list = None) -> ContainerComponent:
    """Renders a container to help with layout

    Args:
        grid_columns (int): Optional. Number of columns (if any) to use. 1-12
        classes (str): Optional. Classes to be applied to the container
        components (list): Components to be rendered inside the container
    
    Returns:
        ContainerComponent: The new component
    """
    new_component = ContainerComponent(grid_columns, classes, components)    
    self.components.append(new_component)
    return new_component
    

  def add_alert(self, text: str, badge: str = '', color: str = 'indigo') -> AlertComponent:
    """Renders an alert

    Args:
        text (str): Text to be rendered
        badge (str): Optional. Text to be rendered inside the badge
        color (str): Optional. Color of the. Choose 'indigo', 'orange', or 'red'
    
    Returns:
        AlertComponent: The new component
    """
    new_component = AlertComponent(text, badge, color)    
    self.components.append(new_component)
    return new_component
    

  def add_code(self, value: str, header: str = '', prefix: str = '>>>') -> CodeComponent:
    """Renders a block of code

    Args:
        value (str): Code to be rendered
        header (str): Optional. Header to be rendered above the code block
        prefix (str): Optional. Prefix to be rendered before the code block
    
    Returns:
        CodeComponent: The new component
    """
    new_component = CodeComponent(value, header, prefix)    
    self.components.append(new_component)
    return new_component
    

  def add_divider(self) -> DividerComponent:
    """Renders a divider

    
    
    Returns:
        DividerComponent: The new component
    """
    new_component = DividerComponent()    
    self.components.append(new_component)
    return new_component
    

  def add_section(self, id: str, name: str, level: int = 1) -> SectionComponent:
    """Creates an invisible element that can be used to link to in the sidebar

    Args:
        id (str): ID for the section. This is what will appear in the link as /page#id
        name (str): Name of the section. This is what will appear in the navigation bar
        level (int): Optional. Level of the section. This is the indentation that will appear in the navigation bar
    
    Returns:
        SectionComponent: The new component
    """
    new_component = SectionComponent(id, name, level)    
    self.components.append(new_component)
    return new_component
    

  def add_form(self, action: str = '?', method: str = 'GET', components: list = None) -> FormComponent:
    """Renders a form

    Args:
        action (str): Optional. Action for the form. This is the page that the form will submit to. Defaults to the current page
        method (str): Optional. Method for the form (i.e. GET, POST)
        components (list): List of Component of the form
    
    Returns:
        FormComponent: The new component
    """
    new_component = FormComponent(action, method, components)    
    self.components.append(new_component)
    return new_component
    

  def add_rawtable(self, components: list = None) -> RawtableComponent:
    """Renders a table manually by constructing the table header, body, content, etc.. This is useful if you want to customize the table more than what the other table functions allow. Most of the time you'll use the other table functions instead of this one.

    Args:
        components (list): Components to render in the table
    
    Returns:
        RawtableComponent: The new component
    """
    new_component = RawtableComponent(components)    
    self.components.append(new_component)
    return new_component
    


  def add_pandastable(self, dataframe, hide_fields: list = [], action_buttons: list = None):
    """Renders a pandas table

    Args:
        dataframe: Dataframe to render
        hide_fields (list): List of fields to hide
        action_buttons (list): Row actions to render
    
    Returns:
        PandastableComponent: The new component
    """
    advanced_add_pandastable(self, dataframe, hide_fields, action_buttons)
    return self
    

  def add_plotlyfigure(self, fig, id: str = '') -> PlotlyfigureComponent:
    """Renders a plotly figure

    Args:
        fig: Figure to render
        id (str): Optional. Unique ID for this element. Will default to a UUID.
    
    Returns:
        PlotlyfigureComponent: The new component
    """
    new_component = PlotlyfigureComponent(fig, id)    
    self.components.append(new_component)
    return new_component
    


  def add_datagrid(self, dataframe, action_buttons: list = None):
    """Renders a data grid

    Args:
        dataframe: Dataframe to render
        action_buttons (list): Row actions to render
    
    Returns:
        DatagridComponent: The new component
    """
    advanced_add_datagrid(self, dataframe, action_buttons)
    return self
    

  def add_codeeditor(self, value: str, language: str = 'python') -> CodeeditorComponent:
    """Renders a code editor

    Args:
        value (str): Code to be rendered
        language (str): Optional. Language mode for syntax highlighting
    
    Returns:
        CodeeditorComponent: The new component
    """
    new_component = CodeeditorComponent(value, language)    
    self.components.append(new_component)
    return new_component
    


  def add_emgithub(self, url: str):
    """Renders a block of code from a github URL

    Args:
        url (str): URL of the GitHub file to be rendered
    
    Returns:
        EmgithubComponent: The new component
    """
    advanced_add_emgithub(self, url)
    return self
    

  def add_scriptstatus(self, job_id: str, redirect_url: str) -> ScriptstatusComponent:
    """Shows the status of a script execution and redirects to a new page when complete

    Args:
        job_id (str): Job id to check the status of
        redirect_url (str): URL to redirect to when the script is complete
    
    Returns:
        ScriptstatusComponent: The new component
    """
    new_component = ScriptstatusComponent(job_id, redirect_url)    
    self.components.append(new_component)
    return new_component
    

class PlainlinkComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_plainlink` method of the parent component.
  """
  def __init__(self, text: str, url: str, classes: str = ''):    
    self.text = text
    self.url = url
    self.classes = classes
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<a class="''' + self.classes + '''" href="''' + self.url + '''">''' + self.text + '''</a>'''

class PlotlyfigureComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_plotlyfigure` method of the parent component.
  """
  def __init__(self, fig, id: str = ''):    
    self.fig = fig
    self.id = id
    if id == "":
        self.id = str(uuid.uuid4())
    self.fig = fig.to_json()

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div id="''' + self.id + '''"></div>
<script>
    config = ''' + self.fig + '''
    Plotly.newPlot( document.getElementById("''' + self.id + '''"), config, {responsive: true} );
</script>'''

class RawtableComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_rawtable` method of the parent component.
  """
  def __init__(self, components: list = None):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="relative overflow-x-auto shadow-md mb-5 sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </table>
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_tablehead(self, components: list = None) -> TableheadComponent:
    """Renders a table head

    Args:
        components (list): Components to render in the table head
    
    Returns:
        TableheadComponent: The new component
    """
    new_component = TableheadComponent(components)    
    self.components.append(new_component)
    return new_component
    

  def add_tablerow(self, components: list = None) -> TablerowComponent:
    """Renders a table row

    Args:
        components (list): Components to render in the table row
    
    Returns:
        TablerowComponent: The new component
    """
    new_component = TablerowComponent(components)    
    self.components.append(new_component)
    return new_component
    

  def add_tablebody(self, components: list = None) -> TablebodyComponent:
    """Renders a table body

    Args:
        components (list): Components to render in the table body
    
    Returns:
        TablebodyComponent: The new component
    """
    new_component = TablebodyComponent(components)    
    self.components.append(new_component)
    return new_component
    

class Rowaction(Component):
  """Renders a row action
  """
  def __init__(self, label: str, url: str, classes: str = '', open_in_new_window: bool = True):    
    self.label = label
    self.url = url
    self.classes = classes
    self.open_in_new_window = open_in_new_window
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''TODO: Internal Component'''

class ScriptstatusComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_scriptstatus` method of the parent component.
  """
  def __init__(self, job_id: str, redirect_url: str):    
    self.job_id = job_id
    self.redirect_url = redirect_url
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<script type="module">
    import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js'
        
    import { getFirestore, doc, onSnapshot } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-firestore.js'

    // TODO: Replace the following with your app's Firebase project configuration
    const firebaseConfig = {
        projectId: "pycob-prod"
    };

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);

    let db = getFirestore();

    const unsub = onSnapshot(doc(db, "users", "test", "_jobs", "''' + self.job_id + '''"), (doc) => {
        console.log("Current data: ", doc.data());
        document.getElementById("''' + self.job_id + '''").innerHTML = doc.data().status;

        if (doc.data().status == "complete") {
            unsub();
            window.location.href = "''' + self.redirect_url + '''";
        }
    });
</script>
<div class="flex items-center justify-center p-5 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
    <svg aria-hidden="true" class="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/><path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/></svg>
    <div id="''' + self.job_id + '''" class="px-3 py-1 text-xs font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full animate-pulse dark:bg-blue-900 dark:text-blue-200">waiting...</div>
</div>'''

class SectionComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_section` method of the parent component.
  """
  def __init__(self, id: str, name: str, level: int = 1):    
    self.id = id
    self.name = name
    self.level = level
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<span id=''' + self.id + '''></span>'''

class SelectoptionComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_selectoption` method of the parent component.
  """
  def __init__(self, label: str, value: str, selected: str = ''):    
    self.label = label
    self.value = value
    self.selected = selected
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<option value="''' + self.value + '''" ''' + self.selected + '''>''' + self.label + '''</option>'''

class Sidebar(Component):
  """Renders a sidebar
  """
  def __init__(self, components: list = None):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<style>
@media (min-width: 1024px) {
    #page-container {
        max-width: calc( 100vw - 320px );
    }
}
</style>
<script>
    function smoothScrollTo(link) {
        console.log(link);
        var hashUrl = link.href;
        console.log(hashUrl);
        var hash = hashUrl.substring(hashUrl.indexOf("#") + 1);
        console.log(hash);
        var element = document.getElementById(hash);
        console.log(element);
        if (element) {
            element.scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"})
        }
        return true;
    }
</script>
<aside style="min-width: 300px" class="hidden lg:block overflow-y-auto flex w-72 flex-col space-y-2 bg-gray-50 dark:bg-gray-800 p-2 h-screen sticky top-0">
    <div class="sticky top-0">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </div>
</aside>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_sidebarcategory(self, title: str, components: list = None) -> SidebarcategoryComponent:
    """Renders a category in the sidebar

    Args:
        title (str): Title of the category
        components (list): List of Sidebar Link in the category
    
    Returns:
        SidebarcategoryComponent: The new component
    """
    new_component = SidebarcategoryComponent(title, components)    
    self.components.append(new_component)
    return new_component
    

class SidebarcategoryComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_sidebarcategory` method of the parent component.
  """
  def __init__(self, title: str, components: list = None):    
    self.title = title
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<div class="mb-8">
    <h2 class="text-lg font-medium text-gray-500 dark:text-gray-400 tracking-wider uppercase mb-3">''' + self.title + '''</h2>
    <ul class="ml-5 list-none">
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </ul>
</div>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_sidebarlink(self, title: str, url: str) -> SidebarlinkComponent:
    """Renders a link in the sidebar

    Args:
        title (str): Title of the link
        url (str): URL of the link
    
    Returns:
        SidebarlinkComponent: The new component
    """
    new_component = SidebarlinkComponent(title, url)    
    self.components.append(new_component)
    return new_component
    

class SidebarlinkComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_sidebarlink` method of the parent component.
  """
  def __init__(self, title: str, url: str):    
    self.title = title
    self.url = url
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<li><a href="''' + self.url + '''" onclick="event.preventDefault(); smoothScrollTo(this)" class="text-gray-900 dark:text-white hover:text-gray-800">''' + self.title + '''</a></li>'''

class TablebodyComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_tablebody` method of the parent component.
  """
  def __init__(self, components: list = None):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<tbody>
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</tbody>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_tablerow(self, components: list = None) -> TablerowComponent:
    """Renders a table row

    Args:
        components (list): Components to render in the table row
    
    Returns:
        TablerowComponent: The new component
    """
    new_component = TablerowComponent(components)    
    self.components.append(new_component)
    return new_component
    

class TablecellComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_tablecell` method of the parent component.
  """
  def __init__(self, value: str):    
    self.value = value
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<td class="px-6 py-4 whitespace-nowrap">
    ''' + self.value + '''
</td>'''

class TablecellheaderComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_tablecellheader` method of the parent component.
  """
  def __init__(self, value: str):    
    self.value = value
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
    ''' + self.value + '''
</th>'''

class TablecolComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_tablecol` method of the parent component.
  """
  def __init__(self, components: list = None):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<td class="px-6 py-4 whitespace-nowrap">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</td>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
class TableheadComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_tablehead` method of the parent component.
  """
  def __init__(self, components: list = None):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<thead class="bg-gray-50 dark:bg-gray-800">
    <tr>
        ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
    </tr>
</thead>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_tablerow(self, components: list = None) -> TablerowComponent:
    """Renders a table row

    Args:
        components (list): Components to render in the table row
    
    Returns:
        TablerowComponent: The new component
    """
    new_component = TablerowComponent(components)    
    self.components.append(new_component)
    return new_component
    

  def add_tablecol(self, components: list = None) -> TablecolComponent:
    """Renders a table column

    Args:
        components (list): Components to render in the table column
    
    Returns:
        TablecolComponent: The new component
    """
    new_component = TablecolComponent(components)    
    self.components.append(new_component)
    return new_component
    

  def add_tablecell(self, value: str) -> TablecellComponent:
    """Renders a table cell

    Args:
        value (str): String to render in the table cell
    
    Returns:
        TablecellComponent: The new component
    """
    new_component = TablecellComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_tablecellheader(self, value: str) -> TablecellheaderComponent:
    """Renders a table cell header

    Args:
        value (str): String to render in the table cell header
    
    Returns:
        TablecellheaderComponent: The new component
    """
    new_component = TablecellheaderComponent(value)    
    self.components.append(new_component)
    return new_component
    

class TablerowComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_tablerow` method of the parent component.
  """
  def __init__(self, components: list = None):    
    # https://stackoverflow.com/questions/4841782/python-constructor-and-default-value
    self.components = components or []
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<tr class="border-t border-gray-200 dark:border-gray-700">
    ''' + '\n'.join(map(lambda x: x.to_html(), self.components)) + ''' 
</tr>'''

  def add(self, component):
    self.components.append(component)
    return self

  def add_component(self, component):
    self.components.append(component)
    return self
  def add_tablecol(self, components: list = None) -> TablecolComponent:
    """Renders a table column

    Args:
        components (list): Components to render in the table column
    
    Returns:
        TablecolComponent: The new component
    """
    new_component = TablecolComponent(components)    
    self.components.append(new_component)
    return new_component
    

  def add_tablecell(self, value: str) -> TablecellComponent:
    """Renders a table cell

    Args:
        value (str): String to render in the table cell
    
    Returns:
        TablecellComponent: The new component
    """
    new_component = TablecellComponent(value)    
    self.components.append(new_component)
    return new_component
    

  def add_tablecellheader(self, value: str) -> TablecellheaderComponent:
    """Renders a table cell header

    Args:
        value (str): String to render in the table cell header
    
    Returns:
        TablecellheaderComponent: The new component
    """
    new_component = TablecellheaderComponent(value)    
    self.components.append(new_component)
    return new_component
    

class TextComponent(Component):
  """You don't normally need to invoke this constructor directly. Instead, use the `.add_text` method of the parent component.
  """
  def __init__(self, value: str):    
    self.value = value
    

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    pass

  def to_html(self):
    return '''<p class="mb-6 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">''' + self.value + '''</p>'''


#
#
# Begin Manual Code
#
#
#
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

