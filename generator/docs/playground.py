import pyvibe as pv
from .common.components import navbar, footer

page = pv.Page('Interactive PyVibe Playground', navbar=navbar, footer=footer)

page.add_header("Welcome to the PyVibe Playground!")
page.add_text("This playground uses Pyodide to run Python code in the browser. You can use it to experiment with PyVibe and learn how to use it. Note that this is experimental and may not work in all browsers.")

page.add_code("pip install pyvibe", header="Install PyVibe to run locally", prefix="%")

page.add_html("""
<script>
code_samples = {
    "Card": `
with page.add_card() as card:
    card.add_header("Hello World")
    card.add_text("This content was generated with Python (from the browser)!")
`,
    "Charts": `
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})
fig = px.line(df, x="First Column", y="Second Column", title='Sample Chart')

page.add_plotlyfigure(fig)
`,
    "Tables": `
import pandas as pd

df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})

page.add_pandastable(df)
`,
    "Forms": `
with page.add_card() as card:
    card.add_header("This is a form")
    with card.add_form() as form:
        form.add_formtext("Name", "name")
        form.add_formemail("Email", "email")
        form.add_formtextarea("Message", "message")
        form.add_formselect("Options", "options", ["Option 1", "Option 2"])
        form.add_formsubmit("Send!")
`,
}

e = "hi"
function setTab(el) {
    e = el;
    // Set all tabs to inactive
    document.querySelectorAll('#tablist button').forEach(function(el) {
        el.classList = "inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300"
    })

    el.classList = "inline-block p-4 rounded-t-lg text-blue-600 bg-gray-100 active dark:bg-gray-800 dark:text-blue-500";

    editor.setValue(code_samples[e.innerHTML.trim()], -1);
}
</script>
<ul id='tablist' class="flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400">
    <li class="mr-2">
        <button onclick="setTab(this)" aria-current="page" class="inline-block p-4 rounded-t-lg text-blue-600 bg-gray-100 active dark:bg-gray-800 dark:text-blue-500">Card</a>
    </li>
    <li class="mr-2">
        <button onclick="setTab(this)" class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Charts</a>
    </li>
    <li class="mr-2">
        <button onclick="setTab(this)" class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Tables</a>
    </li>
    <li class="mr-2">
        <button onclick="setTab(this)" class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Forms</a>
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
        document.getElementById("runButton").innerHTML = loadingButton;
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
                <svg aria-hidden="true" role="status" class="inline w-4 h-4 mr-3 text-gray-200 animate-spin dark:text-gray-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="#1C64F2"/>
                </svg>
                Preparing Pyodide...
            </span>
        </button>
</span>""")

page.add_html("<div id='results' class='border-dashed border-2 border-sky-500'>A preview will appear here once you click run.</div>")

page.add_link("Learn how to serve from Flask", "flask.html")
