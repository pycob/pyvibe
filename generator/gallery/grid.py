import pyvibe as pv
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
df = df.sort_values(by="year")

page = pv.Page("Grid Example")

page.add_header("Grid Example")

with page.add_container(grid_columns=2) as container:
    container.add_plotlyfigure(px.bar(df, x='year', y='pop'))
    container.add_plotlyfigure(px.line(df, x='year', y='lifeExp'))
    container.add_plotlyfigure(px.bar(df, x='year', y='gdpPercap'))
    container.add_plotlyfigure(px.bar(df, x='year', y='pop'))