import pyvibe as pv
from .common.components import navbar, footer, marketing_banner

page = pv.Page("Flask", navbar=navbar, footer=footer)

page.add_header("Flask")


page.add_text("PyVibe can be used with Flask. This is a simple example of how to use PyVibe with Flask.")

page.add_text("First, create a new file called <code>app.py</code> and add the following code:")

page.add_code("""from flask import Flask
import pyvibe as pv

app = Flask(__name__)

@app.route('/')
def index():
    page = pv.Page('Home')
    page.add_header('Hello World')
    return page.to_html()

if __name__ == '__main__':
    app.run(debug=True)
""", prefix="")

page.add_text("Then, run the following command in your terminal:")
page.add_code("python app.py", prefix="%")

page.add_html(marketing_banner)