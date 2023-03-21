print("Generating from Python...")
import pyvibe as pv
from os.path import dirname, basename, isfile, join
import glob
from docs.common.components import navbar, footer

modules = glob.glob(join(dirname(__file__)+"/docs", "*.py"))
files = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

for file in files:
    print("Importing file: " + file)
    exec(f"from docs import {file}")

    # exec(f"{file}.page.add_header('Python Source')")
    # exec(f"{file}.page.add_text('This is the source code for the current page.')")
    # exec(f"{file}.page.add_emgithub('https://github.com/pycob/pyvibe/blob/main/generator/docs/{file}.py')")
    # exec(f"{file}.page.add_link('View Source', 'https://github.com/pycob/pyvibe/blob/main/generator/docs/{file}.py')")

    print(f"Writing to {file}.html")
    exec(f"with open('docs/{file}.html', 'w') as f: f.write({file}.page.to_html())")    

gallery_modules = glob.glob(join(dirname(__file__)+"/gallery", "*.py"))
gallery_files = [ basename(f)[:-3] for f in gallery_modules if isfile(f) and not f.endswith('__init__.py')]

for file in gallery_files:
    print("Importing file: " + file)
    exec(f"from gallery import {file}")

    exec(f"{file}.page.add_header('Python Source')")
    exec(f"{file}.page.add_text('This is the source code for the current page.')")
    exec(f"{file}.page.add_emgithub('https://github.com/pycob/pyvibe/blob/main/generator/gallery/{file}.py')")
    exec(f"{file}.page.add_link('View Source', 'https://github.com/pycob/pyvibe/blob/main/generator/gallery/{file}.py')")

    exec(f'pg = pv.Page({file}.page.title, navbar=navbar, components={file}.page.components)')

    print(f"Writing to {file}.html")
    exec(f"with open('docs/gallery/{file}.html', 'w') as f: f.write(pg.to_html())")   