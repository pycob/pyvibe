import pyvibe as pv
from .common.components import navbar, footer, marketing_banner, gallery_grid, all_layouts

page = pv.Page("Gallery", navbar=navbar, footer=None)
page.add_header("Gallery")

page.add_text("Here are some examples of what you can create with PyVibe.")

page.add_component(gallery_grid(all_layouts))

page.add_text("PyVibe was spun out of Pycob. We are in the process of transitioning Pycob apps to PyVibe.")
page.add_link("See additional examples on Pycob", "https://www.pycob.com/gallery?tag=Featured")
page.add_text("Note: Some of the examples on Pycob are not yet compatible with PyVibe but should give you some examples of the layout possibilities.")