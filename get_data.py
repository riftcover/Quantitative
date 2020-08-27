import tushare as ts

ts.set_token('c856c3a769c0bb77983e43bba40449c7aeed8429492f1af738c551c3')
pro = ts.pro_api()
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
print(df)