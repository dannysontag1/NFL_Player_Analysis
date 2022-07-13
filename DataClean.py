import json
import pandas as pd
import pprint
import pandasql as ps
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests
pd.set_option('display.max_columns', None)

QBJSONData = open('QB_JSON_DATA.json')
QBdata = json.load(QBJSONData)
QBdf = pd.DataFrame()
for year in range (2012, 2022):
    QB = QBdata[str(year) + '_players']
    QB = pd.DataFrame(QB)
    QB['Year'] = year
    QBdf = pd.concat([QBdf, QB], axis=0)
# QBdf.to_csv(r'C:\Users\ds022i\Concattest.csv', index=False)

RBJSONData = open('RB_JSON_DATA.json')
RBdata = json.load(RBJSONData)
RBdf = pd.DataFrame()
for year in range (2012, 2022):
    RB = RBdata[str(year) + '_players']
    RB = pd.DataFrame(RB)
    RB['Year'] = year
    RBdf = pd.concat([RBdf, RB], axis=0)
# RBdf.to_csv(r'C:\Users\ds022i\RBConcattest.csv', index=False)
# 
TACKLEJSONData = open('TACKLE_JSON_DATA.json')
TACKLEdata = json.load(TACKLEJSONData)
TACKLEdf = pd.DataFrame()
for year in range (2012, 2022):
    TACKLE = TACKLEdata[str(year) + '_players']
    TACKLE = pd.DataFrame(TACKLE)
    TACKLE['Year'] = year
    TACKLEdf = pd.concat([TACKLEdf, TACKLE], axis=0)
# TACKLEdf.to_csv(r'C:\Users\ds022i\TACKLEConcattest.csv', index=False)

Offense_df = pd.concat([QBdf, RBdf, TACKLEdf], axis=0)
Offense_df.to_csv(r'C:\Users\ds022i\OffenseConcattest.csv', index=False)

EDGEJSONData = open('EDGE_JSON_DATA.json')
EDGEdata = json.load(EDGEJSONData)
EDGEdf = pd.DataFrame()
for year in range (2012, 2022):
    EDGE = EDGEdata[str(year) + '_players']
    EDGE = pd.DataFrame(EDGE)
    EDGE['Year'] = year
    EDGEdf = pd.concat([EDGEdf, EDGE], axis=0)
# EDGEdf.to_csv(r'C:\Users\ds022i\EDGEConcattest.csv', index=False)

LBJSONData = open('LB_JSON_DATA.json')
LBdata = json.load(LBJSONData)
LBdf = pd.DataFrame()
for year in range (2012, 2022):
    LB = LBdata[str(year) + '_players']
    LB = pd.DataFrame(LB)
    LB['Year'] = year
    LBdf = pd.concat([LBdf, LB], axis=0)
# LBdf.to_csv(r'C:\Users\ds022i\LBConcattest.csv', index=False)

CBJSONData = open('CB_JSON_DATA.json')
CBdata = json.load(CBJSONData)
CBdf = pd.DataFrame()
for year in range (2012, 2022):
    CB = CBdata[str(year) + '_players']
    CB = pd.DataFrame(CB)
    CB['Year'] = year
    CBdf = pd.concat([CBdf, CB], axis=0)
# CBdf.to_csv(r'C:\Users\ds022i\CBConcattest.csv', index=False)

Defense_df = pd.concat([EDGEdf, LBdf, CBdf], axis=0)
Defense_df.to_csv(r'C:\Users\ds022i\DefenseConcattest.csv', index=False)




















# QBJSONData = open('QB_JSON_DATA.json')
# QBdata = json.load(QBJSONData)
# QB_2021_player = QBdata['2021_players']
# QB_2021_player = pd.DataFrame(QB_2021_player)
# QB_2021_player['Year'] = QBdata['2021_season']
# QB_2020_player = QBdata['2020_players']
# QB_2020_player = pd.DataFrame(QB_2020_player)
# QB_2020_player['Year'] = QBdata['2020_season']
# QB_2019_player = QBdata['2019_players']
# QB_2019_player = pd.DataFrame(QB_2019_player)
# QB_2019_player['Year'] = QBdata['2019_season']
# QB_2018_player = QBdata['2018_players']
# QB_2018_player = pd.DataFrame(QB_2018_player)
# QB_2018_player['Year'] = QBdata['2018_season']
# QB_2017_player = QBdata['2017_players']
# QB_2017_player = pd.DataFrame(QB_2017_player)
# QB_2017_player['Year'] = QBdata['2017_season']
# QB_2016_player = QBdata['2016_players']
# QB_2016_player = pd.DataFrame(QB_2016_player)
# QB_2016_player['Year'] = QBdata['2016_season']
# QB_2015_player = QBdata['2015_players']
# QB_2015_player = pd.DataFrame(QB_2015_player)
# QB_2015_player['Year'] = QBdata['2015_season']
# QB_2014_player = QBdata['2014_players']
# QB_2014_player = pd.DataFrame(QB_2014_player)
# QB_2014_player['Year'] = QBdata['2014_season']
# QB_2013_player = QBdata['2013_players']
# QB_2013_player = pd.DataFrame(QB_2013_player)
# QB_2013_player['Year'] = QBdata['2013_season']
# QB_2012_player = QBdata['2012_players']
# QB_2012_player = pd.DataFrame(QB_2012_player)
# QB_2012_player['Year'] = QBdata['2012_season']
#
# QBdf = pd.concat([QB_2021_player, QB_2020_player, QB_2019_player, QB_2018_player, QB_2017_player, QB_2016_player, QB_2015_player, QB_2014_player, QB_2013_player, QB_2012_player], axis=0)

# QBdf.to_csv(r'C:\Users\ds022i\QBtest.csv', index=False)

