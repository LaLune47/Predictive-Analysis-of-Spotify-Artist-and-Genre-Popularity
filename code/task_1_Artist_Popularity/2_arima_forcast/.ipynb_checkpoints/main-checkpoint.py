import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
# 加载数据
data = pd.read_csv('Spotify_Dataset_V3.csv', delimiter=';')

# 确保日期字段是datetime类型，日期格式是DD/MM/YYYY
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# 先按日期倒序，再按Rank正序排序
sorted_data = data.sort_values(by=['Date', 'Rank'], ascending=[False, True])

# 保存排序后的数据到新的CSV文件
sorted_data.to_csv('sorted.csv', index=False, sep=';')

# data = sorted_data
# artist_data = data[data['Artist'] == 'Example Artist']
# print(artist_data)