from astropy.coordinates import get_sun, get_constellation
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


ndfs = []
for x in range(1901, 2100):
    # Create DataFrame
    dates = calc_date(x)
    times = Time(dates)
    df = pd.DataFrame({'Date': dates})
    df['Sign'] = get_sun(times).get_constellation()

    # Get month in each entry.
    month = [dt.datetime.strptime(d, '%Y-%m-%d').month for d in dates]
    df['Month'] = month

    # Save special sign in December and Jan.
    w = df['Month'].isin([1])
    jan_uni = df['Sign'][w].unique()
    w = df['Month'].isin([12])
    dec_uni = df['Sign'][w].unique()
    inter = set(jan_uni).intersection(dec_uni)
    special_sign = list(inter)[0]

    # Find special min and max.
    w = (df['Month'] == 12) * (df['Sign'] == special_sign)
    special_min = df['Date'][w].min()
    w = (df['Month'] == 1) * (df['Sign'] == special_sign)
    special_max = df['Date'][w].max()

    # Create new dataframe.
    df = df.set_index('Sign')
    signs = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo',
        'Virgo', 'Libra', 'Scorpius', 'Ophiucus', 'Sagittarius', 'Capricornus']
    min_val = []
    max_val = []
    for s in signs:
        min_val.append(df.loc[s].min().values[0])
        max_val.append(df.loc[s].max().values[0])

    ndf = pd.DataFrame({
        'Constellation': signs,
        'From': min_val,
        'To': max_val
        })

    # Enter special min and special max in new data frame.
    w = ndf['Constellation'] == special_sign
    ndf.loc[w, 'From'] = special_min
    ndf.loc[w, 'To'] = special_max
    ndfs.append(ndf)

ndf = pd.concat(ndfs)
ndf.to_csv('zodiac_sign.csv', index=False)
ndf = ndf.reset_index()
ndf.to_json('zodiac.json')