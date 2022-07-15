import json
import pandas as pd
import pprint
import pandasql as ps
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests
import datetime as dt
pd.set_option('display.max_columns', None)

QBJSONData = open('QB_JSON_DATA.json')
QBdata = json.load(QBJSONData)
# print(QBdata.keys())
QBdf = pd.DataFrame()    # Create a blank df to loop through the keys for each year
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
# Offense_df.to_csv(r'C:\Users\ds022i\OffenseConcattest.csv', index=False)

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
# Defense_df.to_csv(r'C:\Users\ds022i\DefenseConcattest.csv', index=False)


# Columns to bring in Name, grade_position, offense (offense_rating), offense_snaps, age, height, weight, college, year
# Need to filter our blank ages
Offense_df = Offense_df.loc[(Offense_df['age'] != "")]
# Put filter on number of snaps to only return players with significant playing time remove index
Offense_df = Offense_df[Offense_df['offense_snaps'] > 300]
# Age is their current age need to use Year field to get age at the time of the season end
Offense_df['age'] = pd.to_numeric(Offense_df['age'])
today = dt.date.today()
Offense_df['age'] = round(Offense_df['age'] - (today.year - Offense_df['Year'] - today.month/12), 1)
# Filter out only columns I'm going to use
Offense_df = Offense_df[['name', 'grade_position', 'offense', 'offense_snaps', 'age', 'height', 'weight', 'college', 'Year']]
Offense_df.loc[Offense_df['grade_position'] == 'T', 'grade_position'] = 'Tackle'
Offense_df.loc[Offense_df['grade_position'] == 'QB', 'grade_position'] = 'Quarterback'
Offense_df.loc[Offense_df['grade_position'] == 'HB', 'grade_position'] = 'RunningBack'

# Calculate the max performing year for each Offensive Position
# If Max year is in 2021 then we won't include because we don't know if they have hit their peak yet
# If Max year is 2012 (first year of data) they may have already been on the decline so exclude
# Put a filter on 3 season played to get a greater view of a players performance

Offense_Max_df = ps.sqldf("Select Distinct Name, max(offense), grade_position, age, Year,  count(name) from Offense_df group by name having count(name) > 2")
Offense_Max_df = ps.sqldf("Select *, case when year in (2021, 2012) then 'No' else 'Yes' end Max_Year from Offense_Max_df")
Offense_Max_df = ps.sqldf("Select * from Offense_Max_df where Max_Year = 'Yes'")


# Offense_Age_df = Offense_Max_df.groupby('grade_position')['age'].mean()
# print(Offense_Age_df)

# Columns to bring in Name, grade_position, defense, defense_snaps, age, height, weight, college, year

Defense_df = Defense_df.loc[(Defense_df['age'] != "")]
Defense_df = Defense_df[Defense_df['defense_snaps'] > 300]
Defense_df['age'] = pd.to_numeric(Defense_df['age'])
Defense_df['age'] = pd.to_numeric(Defense_df['age'])
today = dt.date.today()
Defense_df['age'] = round(Defense_df['age'] - (today.year - Defense_df['Year'] - today.month/12), 1)
Defense_df = Defense_df[['name', 'grade_position', 'defense', 'defense_snaps', 'age', 'height', 'weight', 'college', 'Year']]
Defense_df.loc[Defense_df['grade_position'] == 'LB', 'grade_position'] = 'Linebacker'
Defense_df.loc[Defense_df['grade_position'] == 'ED', 'grade_position'] = 'DefensiveEnd'
Defense_df.loc[Defense_df['grade_position'] == 'CB', 'grade_position'] = 'Cornerback'
# Defense_df.to_csv(r'C:\Users\ds022i\DefTotalConcattest.csv', index=False)
Defense_Max_df = ps.sqldf("Select Distinct Name, max(defense), grade_position, age, Year,  count(name) from Defense_df group by name having count(name) > 2")
Defense_Max_df = ps.sqldf("Select *, case when year in (2021, 2012) then 'No' else 'Yes' end Max_Year from Defense_Max_df")
Defense_Max_df = ps.sqldf("Select * from Defense_Max_df where Max_Year = 'Yes'")
# Defense_Age_df = Defense_Max_df.groupby('grade_position')['age'].mean()
# print(Defense_Age_df)

# Concat both Defense and Offense DF together
Total_MaxAge_df = pd.concat([Defense_Max_df, Offense_Max_df], axis=0)
# Total_Age_df.to_csv(r'C:\Users\ds022i\TotalConcattest.csv', index=False)
# print(Total_Age_df)

# This Code give you the mean for age for each position
Mean_MaxAge_df = Total_MaxAge_df.groupby('grade_position')['age'].mean()
# print(Mean_MaxAge_df)

Total_MaxAge_df.boxplot(by = 'grade_position', column=['age'],  grid= False, figsize=(8, 6), showfliers = True)
plt.title("Prime Age by Position")
plt.xlabel('Position')
plt.ylabel('Prime Age')
plt.show()

Offense_College_df = Offense_df[['name', 'grade_position', 'college']]
Defense_College_df = Defense_df[['name', 'grade_position', 'college']]
College_df = pd.concat([Offense_College_df, Defense_College_df], axis=0)
# College_df.to_csv(r'C:\Users\ds022i\CollegesConcat.csv', index=False)
# This df has multiple lines for each year played. Need to get unique values
College_df = ps.sqldf("Select distinct name, grade_position, college from College_df group by name")
College_df = ps.sqldf("Select College, grade_position, count(grade_position)from College_df group by college, grade_position having count(grade_position) > 2 order by count(grade_position) desc")
# College_df.to_csv(r'C:\Users\ds022i\GroupedCollege.csv', index=False)
# College_df[0:10].plot(kind = 'bar', x = 'college', y = 'count(grade_position)')
College_by_Position = College_df.groupby(['college']).sum()
print(College_by_Position)

