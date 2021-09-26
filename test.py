'''
import datetime

import pandas_datareader.data as web

df_stockload = web.DataReader("300033.SZ","yahoo",datetime.datetime(2019,1,1),datetime.datetime(2019,6,1))
print(df_stockload)
'''
import pandas as pd
import tushare as ts

token = '3b490c6d1a57adc1bcde82ebb5aadfc4176c890f34611d3beec31666'    #输入你的口令
pro = ts.pro_api(token)   #  初始化pro接口
df_gldg = pro.daily(ts_code='000651.SZ',start_date='20090101',end_date='20190601')
print(df_gldg)
df_gldg.index = pd.to_datetime(df_gldg.trade_date)
df_gldg.drop(axis=1,columns='trade_date', inplace=True)
print(df_gldg.head())
df_gldg.sort_index(inplace=True)
print(df_gldg.index)
df_gldg.index = df_gldg.index.set_names('Date')
print(df_gldg.index)