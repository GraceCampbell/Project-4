#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Functions
def make_datetime(df):
    if len(df) < 75:
        df.index = pd.date_range('2001', '2018', freq='MS')
    else:
        df.index = pd.date_range('2000-01', '2017-09', freq='MS')
    
def monthly(df, county=None):
    a = []
    if county != None:
        m = df.loc[df['county'] == county, ['month_1', 'month_2', 'month_3']].T
    else:
        m = df[['month_1', 'month_2', 'month_3']].T
    for col in m.columns:
        for each in m[col]:
            a.append(each)
    new_df = pd.DataFrame(a, columns=['employment'])
    make_datetime(new_df)
    return new_df

def plot_acf_pacf(df, lags, time_range, county_name=None):
    fig, axes = plt.subplots(2, figsize=(14, 12))

    plot_acf(df, lags=lags, ax=axes[0])
    axes[0].set_title(f'Autocorrelation Function  -  {time_range}\n{county_name}', size=20)
    axes[0].set_xlabel('Time', size=15)
    axes[0].set_ylabel('Correlation', size=15)

    plot_pacf(df, lags=lags, ax=axes[1])
    axes[1].set_title(f'Partial Autocorrelation Function  -  {time_range}\n{county_name}', size=20)
    axes[1].set_xlabel('Time', size=15)
    axes[1].set_ylabel('Correlation', size=15)

    plt.subplots_adjust(hspace=.4);

def plot_preds(df, preds_post_df, county_name, measure):
    plt.figure(figsize=(15, 10))
    plt.plot(df, c='#6ea4c1', label='Actual')
    plt.plot(preds_post_df, c='#bc006d', label='Predicted')
    plt.xlabel('Time', size=15)
    plt.ylabel(measure, size=15)
    plt.legend(loc='upper left', fontsize=13)
    plt.title(f'Predicted vs. Actual {measure}:\n{county_name}', size=25);

