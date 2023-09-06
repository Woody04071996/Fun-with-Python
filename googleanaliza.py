import pandas as pd
import pandas_datareader.data as web

pd.set_option('display.float_format', '{:.2f}'.format)

df = web.DataReader(name='GOOGL', data_source='stooq')
