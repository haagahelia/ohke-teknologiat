from pathlib import Path

import pandas
import numpy as np
import plotly.express as px
from shiny.express import render, input, ui
from shinywidgets import render_plotly
from shiny import reactive

@reactive.calc
def dat():
    infile = Path(__file__).parent / "mtcars.csv"
    return pandas.read_csv(infile)

def gapminder():
    return px.data.gapminder()



ui.page_opts(title="Filling layout", fillable=True)

ui.input_select(
    "country",
    "Valitse maa:",
    choices=sorted(gapminder()["country"].unique()),
    selected="Finland"
)


with ui.layout_columns():
    @render_plotly
    def plot1():
        dff = gapminder()[gapminder()["country"] == input.country()]
        return px.line(dff, x="year", y="gdpPercap", title=f"{input.country()} - BKT/asukas")
    
    @render_plotly
    def plot2():
        dff = gapminder()[gapminder()["country"] == input.country()]
        return px.scatter(dff, x="year", y="pop", title=f"{input.country()} - Väestönmäärä")

    @render_plotly
    def plot3():
        dff = gapminder()[gapminder()["country"] == input.country()]
        return px.line(dff, x="year", y="lifeExp", title=f"{input.country()} - Eliniän odote")



with ui.navset_card_underline():

    with ui.nav_panel("Data frame"):

        @render.data_frame
        def frame():
            # Give dat() to render.DataGrid to customize the grid
            return gapminder()

    with ui.nav_panel("Table"):

        @render.table
        def table():
            return gapminder()