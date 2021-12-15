import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df = pd.read_csv('data/girls.csv',delimiter=',')
df.insert(0,"event_timestamp", pd.Timestamp(datetime.now(), tz="UTC"))
df['girl_id']=np.arange(len(df))
df.to_parquet('data/girls.parquet')