from astropy.coordinates import get_sun, get_constellation
from astropy.timeseries import TimeSeries
import numpy as np
import pandas as pd
from astropy.time import Time
import datetime as dt


# Gregorian Days of the Year
def calc_date(year):
    dates = []
    for x in range(1, 13, 1):
        for y in range(1, 32, 1):
            if x == 2:
                if year % 4 != 0:
                    if y > 28: continue
                else:
                    if y > 29: continue
                dates.append(f'{year:04d}-{x:02d}-{y:02d}')

            elif x in [4, 6, 9, 11]:
                if y > 30: continue
                dates.append(f'{year:04d}-{x:02d}-{y:02d}')

            else:
                dates.append(f'{year:04d}-{x:02d}-{y:02d}')
    return dates

# Create DataFrame
dates = calc_date(1986)
times = Time(dates)
df = pd.DataFrame({'Date': dates})
df['Sign'] = get_sun(times).get_constellation()

# Get month in each entry.
month = [dt.datetime.strptime(d, '%Y-%m-%d').month for d in dates]
df['Month'] = month

# Find min/max in December/Jan.
w = df['Month'].isin([1])
jan_uni = df['Sign'][w].unique()
w = df['Month'].isin([12])
dec_uni = df['Sign'][w].unique()

inter = set(jan_uni).intersection(dec_uni)

print(list(inter)[0])