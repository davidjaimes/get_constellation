from astropy.coordinates import get_sun, get_constellation
from astropy.timeseries import TimeSeries
import numpy as np
import pandas as pd


# Create datetimes array.
dates = [f'{x+1678}/12/16' for x in range(584)]

# Prepare Data Frame
df = pd.DataFrame()
df['a'] = np.arange(1, len(dates) + 1, 1)
df.set_index(pd.DatetimeIndex(dates), inplace=True)

# Turn from pandas to astropy time.
ts = TimeSeries.from_pandas(df)

# New DF
ndf = pd.DataFrame({
    'Date': ts['time'],
    'Zign': get_sun(ts['time']).get_constellation()
    })

print(ndf)