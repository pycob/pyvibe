import pyvibe as pv
from .common.components import navbar, footer, marketing_banner, gallery_grid, featured_layouts

page = pv.Page("PyVibe", navbar=navbar, footer=footer, image="./img/social.png")

page.add_header("Easily create styled web pages with Python")

page.add_code("""import pyvibe as pv

page = pv.Page()

page.add_header("Welcome to PyVibe!")

page.add_text("PyVibe is an open source Python library for creating UI components for web apps without the need to write HTML code.")
""", prefix="", header="Example")

with page.add_card() as card:
    card.add_header("Welcome to PyVibe!")
    card.add_text("PyVibe is an open source Python library for creating UI components for web apps without the need to write HTML code.")

page.add_link("See All Components", "component_reference.html")
page.add_link("Interactive Playground", "playground.html")
page.add_text("")

page.add_header("What is PyVibe?", 3)
page.add_text("PyVibe is a Python library for creating web pages. It is designed to be a quick way for Python developers to build front-ends.")
page.add_text("PyVibe uses a component-based approach to building web pages. This means that you can create a page by combining components together.")

page.add_header("How do I use PyVibe?", 3)
page.add_text("PyVibe is a Python library that simplifies UI development for web apps by providing semantic Python components that compile into HTML and can be used with any web framework.")
page.add_text("Fundamentally, PyVibe returns an HTML string that can be used with:")

with page.add_list() as list:
    list.add_listitem("<b><a href='https://github.com/pycob/pyvibe/blob/main/generator/docs/about.py'>Static Pages</a></b>: Like the one you're viewing now", is_checked=True)
    list.add_listitem("<b><a href='flask.html'>Flask</a></b>: Inside a Flask function", is_checked=True)
    list.add_listitem("<b><a href='https://github.com/pycob/pyvibe/blob/main/generator/docs/playground.py#L124-L151'>Pyodide</a></b>: For dynamic client-side rendered pages", is_checked=True)

page.add_text("")

page.add_header("What can you build with PyVibe?", 3)
page.add_component(gallery_grid(featured_layouts))
page.add_link("See more examples", "/gallery.html")

page.add_header("Designed for Autocomplete", 3)
page.add_text("PyVibe is designed to be used with autocomplete. This means that you can type <code>page.add_</code> and autocomplete will show you all the components that you can add to your page along with documentation about the component.")
page.add_html('<img class="rounded-lg" src="./img/autocomplete.png" alt="Autocomplete">')

page.add_header("Themes", 3)
page.add_text('PyVibe is meant to be a generic framework. While the default theme uses <a href="https://flowbite.com/" class="font-medium text-blue-600 underline dark:text-blue-500 hover:no-underline">Flowbite</a>, which are components that use <a href="https://tailwindcss.com/" class="font-medium text-blue-600 underline dark:text-blue-500 hover:no-underline">TailwindCSS</a>, we envision including many themes and CSS frameworks in the future.')

page.add_header("How does PyVibe compare to Streamlit, Plotly Dash, Pynecone, Anvil, NiceGUI, etc?", 3)
page.add_text("PyVibe is not a web server -- it produces styled HTML that can be used with any web server.")

page.add_html(marketing_banner)