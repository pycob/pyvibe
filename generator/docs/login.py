import pyvibe as pv
from .common.components import navbar, footer

page = pv.Page("Login", navbar=navbar, footer=footer)

page.add_header("Login")
page.add_text("You can create your own login forms or link to third-party auth providers")