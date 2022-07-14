from binance.client import Client
import pandas as pd
import mplfinance as mpf
api_key = ''
api_secret = '' 
client = Client(api_key, api_secret)
infos = client.get_all_tickers()
for i in infos:
    print(i)
infos_df = pd.DataFrame(infos)
print(infos_df)
historical = client.get_historical_klines('ETHBTC', client.KLINE_INTERVAL_1DAY, '20 Jun 2022')
hist_df = pd.DataFrame(historical)
hist_df.columns = ['Open Time', 'Open', 'Hight', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'Tb Quote Volume', 'Ignore']
hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time']/1000, unit='s')
print(hist_df.head)
mpf.plot(hist_df.set_index('Close Time').tail(100))
