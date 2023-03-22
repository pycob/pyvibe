import pyvibe as pv
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

class WebSocketReceiverComponent(pv.Component):
    def __init__(self, path_to_websocket: str):    
        self.path_to_websocket = path_to_websocket

    def to_html(self):
        return """
        <div id="log"></div>
        <script>
            var httpProtocol = 'http://'; 
            var wsProtocol = 'ws://';
            if (window.location.protocol === 'https:') {
                httpProtocol = 'http://';
                wsProtocol = 'wss://';
            }

            const log = (text, color) => {
                document.getElementById('log').innerHTML += `<span style="color: ${color}">${text}</span><br>`;
            };

            const socket = new WebSocket(wsProtocol + location.host + '""" + self.path_to_websocket + """');
            socket.addEventListener('message', ev => {
                document.getElementById('log').innerHTML += ev.data;
            });
        </script>
        """
 
class WebSocketSenderComponent(pv.Component):
    def __init__(self, path_to_websocket: str):    
        self.path_to_websocket = path_to_websocket

    def to_html(self):
        return """
        <form class="max-w-full" style="width: 500px" onsubmit="event.preventDefault(); sendWebsocket(this)" action="?" method="GET">
            <div class="mb-6">
                <label for="text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Input</label>
                <input type="text" name="text" value="" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required="">
            </div>
            <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Send</button> 
        </form>
        <script>
            function sendWebsocket(form) {
                const textField = form.text;
                socket.send(textField.value);
                textField.value = '';
                return false;
            }
        </script>
        """

@app.route('/')
def index():
    page = pv.Page('Websocket Test', description='WebSocket proof of concept using Flask-Sock and PyVibe')

    page.add_header("Websocket Test")

    with page.add_container(grid_columns=2) as container:
        with container.add_card() as card:
            card.add_header('Send')
            card.add_component(WebSocketSenderComponent('/echo'))
        
        with container.add_card() as card:
            card.add_header('Receive')
            card.add_component(WebSocketReceiverComponent('/echo'))

    page.add_header("Source Code")
    page.add_emgithub("https://github.com/pycob/pyvibe/blob/main/sample-apps/websockets/main.py")

    return page.to_html()

from threading import Timer

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()

        alert_component = pv.AlertComponent(data, 'Received')

        sock.send(alert_component.to_html())

if __name__ == '__main__':
    app.run(debug=True)