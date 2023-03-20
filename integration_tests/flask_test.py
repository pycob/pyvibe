from flask import Flask
import pyvibe as pv

app = Flask(__name__)

@app.route('/')
def index():
    page = pv.Page('Home')
    page.add_header('Hello World')
    return page.to_html()

if __name__ == '__main__':
    app.run(debug=True)