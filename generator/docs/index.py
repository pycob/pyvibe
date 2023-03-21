import pyvibe as pv
from .common.components import footer, marketing_banner, gallery_grid, featured_layouts

page = pv.Page("PyVibe: Easily create styled web pages with Python", navbar=None, footer=footer, image="./img/social.png")

container_outer = page.add_container(grid_columns=2)

container_inner1 = container_outer.add_container(classes="text-center")
container_inner1.add_header("<span class='gradient-text'>PyVibe</span>", size=9)
container_inner1.add_image("https://cdn.pycob.com/pyvibe.svg", 'logo', classes='w-1/2 mx-auto')
container_inner1.add_header("Easily create styled web pages with <span class='gradient-text'>Python</span>")
container_inner1.add_link("Learn more", "about.html")

container_inner2 = container_outer.add_container()
container_inner2.add_code("""import pyvibe as pv

page = pv.Page()

page.add_header("Welcome to PyVibe!")

page.add_text("PyVibe is an open source Python library for creating UI components for web apps without the need to write HTML code.")
""", prefix="", header="Example")

with container_inner2.add_card() as card:
    card.add_header("Welcome to PyVibe!")
    card.add_text("PyVibe is an open source Python library for creating UI components for web apps without the need to write HTML code.")

page.add_header("Examples", 2)
page.add_component(gallery_grid(featured_layouts))

page.add_html(marketing_banner)