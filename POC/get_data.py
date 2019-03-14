#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:40:24 2019

@author: pascal-baur
"""

from iex_data import Fetcher
from datetime import datetime
import sqlite3
#import talib

tickers = ['AAPL', 'TSLA', 'MSFT', 'AMZN', 'NFLX', 'GOOG'] # TODO: import file with ticker list to download

def run():
    #with open("sp500tickers.pickle", "rb") as f:
    #    tickers = pickle.load(f)
    conn = sqlite3.connect('/Users/pascal-baur/Desktop/grid_search_/main.db')
    try:
        for i in tickers:
            df = Fetcher.get_historical(ticker='{}'.format(i), start=datetime(2014, 1, 1), end=None) 
            # Technical indicators
            #df['EMA30'] = talib.EMA(df['close'], timeperiod=30)
            #df['EMA60'] = talib.EMA(df['close'], timeperiod=60)
            #df['EMA90'] = talib.EMA(df['close'], timeperiod=90)
            #df['CCI']= talib.CCI(df['high'], df['low'], df['close'], timeperiod=14)
            #df['Chande Momentum Oscillator'] = talib.CMO(df['close'], timeperiod=14)
            #df['MACD'] = talib.
            #df['MFI'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=14)
            #df['MOM'] = talib.MOM(df['close'], timeperiod=10)
            #df['DX'] = talib.DX(df['high'], df['low'], df['close'], timeperiod=14)
            #df['MINUS_DI'] = talib.MINUS_DI(df['high'], df['low'], df['close'], timeperiod=14)
            #df['PLUS_DI'] = talib.PLUS_DI(df['high'], df['low'], df['close'], timeperiod=14)
            #df['ADX'] = talib.ADX(df['high'], df['low'], df['close'], timeperiod=14)
            #df['RSI'] = talib.RSI(df['close'], timeperiod=14)
            #df['OBV'] = talib.OBV(df['close'], df['volume'])
            #df['Vol_ATR'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14)
            #df['Vol'] = talib.TRANGE(df['high'], df['low'], df['close'])
            # Save to database
            df.to_sql('{}'.format(i), conn, if_exists='replace', index=True)
    except Exception as e:
        print (e)


if __name__ == "__main__":
    run()