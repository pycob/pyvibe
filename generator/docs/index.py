import pyvibe as pv

navbar = pv.Navbar("PyVibe", button_url="login.html")
navbar.add_navbarlink("Component Reference", "component_reference.html")
navbar.add_navbarlink("Interactive Tutorial", "tutorial.html")
navbar.add_navbarlink('<svg class="w-4 h-4 mr-2 -ml-1" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="github" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512"><path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3 .3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5 .3-6.2 2.3zm44.2-1.7c-2.9 .7-4.9 2.6-4.6 4.9 .3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3 .7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3 .3 2.9 2.3 3.9 1.6 1 3.6 .7 4.3-.7 .7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3 .7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3 .7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"></path></svg> GitHub', "https://github.com/pycob/pyvibe", classes="inline-flex items-center")

page = pv.Page("PyVibe", navbar=navbar)

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
page.add_link("Interactive Tutorial", "tutorial.html")
page.add_text("")

page.add_header("What is PyVibe?", 3)
page.add_text("PyVibe is a Python library for creating web pages. It is designed to be a quick way for Python developers to build front-ends.")
page.add_text("PyVibe uses a component-based approach to building web pages. This means that you can create a page by combining components together.")

page.add_header("How do I use PyVibe?", 3)
page.add_text("PyVibe is a Python library that simplifies UI development for web apps by providing semantic Python components that compile into HTML and can be used with any web framework.")
page.add_text("Fundamentally, PyVibe returns an HTML string that can be used with:")

page.add_text("TODO: Link to examples for each of these")
with page.add_list() as list:
    list.add_listitem("<b>Static Pages</b>: Like the one you're viewing now", is_checked=True)
    list.add_listitem("<b>Flask</b>: Inside a Flask function", is_checked=True)
    list.add_listitem("<b>Django</b>: ", is_checked=True)
    list.add_listitem("<b>Pyodide</b>: For dynamic client-side rendered pages", is_checked=True)

page.add_text("")

page.add_header("What can you build with PyVibe?", 3)
page.add_text("TODO: Gallery here")

page.add_header("Themes", 3)
page.add_text('PyVibe is meant to be a generic framework. While the default theme uses <a href="https://flowbite.com/" class="font-medium text-blue-600 underline dark:text-blue-500 hover:no-underline">Flowbite</a>, which are components that use <a href="https://tailwindcss.com/" class="font-medium text-blue-600 underline dark:text-blue-500 hover:no-underline">TailwindCSS</a>, we envision including many themes and CSS frameworks in the future.')

page.add_header("How does PyVibe compare to Streamlit, Plotly Dash, Pynecone, Anvil, NiceGUI, etc?", 3)
page.add_text("PyVibe is not a web server -- it produces styled HTML that can be used with any web server.")

page.add_html("""
<script>
  function dismissBanner() {
    document.getElementById('marketing-banner').remove()    
  }
</script>
<div id="marketing-banner" tabindex="-1" class="dark fixed z-50 flex flex-col md:flex-row justify-between w-[calc(100%-2rem)] p-4 -translate-x-1/2 border rounded-lg shadow-sm lg:max-w-7xl left-1/2 bottom-6 bg-gray-700 border-gray-600">
    <div class="flex flex-col items-start mb-3 mr-4 md:items-center md:flex-row md:mb-0">
        <a href="https://pypi.org/project/pyvibe/" class="flex items-center mb-2 border-gray-200 md:pr-4 md:mr-4 md:border-r md:mb-0 dark:border-gray-600">
            <img src="https://cdn.pycob.com/pycob_hex.svg" class="h-6 mr-2" alt="Pycob Logo">
            <span class="self-center text-lg font-semibold whitespace-nowrap dark:text-white">PyVibe</span>
        </a>
        <p class="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">Easily create styled web pages with Python</p>
    </div>
    <div class="flex items-center flex-shrink-0">
      <a href="https://github.com/pycob/pyvibe" type="button" class="text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 flex items-center">
          <svg aria-hidden="true" class="w-5 h-5 text-yellow-400 mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>First star</title><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
      Star on GitHub</a>
        <button onclick="dismissBanner()" data-dismiss-target="#marketing-banner" type="button" class="absolute top-2.5 right-2.5 md:relative md:top-auto md:right-auto flex-shrink-0 inline-flex justify-center items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white">
            <svg aria-hidden="true" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            <span class="sr-only">Close banner</span>
        </button>
    </div>
</div>
    """)