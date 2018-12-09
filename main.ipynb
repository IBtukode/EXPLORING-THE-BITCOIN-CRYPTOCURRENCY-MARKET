# EXPLORING-THE-BITCOIN-CRYPTOCURRENCY-MARKET
# The DataCamp project in exploring the BTC
# Task 1. Load in the Current variable the data on cryptocurrencies from coinmarketcap.com

import pandas as pd
import matplotlib.pyplot as plt
# Display plotting commands inline with frontends directly below the code cell that produced it. Error syntax if used to PyCharm
%matplotlib inline
%config InlineBackend.figure_format = 'svg' 
plt.style.use('fivethirtyeight')

# Reading in current data from coinmarketcap.com
current = pd.read_json("https://api.coinmarketcap.com/v1/ticker/")
# Printing out the header of the current variable
print(current.head())
 

# Task 2. Load the CSV file and select the relevant columns
# Read datasets CSV file into pd and assign it to variable dec6
dec6 = pd.read_csv("datasets/coinmarketcap_06122017.csv")
# From the variable dec6 select the columns id and market_cap_usd. Note, use [[]] in order to maintain the DataFrame format instead of Pandas Series
market_cap_raw = dec6[['id', 'market_cap_usd']]
# Count the number of values using count method. EDA
print(market_cap_raw.count())

# Task 3. Clean data
# As we can see 295 Cryptos have no market capitalization. Therefore the data should be cleaned
# df.query('a > 0') is simillar df[df['a'] > 0] 
cap = market_cap_raw.query('market_cap_usd > 0')

# Task 4. Compare Market cap of BTC to other cryptos. Top 10 cryptos by market cap
TOP_CAP_TITLE  = 'Top 10 market capitalization'
TOP_CAP_YLABEL = '% of total cap'

cap10 = caphead(10).set_index('id')
cap10 = cap10.assign(market_cap_perc = lambda x: (x.market_cap_usd/cap10.market_cap_usd.sum())* 100)
ax = cap10.market_cap_perc.plot.bar(title=TOP_CAP_TITLE)
ax.set_ylabel(TOP_CAP_YLABEL(

# Task 5. Visualize the market cap
# Colors for the bar plot
COLORS = ['orange', 'green', 'orange', 'cyan', 'cyan', 'blue', 'silver', 'orange', 'red', 'green']

# Plotting market_cap_usd as before but adding the colors and scaling the y-axis  
ax = cap10.market_cap_usd.head(10).plot.bar(colors = COLORS, title = TOP_CAP_TITLE)
ax.set_yscale('log')
ax.set_ylabel('USD')
ax.set_xlabel('')

# Task6. Volatility on crypto

# Selecting the id, percent_change_24h and percent_change_7d columns
volatility = dec6.loc[:,["id", "percent_change_24h", "percent_change_7d"]]
# Setting the index to 'id' and dropping all NaN rows
volatility = volatility.set_index('id').dropna()
# Sorting the DataFrame by percent_change_24h in ascending order
volatility = volatility.sort_values(by='percent_change_24h', ascending=True)
# Checking the first few rows
print(volatility.head())

# Task7. Determine top losers and winners
#Defining a function with 2 parameters, the series to plot and the title
def top10_subplot(volatility_series, title):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    volatility_series[:10].plot.bar(ax=axes[0], color='darkred')
    fig.suptitle(title)
    ax.set_ylabel('% change')
    volatility_series[-10:].plot.bar(ax=axes[1], color='darkblue')
    return fig, ax
DTITLE = "24 hours top losers and winners"
# Calling the function above with the 24 hours period series and title DTITLE  
fig, ax = top10_subplot(volatility.percent_change_24h, DTITLE)

# Task8. Check the weekly volatility
# Sorting weekly volatility in ascending order
volatility7d = volatility.sort_values(by='percent_change_7d', ascending=True)
WTITLE = "Weekly top losers and winners"
# Calling the top10_subplot function in order to depict the plot
fig, ax = top10_subplot(volatility7d.percent_change_7d, WTITLE)

# Task10. Visualize the number of large, medium and small coins

def capcount(query_string):
    return cap.query(query_string).count().id
LABELS = ["biggish", "micro", "nano"]
biggish = capcount('market_cap_usd > 3e+8')
micro = capcount('market_cap_usd > 5e+7 and market_cap_usd < 3e+8')
nano =  capcount('market_cap_usd < 5e+7')

values = [biggish, micro, nano]
plt.title('Classification of coins by market cap')
plt.ylabel('Number of coins')
plt.bar(range(len(values)), values, tick_label=LABELS)

