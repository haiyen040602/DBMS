import pandas as pd
import numpy as np 
from datetime import datetime, timezone
import random

measurement = []
location_df = pd.read_csv('data/location.csv')
location = location_df['location'].to_list()
idx = []
humidity = []
wind_speed = []
mean_pressure = []
date_time = []

for j in range(10000000):
    measurement.append("humidity2010")
    idx.append(str(j))
    date_time.append(datetime.now(timezone.utc).astimezone().isoformat())
    location.append(random.choice(location)) 
    humidity.append(np.random.uniform(0,50))
df = pd.DataFrame(zip(measurement, idx, date_time, location, humidity), columns=['measurement','idx', 'date_time', 'location', 'humidity'])
df.to_csv('csv/humidity20109.csv', index=False)

#datatype measurement,tag,dateTime:RFC3339,string,double
