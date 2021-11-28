from astropy.coordinates import get_sun, get_constellation
from astropy.timeseries import TimeSeries
import numpy as np
import pandas as pd
from astropy.time import Time


# Create datetimes array.
times = [f'{x:04d}-06-16' for x in range(0, 5001, 500)]

# Prepare Data Frame
t = Time(times)
df = pd.DataFrame({
    'Date': t,
    'Zign': get_sun(t).get_constellation()
    })

print(df)