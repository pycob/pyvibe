import pyvibe as pv

page = pv.Page("Form Example")


# Here we put the form inside a card so it is easier to see.
with page.add_card() as card:
    card.add_header("Form Example")

    with card.add_form() as form:
        form.add_formtext(label="Name", name="name", placeholder="Enter your name")
        form.add_formemail(label="Email", name="email", placeholder="Enter your email")
        form.add_formpassword(label="Password", name="password", placeholder="Enter your password")
        form.add_formtextarea(label="Message", name="message", placeholder="Enter your message")
        form.add_formsubmit(label="Send")
