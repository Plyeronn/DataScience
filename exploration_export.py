# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# from google.colab import files
# import io
# import glob


# %%
# df_main_ar = [pd.read_csv(io.BytesIO(uploaded[d])) for d in uploaded]
# path = r'./data' # use your path
# all_files = glob.glob(path + "/*.csv")

# li = {}
# li = []
# for filename in all_files:
#     df = pd.read_csv(filename, index_col=None, header=0)
#     name = filename.split("/")[2][7:-4]
#     # li[name] = (df)
#     li.append(df)

AddressCount = pd.read_csv("./data/export-AddressCount.csv", index_col=None, header=0)
DAU = pd.read_csv("./data/export-DailyActiveEthAddress.csv", index_col=None, header=0)
MarCap = pd.read_csv("./data/export-MarketCap.csv", index_col=None, header=0)
NetHash = pd.read_csv("./data/export-NetworkHash.csv", index_col=None, header=0)
DailyTx = pd.read_csv("./data/export-TxGrowth.csv", index_col=None, header=0)
Fees = pd.read_csv("./data/export-TransactionFee.csv", index_col=None, header=0)
AVGFee = pd.read_csv("./data/export-AverageDailyTransactionFee.csv", index_col=None, header=0)

AddressCount = AddressCount.rename(columns={"Value":"AddressCount"})
NetHash = NetHash.rename(columns={"Value":"NetHash"})
DailyTx = DailyTx.rename(columns={"Value":"DailyTx"})
Fees = Fees.rename(columns={"Value":"Fees"})

DAU.drop('Date(UTC)',axis = 1, inplace = True)
AVGFee.drop('Date(UTC)',axis = 1, inplace = True)
AVGFee.drop('UnixTimeStamp',axis = 1, inplace = True)
AVGFee.drop('DateTime',axis = 1, inplace = True)

frame = pd.concat([AddressCount, DAU,MarCap, NetHash, DailyTx, AVGFee], axis=1)
# frame.rename(columns={frame.columns[3]:'Drop'}, inplace=True)
frame = frame.T.drop_duplicates().T

frame['Date(UTC)'] = frame['Date(UTC)'].apply(pd.to_datetime)
frame['newAddressCount'] = frame['AddressCount'].diff()

# frame.drop('Drop',axis = 1, inplace = True)
frame
# frame = pd.concat(li, axis=1)
# # frame
# frame = frame.T.drop_duplicates().T
# frame.drop(frame.columns[[7]], axis = 1, inplace = True)
# frame.rename(columns={frame.columns[[4]]:'DailyTx'}, inplace=True)
# # frame.AddressCount = 
# frame.AddressCount.rename(columns={frame.columns[6]:'AddressCount'})
# frame
# frame.TxGrowth.rename(columns={'Value':'DailyTx'}, inplace=True)
# frame[['MarketCap','AddressCount']]
# frame
# frame = pd.concat(li, axis=0, ignore_index=True)
# frame[10000:]
# [df_ad, df_day, df_mc, df_txg, tmp] = frame
# df_day

# %%
frame

# %%

tmp = frame.copy().loc[:, frame.columns!='Date(UTC)']
tmp = tmp.loc[:, tmp.columns!='Price'].astype(float)
tmp.corr()['MarketCap']

# %%
def shift_(cur, c, n):
    if (n>0):
        df = cur.copy()
        df[c] = df[c].shift(n)
        return df[n:]
    elif(n<0):
        df = cur.copy()
        df[c] = df[c].shift(n)
        return df[:n]
    else:
        return cur.copy()

# %%
#Test shift
shift_(tmp,'MarketCap', -2)

# %%
cur = tmp.corr()['MarketCap'].copy()
# frame[['Unique Address Total Count','MarketCap']]
arr = {}
for i in range(-5, 5):
    cur = pd.concat([shift_(tmp, 'MarketCap', i*2).corr()['MarketCap'],cur], axis = 1)
    index = i*2
    arr[index] = shift_(tmp, 'MarketCap', index).corr()['MarketCap']
# cur
pd.DataFrame.from_dict(arr)

# %%
cur.loc['Unique Address Total Count']

# %%
# sns.lineplot(data = frame, x = "MarketCap", y = "NetHash", color="g")

cur = tmp.corr()['MarketCap'].copy()
# frame[['Unique Address Total Count','MarketCap']]
arr = {}
for i in range(-5, 5):
    cur = pd.concat([shift_(tmp, 'MarketCap', i*2).corr()['MarketCap'],cur], axis = 1)
    index = i*2
    arr[index] = shift_(tmp, 'MarketCap', index).corr()['MarketCap']
# cur
arr = pd.DataFrame.from_dict(arr)


# %%
# frame['year'] = [d.year for d in frame['Date(UTC)']]
# frame['month'] = [d.month for d in frame['Date(UTC)']]
# frame['day'] = [d.day for d in frame['Date(UTC)']]
# frame_by_m = frame[frame['day'] == 1][2:]
# frame_by_m[20:22]





# # frame_ = df_day_s['Unique Address Total Count'].diff().cumsum() / df_day_s['Unique Address Total Count'].iloc[0]
# # df_day_s_n

# # df_day.dtypes

# %%
# print(frame.corrwith(frame['MarketCap']))


# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(data = tmp, x = "Unique Address Total Count", y = "MarketCap", color="g")
# ax2 = plt.twinx()
# sns.lineplot(data=df_day_s_n, color="b", ax=ax2)

# %%
sns.scatterplot(data = frame, x = "Unique Address Total Count", y = "MarketCap", color="g")

# %%
# 'sssd' is not a valid value for name; supported values are 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r'


# %%
target = frame.copy()
target["Year"] = target["Date(UTC)"].dt.year
target = target[target["Year"] > 2018]
# sns.scatterplot(data = target, x = "NetHash", y = "MarketCap", hue="Year", palette="pastel")

# %%
sns.scatterplot(data = target, x = "Unique Address Total Count", y = "MarketCap", hue="Year", palette="pastel")

# %%
sns.scatterplot(data = target, x = "NetHash", y = "MarketCap", hue="Year", palette="pastel")

# %%
sns.scatterplot(data = target, x = "DailyTx", y = "MarketCap", hue="Year", palette="pastel")

# %%
# UnixTimeStamp	AddressCount	Unique Address Total Count	Unique Address Receive Count	Unique Address Sent Count	Supply	MarketCap	NetHash	DailyTx	Average Txn Fee (USD)	Average Txn Fee (Ether)	newAddressCount

# %%
sns.scatterplot(data = target[target['Average Txn Fee (USD)'] < 100], x = "Average Txn Fee (USD)", y = "MarketCap", hue="Year", palette="pastel")

# %%
sns.scatterplot(data = target, x = "AddressCount", y = "MarketCap", hue="Year", palette="pastel")

# %%
target = frame.copy()
target["Year"] = target["Date(UTC)"].dt.year
target = target[target["Year"] > 2018]


