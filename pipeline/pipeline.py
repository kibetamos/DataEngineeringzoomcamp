import sys

import pandas as pd

print('arguments', sys.argv)



df = pd.DataFrame({"day": [1, 2], "number_passengers": [3, 4]})
month = int(sys.argv[1])

print("Hello Pipeline")

print(f'hello pipeline, month= {month}')

print(df.head())

df.to_parquet(f'outut_{month}.parquet')