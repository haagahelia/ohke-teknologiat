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

ui.page_opts(title="Filling layout", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(dat(), y="mpg")

    @render_plotly
    def plot2():
        return px.histogram(dat(), y="qsec")


with ui.navset_card_underline():

    with ui.nav_panel("Data frame"):

        @render.data_frame
        def frame():
            # Give dat() to render.DataGrid to customize the grid
            return dat()

    with ui.nav_panel("Table"):

        @render.table
        def table():
            return dat()
