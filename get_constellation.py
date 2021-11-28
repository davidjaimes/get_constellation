from astropy.coordinates import get_sun, get_constellation
from astropy.timeseries import TimeSeries
import numpy as np
import pandas as pd
from astropy.time import Time


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
df = pd.DataFrame({'Date': dates})
times = Time(dates)
df['Sign'] = get_sun(times).get_constellation()
df = df.set_index('Sign')

# Find min and max fo reach sign.
signs = ['Aquarius', 'Pisces', 'Aries', 'Taurus', ]

print(df.loc['Libra'].max())