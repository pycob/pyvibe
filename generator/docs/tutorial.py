import pyvibe as pv
from .common.components import navbar, footer

page = pv.Page('Interactive PyVibe Tutorial', navbar=navbar, footer=footer)

page.add_header("Welcome to the PyVibe Tutorial!")
page.add_text("This is a work in progress.")

page.add_html("""

<ul class="flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400">
    <li class="mr-2">
        <button aria-current="page" class="inline-block p-4 text-blue-600 bg-gray-100 rounded-t-lg active dark:bg-gray-800 dark:text-blue-500">Card</a>
    </li>
    <li class="mr-2">
        <button class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Charts</a>
    </li>
    <li class="mr-2">
        <button class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Tables</a>
    </li>
    <li class="mr-2">
        <button class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Forms</a>
    </li>
</ul>

""")

page.add_codeeditor("""with page.add_card() as card:
    card.add_header("Hello World")
    card.add_text("This content was generated with Python (from the browser)!")
""")

page.add_html("""
    <script src="https://cdn.jsdelivr.net/pyodide/v0.22.1/full/pyodide.js"></script>  
    <script defer type="text/javascript">
    var loadingButton = `
        <button disabled class="relative inline-flex items-center justify-center p-0.5 mb-2 mr-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-pink-500 to-orange-400 group-hover:from-pink-500 group-hover:to-orange-400 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800">
            <span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
                Running...
            </span>
        </button>`

    var runButton = `
        <button onclick="runCode()" class="relative inline-flex items-center justify-center p-0.5 mb-2 mr-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-pink-500 to-orange-400 group-hover:from-pink-500 group-hover:to-orange-400 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800">
            <span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
                Run
            </span>
        </button>`  

      var pyodide;

      async function main(){
        pyodide = await loadPyodide();
        await pyodide.loadPackage("micropip");
        const micropip = pyodide.pyimport("micropip");
        await micropip.install("pyvibe");
        await micropip.install("plotly");
        await micropip.install("pandas");

        pyodide.runPython(`import pagebuilder as pv`);        
        
        document.getElementById("runButton").innerHTML = runButton;
      }
      main();

      function runCode() {
        document.getElementById("results").innerHTML = loadingButton;
        pyodide.runPython(`page = pv.ContainerComponent()`);
        pyodide.runPython(editor.getValue());

        pyodide.runPython(`results = page.to_html()`);

        results = pyodide.globals.get("results");

        // document.getElementById("results").innerHTML = results;
        setInnerHTML(document.getElementById("results"), results);

        document.getElementById("runButton").innerHTML = runButton;

        document.getElementById("results").scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"})
      }
      
      function setInnerHTML(elm, html) {
  elm.innerHTML = html;
  
  Array.from(elm.querySelectorAll("script"))
    .forEach( oldScriptEl => {
      const newScriptEl = document.createElement("script");
      
      Array.from(oldScriptEl.attributes).forEach( attr => {
        newScriptEl.setAttribute(attr.name, attr.value) 
      });
      
      const scriptText = document.createTextNode(oldScriptEl.innerHTML);
      newScriptEl.appendChild(scriptText);
      
      oldScriptEl.parentNode.replaceChild(newScriptEl, oldScriptEl);
  });
}

    </script>
""")
              
page.add_html("""<span id="runButton">
<button disabled class="relative inline-flex items-center justify-center p-0.5 mb-2 mr-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-pink-500 to-orange-400 group-hover:from-pink-500 group-hover:to-orange-400 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800">
            <span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
                Preparing Pyodide...
            </span>
        </button>
</span>""")

page.add_html("<div id='results' class='border-dashed border-2 border-sky-500'></div>")

page.add_link("Learn how to serve from Flask", "flask.html")
