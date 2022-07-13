import json
import pandas as pd
import pprint
import pandasql as ps
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests
import os
pd.set_option('display.max_columns', None)



QBJSONData = open('QB2012.json')
QBdata = json.load(QBJSONData)
QB_2012_player = QBdata['2012players']
QB_2012_player = pd.DataFrame(QB_2012_player)
QB_2012_player['Year'] = QBdata['2012season']
print(QB_2012_player)





# QB_2013_Player_Data = QBdata['2013players']
# QB_2013_Season = QBdata['2013season']
# QB_2013_Player_Data = pd.DataFrame[QB_2013_Player_Data]
# print(QB_2013_Player_Data)
# QBplayer2021 = QBdata2021['players']
# QBseason2021 = QBdata2021['season']
# QBplayer2021 = pd.DataFrame(QBplayer2021)
# QBplayer2021['season'] = QBseason2021
# print(QBplayer2021)



# QBdata2021 = open('QB2012.json')
# QBdata2021 = json.load(QBdata2021)
# QBdata2021 = QBdata2021['players']
# QBdf2021 = pd.DataFrame(QBdata2021)
# QBdf2021.to_csv(r'C:\Users\ds022i\test.csv', index=False)
# QBdf2021 = QBdf2021[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2021['year'] = 2021
# QBdf2021 = QBdf2021.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2021 = QBdf2021.loc[(QBdf2021['age'] != "")]
# QBdf2021 = (QBdf2021[(QBdf2021['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2021['age'] = pd.to_numeric(QBdf2021['age'])
# QBdf2021['age'] = QBdf2021['age'] - .5
# QBdf2021 = QBdf2021[['name', 'offense', 'age', 'year']]
# print(QBdf2021)
# print(QBdf2021)
#
# QBdata2020 = open('QB2020.json')
# QBdata2020 = json.load(QBdata2020)
# QBdata2020 = QBdata2020['players']
# QBdf2020 = pd.DataFrame(QBdata2020)
# QBdf2020 = QBdf2020[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2020['year'] = 2020
# QBdf2020 = QBdf2020.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2020 = QBdf2020.loc[(QBdf2020['age'] != "")]
# QBdf2020 = (QBdf2020[(QBdf2020['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2020['age'] = pd.to_numeric(QBdf2020['age'])
# QBdf2020['age'] = QBdf2020['age'] - 1.5
# QBdf2020 = QBdf2020[['name', 'offense', 'age', 'year']]
# print(QBdf2020)
#
# QBdata2019 = open('QB2019.json')
# QBdata2019 = json.load(QBdata2019)
# QBdata2019 = QBdata2019['players']
# QBdf2019 = pd.DataFrame(QBdata2019)
# QBdf2019 = QBdf2019[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2019['year'] = 2019
# QBdf2019 = QBdf2019.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2019 = QBdf2019.loc[(QBdf2019['age'] != "")]
# QBdf2019 = (QBdf2019[(QBdf2019['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2019['age'] = pd.to_numeric(QBdf2019['age'])
# QBdf2019['age'] = QBdf2019['age'] - 2.5
# QBdf2019 = QBdf2019[['name', 'offense', 'age', 'year']]
# # print(QBdf2019)
#
# QBdata2018 = open('QB2018.json')
# QBdata2018 = json.load(QBdata2018)
# QBdata2018 = QBdata2018['players']
# QBdf2018 = pd.DataFrame(QBdata2018)
# QBdf2018 = QBdf2018[['name', 'offense', 'pass', 'age', 'height', 'weight' 'offense_snaps', 'college']]
# QBdf2018['year'] = 2018
# QBdf2018 = QBdf2018.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2018 = QBdf2018.loc[(QBdf2018['age'] != "")]
# QBdf2018 = (QBdf2018[(QBdf2018['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2018['age'] = pd.to_numeric(QBdf2018['age'])
# QBdf2018['age'] = QBdf2018['age'] - 3.5
# QBdf2018 = QBdf2018[['name', 'offense', 'age', 'year']]
# # print(QBdf2018)
#
# QBdata2017 = open('QB2017.json')
# QBdata2017 = json.load(QBdata2017)
# QBdata2017 = QBdata2017['players']
# QBdf2017 = pd.DataFrame(QBdata2017)
# QBdf2017 = QBdf2017[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2017['year'] = 2017
# QBdf2017 = QBdf2017.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2017 = QBdf2017.loc[(QBdf2017['age'] != "")]
# QBdf2017 = (QBdf2017[(QBdf2017['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2017['age'] = pd.to_numeric(QBdf2017['age'])
# QBdf2017['age'] = QBdf2017['age'] - 4.5
# QBdf2017 = QBdf2017[['name', 'offense', 'age', 'year']]
# # print(QBdf2017)
#
# QBdata2016 = open('QB2016.json')
# QBdata2016 = json.load(QBdata2016)
# QBdata2016 = QBdata2016['players']
# QBdf2016 = pd.DataFrame(QBdata2016)
# QBdf2016 = QBdf2016[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2016['year'] = 2016
# QBdf2016 = QBdf2016.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2016 = QBdf2016.loc[(QBdf2016['age'] != "")]
# QBdf2016 = (QBdf2016[(QBdf2016['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2016['age'] = pd.to_numeric(QBdf2016['age'])
# QBdf2016['age'] = QBdf2016['age'] - 5.5
# QBdf2016 = QBdf2016[['name', 'offense', 'age', 'year']]
# # print(QBdf2016)
#
# QBdata2015 = open('QB2015.json')
# QBdata2015 = json.load(QBdata2015)
# QBdata2015 = QBdata2015['players']
# QBdf2015 = pd.DataFrame(QBdata2015)
# QBdf2015 = QBdf2015[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2015['year'] = 2015
# QBdf2015 = QBdf2015.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2015 = QBdf2015.loc[(QBdf2015['age'] != "")]
# QBdf2015 = (QBdf2015[(QBdf2015['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2015['age'] = pd.to_numeric(QBdf2015['age'])
# QBdf2015['age'] = QBdf2015['age'] - 6.5
# QBdf2015 = QBdf2015[['name', 'offense', 'age', 'year']]
# # print(QBdf2015)
#
# QBdata2014 = open('QB2014.json')
# QBdata2014 = json.load(QBdata2014)
# QBdata2014 = QBdata2014['players']
# QBdf2014 = pd.DataFrame(QBdata2014)
# QBdf2014 = QBdf2014[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2014['year'] = 2014
# QBdf2014 = QBdf2014.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2014 = QBdf2014.loc[(QBdf2014['age'] != "")]
# QBdf2014 = (QBdf2014[(QBdf2014['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2014['age'] = pd.to_numeric(QBdf2014['age'])
# QBdf2014['age'] = QBdf2014['age'] - 7.5
# QBdf2014 = QBdf2014[['name', 'offense', 'age', 'year']]
# # print(QBdf2014)
#
# QBdata2013 = open('QB2013.json')
# QBdata2013 = json.load(QBdata2013)
# QBdata2013 = QBdata2013['players']
# QBdf2013 = pd.DataFrame(QBdata2013)
# QBdf2013 = QBdf2013[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2013['year'] = 2013
# QBdf2013 = QBdf2013.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2013 = QBdf2013.loc[(QBdf2013['age'] != "")]
# QBdf2013 = (QBdf2013[(QBdf2013['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2013['age'] = pd.to_numeric(QBdf2013['age'])
# QBdf2013['age'] = QBdf2013['age'] - 8.5
# QBdf2013 = QBdf2013[['name', 'offense', 'age', 'year']]
# # print(QBdf2013)
#
# QBdata2012 = open('QB2012.json')
# QBdata2012 = json.load(QBdata2012)
# QBdata2012 = QBdata2012['players']
# QBdf2012 = pd.DataFrame(QBdata2012)
# QBdf2012 = QBdf2012[['name', 'offense', 'age', 'offense_snaps']]
# QBdf2012['year'] = 2012
# QBdf2012 = QBdf2012.sort_values('offense', ascending=False, ignore_index=True)
# QBdf2012 = QBdf2012.loc[(QBdf2012['age'] != "")]
# QBdf2012 = (QBdf2012[(QBdf2012['offense_snaps'] > 500)].sort_values('offense', ascending=False, ignore_index=True))
# QBdf2012['age'] = pd.to_numeric(QBdf2012['age'])
# QBdf2012['age'] = QBdf2012['age'] - 9.5
# QBdf2012 = QBdf2012[['name', 'offense', 'age', 'year']]
# print(QBdf2012)
#
# QBdf = pd.concat([QBdf2021, QBdf2020, QBdf2019, QBdf2018, QBdf2017, QBdf2016, QBdf2015, QBdf2014, QBdf2013, QBdf2012], axis=0)
# # print(QBdf)
#
# # MaxQBdf = ps.sqldf("Select Distinct name, max(offense), age, year from QBdf group by name")
# # MaxQBdf = ps.sqldf("Select *, case when year in (2021, 2012) then 'May Not be Maxed' else 'Maxed' end Full_data from MaxQBdf")
# # MaxQBdf = ps.sqldf("Select * from MaxQBdf where Full_data = 'Maxed'")
# #
# # # print(MaxQBdf)
# #
# # print(ps.sqldf('Select avg(age) from MaxQBdf'))
