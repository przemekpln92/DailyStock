from pandas_datareader import data, get_nasdaq_symbols
import pandas as pd
from datetime import datetime, timedelta

def dia():
    end = datetime.now()
    start = end - timedelta(days=5)
    df = data.DataReader(name="DIA", data_source="iex", start=start, end=None)
    lenght = len(df.index)
    close = round(df["close"][lenght -1],2)
    previous_close = df["close"][lenght - 2]
    symbols = get_nasdaq_symbols()
    security_name = (symbols.loc["DIA"])
    return close, previous_close, security_name

def spy():
    end = datetime.now()
    start = end - timedelta(days=5)
    df = data.DataReader(name="SPY", data_source="iex", start=start, end=None)
    lenght = len(df.index)
    close = round(df["close"][lenght -1],2)
    previous_close = df["close"][lenght - 2]
    symbols = get_nasdaq_symbols()
    security_name = (symbols.loc["SPY"])
    return close, previous_close, security_name

def iwm():
    end = datetime.now()
    start = end - timedelta(days=5)
    df = data.DataReader(name="IWM", data_source="iex", start=start, end=None)
    lenght = len(df.index)
    close = round(df["close"][lenght -1],2)
    previous_close = df["close"][lenght - 2]
    symbols = get_nasdaq_symbols()
    security_name = (symbols.loc["IWM"])
    return close, previous_close, security_name

def jpxn():
    end = datetime.now()
    start = end - timedelta(days=5)
    df = data.DataReader(name="JPXN", data_source="iex", start=start, end=None)
    lenght = len(df.index)
    close = round(df["close"][lenght -1],2)
    previous_close = df["close"][lenght - 2]
    symbols = get_nasdaq_symbols()
    security_name = (symbols.loc["JPXN"])
    return close, previous_close, security_name