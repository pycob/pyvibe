print("Generating from Python...")

from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__)+"/docs", "*.py"))
files = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

for file in files:
    print("Importing file: " + file)
    exec(f"from docs import {file}")

    print(f"Writing to {file}.html")
    exec(f"with open('docs/{file}.html', 'w') as f: f.write({file}.page.to_html())")    

breakpoint()