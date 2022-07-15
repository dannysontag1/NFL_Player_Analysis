import json
import pandas as pd
import pandasql as ps
import matplotlib.pyplot as plt
import datetime as dt

QBJSONData = open('QB_JSON_DATA.json')
QBdata = json.load(QBJSONData)
QBdf = pd.DataFrame()
for year in range (2012, 2022):
    QB = QBdata[str(year) + '_players']
    QB = pd.DataFrame(QB)
    QB['Year'] = year
    QBdf = pd.concat([QBdf, QB], axis=0)

RBJSONData = open('RB_JSON_DATA.json')
RBdata = json.load(RBJSONData)
RBdf = pd.DataFrame()
for year in range (2012, 2022):
    RB = RBdata[str(year) + '_players']
    RB = pd.DataFrame(RB)
    RB['Year'] = year
    RBdf = pd.concat([RBdf, RB], axis=0)

TACKLEJSONData = open('TACKLE_JSON_DATA.json')
TACKLEdata = json.load(TACKLEJSONData)
TACKLEdf = pd.DataFrame()
for year in range (2012, 2022):
    TACKLE = TACKLEdata[str(year) + '_players']
    TACKLE = pd.DataFrame(TACKLE)
    TACKLE['Year'] = year
    TACKLEdf = pd.concat([TACKLEdf, TACKLE], axis=0)

EDGEJSONData = open('EDGE_JSON_DATA.json')
EDGEdata = json.load(EDGEJSONData)
EDGEdf = pd.DataFrame()
for year in range (2012, 2022):
    EDGE = EDGEdata[str(year) + '_players']
    EDGE = pd.DataFrame(EDGE)
    EDGE['Year'] = year
    EDGEdf = pd.concat([EDGEdf, EDGE], axis=0)

LBJSONData = open('LB_JSON_DATA.json')
LBdata = json.load(LBJSONData)
LBdf = pd.DataFrame()
for year in range (2012, 2022):
    LB = LBdata[str(year) + '_players']
    LB = pd.DataFrame(LB)
    LB['Year'] = year
    LBdf = pd.concat([LBdf, LB], axis=0)

CBJSONData = open('CB_JSON_DATA.json')
CBdata = json.load(CBJSONData)
CBdf = pd.DataFrame()
for year in range (2012, 2022):
    CB = CBdata[str(year) + '_players']
    CB = pd.DataFrame(CB)
    CB['Year'] = year
    CBdf = pd.concat([CBdf, CB], axis=0)

Offense_df = pd.concat([QBdf, RBdf, TACKLEdf], axis=0)
Offense_df = Offense_df.loc[(Offense_df['age'] != "")]
Offense_df = Offense_df[Offense_df['offense_snaps'] > 300]
Offense_df['age'] = pd.to_numeric(Offense_df['age'])
today = dt.date.today()
Offense_df['age'] = round(Offense_df['age'] - (today.year - Offense_df['Year'] - today.month/12), 1)
Offense_df = Offense_df[['name', 'grade_position', 'offense', 'age', 'height', 'weight', 'college', 'Year']]
Offense_df = Offense_df.rename(columns={'name': 'Name', 'grade_position': 'Position', 'offense': 'Grade', 'age':'Age', 'height': 'Height', 'weight': 'Weight', 'college': 'College'})
Offense_df.loc[Offense_df['Position'] == 'T', 'Position'] = 'Tackle'
Offense_df.loc[Offense_df['Position'] == 'QB', 'Position'] = 'Quarterback'
Offense_df.loc[Offense_df['Position'] == 'HB', 'Position'] = 'RunningBack'

Defense_df = pd.concat([EDGEdf, LBdf, CBdf], axis=0)
Defense_df = Defense_df.loc[(Defense_df['age'] != "")]
Defense_df = Defense_df[Defense_df['defense_snaps'] > 300]
Defense_df['age'] = pd.to_numeric(Defense_df['age'])
Defense_df['age'] = pd.to_numeric(Defense_df['age'])
today = dt.date.today()
Defense_df['age'] = round(Defense_df['age'] - (today.year - Defense_df['Year'] - today.month/12), 1)
Defense_df = Defense_df[['name', 'grade_position', 'defense', 'age', 'height', 'weight', 'college', 'Year']]
Defense_df = Defense_df.rename(columns={'name': 'Name', 'grade_position': 'Position', 'defense': 'Grade', 'age':'Age', 'height': 'Height', 'weight': 'Weight', 'college': 'College'})
Defense_df.loc[Defense_df['Position'] == 'LB', 'Position'] = 'Linebacker'
Defense_df.loc[Defense_df['Position'] == 'ED', 'Position'] = 'DefensiveEnd'
Defense_df.loc[Defense_df['Position'] == 'CB', 'Position'] = 'Cornerback'

