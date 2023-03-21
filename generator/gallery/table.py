import pyvibe as pv
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")

page = pv.Page("Table Example")

page.add_header("Table Example")

actions = [
    # This button uses the year for the row as a parameter in the URL
    pv.Rowaction("Edit", "#/edit?year={year}", "edit", open_in_new_window=False),
    # This button uses the country for the row as a parameter in the URL
    pv.Rowaction("{iso_alpha}", "#/country?year={year}&country={country}", open_in_new_window=False)
]

page.add_pandastable(df, action_buttons=actions)
