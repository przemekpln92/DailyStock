import datetime
from pandas_datareader import data, get_nasdaq_symbols
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.embed import components
from bokeh.resources import CDN


def candle_stick(ticker_and_date,start_date):

    def get_security_name(ticker):
        symbols = get_nasdaq_symbols()
        security_name = (symbols.loc[ticker])
        return security_name

    # Defining date range
    start = datetime.datetime(start_date[0],start_date[1],start_date[2])
    # Data Frame source
    df = data.DataReader(name=ticker_and_date, data_source="iex", start=start, end=None)


    # Converting date to 'datetime64[ns]' type
    df.index = pd.to_datetime(df.index)
    # Half day in ms
    w = 12 * 60 * 60 * 1000

    # Getting official security common name
    security_name = get_security_name(ticker_and_date)

    # Stick distinction
    increas = df.close > df.open
    decreas = df.open > df.close

    # Data source for stick where close price > open price
    source = ColumnDataSource(data={
        'date':  df.index[increas],
        'close': df.close[increas],
        'open':  df.open[increas],
        'high':  df.high[increas],
        'low':   df.low[increas],
    })

    # Data source for stick where close price < open price
    source_two = ColumnDataSource(data={
        'date':  df.index[decreas],
        'close': df.close[decreas],
        'open':  df.open[decreas],
        'high':  df.high[decreas],
        'low':   df.low[decreas],
    })

    # Responsive chart figure and grid size
    p = figure(x_axis_type="datetime", height=120, width=280, title=security_name[1], sizing_mode="scale_width")
    p.grid.grid_line_alpha = 0.8

    # Description of the x and y axes
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Price'

    # Thick segment for stick where close price > open price
    p.segment("date", "high", 'date', 'low', color="black", source=source)

    # Thick segment for stick where close price < open price
    p.segment("date", "high", 'date', 'low', color="black", source=source_two)

    # Stick where close price > open price
    p.vbar(x="date", top="open", bottom="close", width=w, fill_color="#D5E1DD", line_color="black", source=source)

    # Stick where close price < open price
    p.vbar(x="date", top="open", bottom="close", width=w, fill_color="#F2583E", line_color="black", source=source_two)

    # Mouse over the stick tools and formatters
    p.add_tools(HoverTool(
        tooltips=[
            ('date',  '@date{%F}'),
            ('open',  '@open'),
            ('high',  '@high'),
            ('low',   '@low'),
            ('close', '@close'),
        ],

        formatters={
            'date':   'datetime',  # Formatting date to datetime type
        },
        mode='vline'  # Display a tooltip
    ))

    script_candle, div_candle = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return script_candle,div_candle,cdn_js,cdn_css