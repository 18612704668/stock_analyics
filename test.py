'''
import datetime

import pandas_datareader.data as web

df_stockload = web.DataReader("300033.SZ","yahoo",datetime.datetime(2019,1,1),datetime.datetime(2019,6,1))
print(df_stockload)
'''
import pandas as pd

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

recon_data = {'Open': df_gldg.open,'Close': df_gldg.close,'High': df_gldg.high,'Low': df_gldg.low,'Volume': df_gldg.vol}
df_recon = pd.DataFrame(recon_data)
print(df_recon.columns)

'''
'''
#定制股票行情数据获取接口(基于Tushare Pro 的daily()接口)
def pro_daily_stock(code_val='000651.sz',start_val='20090101',end_val='20190601');
#  获取股票日线行情数据
    df_stock = pro.daily(ts_code=code_val,start_date=start_val,end_date=end_val)
    df_stock.trade_date = pd.DatetimeIndex(df_stock.trade_date)
    df_stock.set.index("trade_date",drop=True,inplace=True)
    df_stock.sort.index(inplace=True)
    df_stock.index = df_stock.index.set_name('Date')

    recon_data = {'Open': df_stock.open,'Close': df_stock.close,'High': df_stock.high,'Low': df_stock.low,'Volume': df_stock.vol}
    df_recon = pd.DataFrame(recon_data)
    return df_recon

#定制股票行情数据获取接口(基于Baostock 的query_history_k_data_plus()接口)
def bs_k_data_stock(code_val='000651.sz',start_val='20090101',end_val='20190601',adjust_val='3');
    lg = bs.login()
    field= "data,open,high,low,close,volume"
    df_bs = bs.query_history_k_data(code_val, fields, start_data=start_val, end_data=end_val, frequency=freq_val, adjustflag=adjust_val)
    #   <class'baostock.data.resultset.ResultData'>
    #   frequency="d"取日K线,adjustflag="3"默认不复权，1：后复权；2：前复权
    data_list = []
    while (df_bs.error_code =='0' )& (df_bs.next):
        # 获取第一条记录，讲记录合并在一起
        data_list.append(df_bs.get_row_data())
    result = pd.DataFrame(data.list, columns=df_bs.fields)

    result.close = result.close.astype('float64')
    result.open = result.open.astype('float64')
    result.low = result.low.astype('float64')
    result.high = result.high.astype('float64')
    result.volume = result.volume.astype('float64')
    result.volume = result.volume/100 #单位转化，股换手
    result.date = pd.DatetimeIndex(result.date)
    result.index = result.index.set_names('Date')

    recon_data = {'High':result.high, 'Low':result.low,'Open':result.open,'Close':result.close,'Volume':result.volume}
    df_recon = pd.DataFrame(recon_data)

    #退出系统
    bs.logout()
    return df_recon
'''
import json
stock_index = [{'指数':
                {'上证指数':'sh.000001',
                 '深证指数':'sz.399001',
                 '沪深300':'sz.000300',
                 '创业指数':'sz.399006',
                 '上证50':'sh.000016',
                 '中证500':'sh.000905',
                 '中小板指':'sz.399005',
                 '上涨180':'sh.000010',}},
               {'股票':
                {'格力电器':'000651.SZ',
                 '平安银行':'000001.SZ',
                 '同花顺':'300033.SZ',
                 '贵州茅台':'600519.SH',
                 '浙大网新':'600797.SH'} }]
print(stock_index)
print(type(stock_index))

json_str = json.dumps(stock_index)
print(json_str)
print(type(json_str))

with open("stock_pool.json","w",encoding='utf-8') as f:
    json.dump(stock_index,f,ensure_ascii=False,indent=4)