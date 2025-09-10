from pathlib import Path

import pandas
import re
import numpy as np
import plotly.express as px
from shiny.express import render, input, ui
from shinywidgets import render_plotly
from shiny import reactive

@reactive.calc
def dat():
    infile = Path(__file__).parent / "gm_pop.csv"
    return pandas.read_csv(infile, sep=";")

def gapminder():
    return px.data.gapminder()



ui.page_opts(title="Valtion statistiikka", fillable=False)

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
        infile = Path(__file__).parent / "gm_pop.csv"
        df = pandas.read_csv(infile, sep=";")
        dff = df[df["name"] == input.country()]
        year_columns = [row for row in dff if re.fullmatch(r"\d{4}", row)]
        df_long = dff.melt(
            id_vars=["geo", "name"],   # nämä pysyvät riveillä
            value_vars=year_columns,   # nämä sarakkeet muutetaan riveiksi
            var_name="year", 
            value_name="population"
        )
        return px.scatter(df_long, x=year_columns, y="population", title=f"{input.country()} - Väestönmäärä")

    @render_plotly
    def plot3():
        dff = gapminder()[gapminder()["country"] == input.country()]
        return px.line(dff, x="year", y="lifeExp", title=f"{input.country()} - Eliniän odote")

#    @render_plotly
#    def plot4():
#        return px.choropleth(dat(), locations="iso_alpha", color="lifeExp",
#                      hover_name="country")

with ui.navset_card_underline():

    with ui.nav_panel("Data frame"):

        @render.data_frame
        def frame():
            infile = Path(__file__).parent / "gm_pop.csv"
            df = pandas.read_csv(infile, sep=";")
            dff = df[df["name"] == input.country()]
            year_columns = [row for row in dff if re.fullmatch(r"\d{4}", row)]
            # Give dat() to render.DataGrid to customize the grid
            # print(year_columns)
            return pandas.DataFrame(dff)

    with ui.nav_panel("Table"):

        @render.table
        def table():
            return dat()
