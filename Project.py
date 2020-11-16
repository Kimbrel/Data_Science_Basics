import numpy as np
import pandas as pd
import seaborn as sb

# Task 1
pubg = pd.read_csv('pubg - Dr. Darshan Ingle.csv')
#Task 2
print (pubg.dtypes)
#Task 3 
print(pubg.describe())
#Task 5
ex_data = pubg['kills']
print(ex_data.mode())
#Task 6
print(ex_data.max())
#Task 7
col = pubg.shape
pd.set_option('display.max_columns', col[1])
print(pubg)
#Task 8
sb.distplot(pubg['matchDuration'])
#Task 9
sb.distplot(pubg['walkDistance'])
#Task 10 and 11
sb.distplot(x= 'walkDistance',y = 'matchDuration', data = pubg)
#Task 12
sb.pairplot(pubg)
#Task 13
print(pubg['matchType'].value_counts())
#Task 14
sb.barplot(x = 'matchType', y = 'killPoints', data = pubg)
# normal-duo-fpp has max killPoints
#Task 15
sb.barplot(x = 'matchType', y = 'weaponsAcquired', data = pubg)
# crashtpp  has acquired max weapons

#Task 16
if pubg.dtypes.name == 'category':
    print(pubg.dtypes)
else:
    print('no categorial column')
#task 17
sb.boxplot(x = 'matchType', y = 'winPlacePerc', data = pubg)
#Task 18
sb.boxplot(x = 'matchType', y = 'matchDuration', data = pubg)
#Task 19
sb.boxplot(y = 'matchType', x = 'matchDuration', data = pubg)
#Task 20

KILL = pubg['headshotKills']+pubg['teamKills']+pubg['roadKills']
pubg['KILL'] = KILL
#Task 21
pubg['winPlacePerc'] = round(pubg['winPlacePerc'], 2)
print(pubg)
