import pyvibe as pv

page = pv.Page("Gallery")

page.add_header("Gallery")
page.add_text("Here are some examples of what you can create with PyVibe.")

page.add_header("Basic", 2)

with page.add_card() as card:
    card.add_header("Basic Card")
    card.add_text("This is a basic card.")
    card.add_link("Learn more", "https://pycob.com")

page.add_header("Advanced", 2)

with page.add_card() as card:
    card.add_header("Advanced Card")
    card.add_text("This is an advanced card.")
    card.add_link("Learn more", "https://pycob.com")
    card.add_image("https://cdn.pycob.com/pyvibe.svg", 'logo', classes='w-1/2')
    card.add_text("You can add images, text, and links to cards.")

page.add_header("Grid", 2)

with page.add_container(grid_columns=2) as container:
    with container.add_card() as card:
        card.add_header("Card 1")
        card.add_text("This is card 1.")
        card.add_link("Learn more", "https://pycob.com")
    with container.add_card() as card:
        card.add_header("Card 2")
        card.add_text("This is card 2.")
        card.add_link("Learn more", "https://pycob.com")
    with container.add_card() as card:
        card.add_header("Card 3")
        card.add_text("This is card 3.")
        card.add_link("Learn more", "https://pycob.com")
    with container.add_card() as card:
        card.add_header("Card 4")
        card.add_text("This is card 4.")
        card.add_link("Learn more", "https://pycob.com")


