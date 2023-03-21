import pyvibe as pv
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")

page = pv.Page("Chart Example")

page.add_header("Chart Example")

fig = px.bar(df, x='year', y='pop')

page.add_plotlyfigure(fig)