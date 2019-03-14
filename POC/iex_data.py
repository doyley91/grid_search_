#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:53:05 2019

@author: pascal-baur
"""

from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
from datetime import datetime
import datetime as dt
import calendar as cal
import time


class Fetcher(object):
    
    def __init__(self, ticker, start, end=None):
        self.ticker = ticker.upper()
        self.start = int(cal.timegm(dt.datetime(*start).timetuple()))
        
        if end is not None:
            self.end = int(cal.timegm(dt.datetime(*end).timetuple()))
        else:
            self.end = int(time.time())
        
    def get_historical(ticker, start, end):
        return get_historical_data(ticker, start, end, output_format='pandas')