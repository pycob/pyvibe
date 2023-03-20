import pyvibe as pv

page = pv.Page('Interactive PyVibe Tutorial')

page.add_header("Welcome to the PyVibe Tutorial!")
page.add_text("This is a work in progress.")

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

        document.getElementById("results").innerHTML = results;

        document.getElementById("runButton").innerHTML = runButton;
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

page.add_text("TODO: Tutorial here")

page.add_header("Page")

page.add_header("Dataframes")

page.add_header("Charts")

page.add_header("Tables")

page.add_header("Forms")

page.add_header("Serving from Flask")