Player_df = pd.concat([Defense_df, Offense_df], axis=0)


Player_Max_df = ps.sqldf("Select Distinct Name, max(Grade), Position, Age, Year, count(Name) from Player_df group by Name having count(Name) > 2")
Player_Max_df = ps.sqldf("Select *, case when year in (2021, 2012) then 'No' else 'Yes' end Max_Year from Player_Max_df")
Player_Max_df = ps.sqldf("Select * from Player_Max_df where Max_Year = 'Yes'")

Mean_MaxAge_df = Player_Max_df.groupby('Position')['Age'].mean().sort_values(ascending=False)


bp = Player_Max_df.boxplot(by = 'Position', column=['Age'],  grid= False, figsize=(12, 10), showfliers = True)
plt.title("Prime Age by Position", size=25)
# bp.get_figure().gca().set_title("")
plt.xlabel('Position', size=20)
plt.ylabel('Prime Age', size=20)
plt.show()


# Breakdown of colleges that produced the most amount of players in the NFL over the last 10 years at one of these positions
College_df = Player_df[['Name', 'Position', 'College', 'Year']]
# Max year to remove duplicates and get the last year that an individual played
College_df = Player_df.groupby(['Name', 'College', 'Position'])['Year'].max()
College_Position_df = College_df.groupby(['College', 'Position']).count()
College_Position_df.sort_values(ascending=False).head(20)


College_df = Player_df[['Name', 'Position', 'College', 'Year']]
College_df = ps.sqldf("Select distinct Name, Position, College from College_df group by Name")
CB_df = ps.sqldf("Select College, Position, count(Position) from College_df where Position = 'Cornerback' group by College, Position having count(Position) > 6 order by count(Position)")
LB_df = ps.sqldf("Select College, Position, count(Position) from College_df where Position = 'Linebacker' group by College, Position having count(Position) > 5 order by count(Position)")
DE_df = ps.sqldf("Select College, Position, count(Position) from College_df where Position = 'DefensiveEnd' group by College, Position having count(Position) > 6 order by count(Position)")
QB_df = ps.sqldf("Select College, Position, count(Position) from College_df where Position = 'Quarterback' group by College, Position having count(Position) > 2 order by count(Position)")
RB_df = ps.sqldf("Select College, Position, count(Position) from College_df where Position = 'RunningBack' group by College, Position having count(Position) > 4 order by count(Position)")
T_df = ps.sqldf("Select College, Position, count(Position) from College_df where Position = 'Tackle' group by College, Position having count(Position) > 4 order by count(Position)")
# T_df.plot(kind = 'bar', x = 'College', y = 'count(Position)')
# plt.show()
plt.figure(figsize = (25, 15))
plt.subplot(231)
plt.barh(QB_df['College'], QB_df['count(Position)'], color='green')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Quarterbacks by College', fontsize=27)

plt.subplot(232)
plt.barh(RB_df['College'], RB_df['count(Position)'], color='orange')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Running Backs by College', fontsize=27)

plt.subplot(233)
plt.barh(T_df['College'], T_df['count(Position)'])
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Tackles by College', fontsize=27)

plt.subplot(234)
plt.barh(DE_df['College'], DE_df['count(Position)'], color='Purple')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Defensive Ends by College', fontsize=27)

plt.subplot(235)
plt.barh(CB_df['College'], CB_df['count(Position)'], color='Red')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Cornerbacks by College', fontsize=27)

plt.subplot(236)
plt.barh(LB_df['College'], LB_df['count(Position)'], color='Grey')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Linebackers by College', fontsize=27)


plt.tight_layout()
plt.show()

