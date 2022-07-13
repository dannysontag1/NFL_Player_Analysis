import json
import pandas as pd
import pprint
import pandasql as ps
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

RBdata2021 = open('RB2021.json')
RBdata2021 = json.load(RBdata2021)
RBdata2021 = RBdata2021['players']
RBdf2021 = pd.DataFrame(RBdata2021)
RBdf2021 = RBdf2021[['name', 'offense', 'age', 'offense_snaps']]
RBdf2021['year'] = 2021
RBdf2021 = RBdf2021.sort_values('offense', ascending=False, ignore_index=True)
RBdf2021 = RBdf2021.loc[(RBdf2021['age'] != "")]
RBdf2021 = (RBdf2021[(RBdf2021['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2021['age'] = pd.to_numeric(RBdf2021['age'])
RBdf2021['age'] = RBdf2021['age'] - .5
RBdf2021 = RBdf2021[['name', 'offense', 'age', 'year']]
# print(RBdf2021)

RBdata2020 = open('RB2020.json')
RBdata2020 = json.load(RBdata2020)
RBdata2020 = RBdata2020['players']
RBdf2020 = pd.DataFrame(RBdata2020)
RBdf2020 = RBdf2020[['name', 'offense', 'age', 'offense_snaps']]
RBdf2020['year'] = 2020
RBdf2020 = RBdf2020.sort_values('offense', ascending=False, ignore_index=True)
RBdf2020 = RBdf2020.loc[(RBdf2020['age'] != "")]
RBdf2020 = (RBdf2020[(RBdf2020['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2020['age'] = pd.to_numeric(RBdf2020['age'])
RBdf2020['age'] = RBdf2020['age'] - 1.5
RBdf2020 = RBdf2020[['name', 'offense', 'age', 'year']]
# print(RBdf2020)

RBdata2019 = open('RB2019.json')
RBdata2019 = json.load(RBdata2019)
RBdata2019 = RBdata2019['players']
RBdf2019 = pd.DataFrame(RBdata2019)
RBdf2019 = RBdf2019[['name', 'offense', 'age', 'offense_snaps']]
RBdf2019['year'] = 2019
RBdf2019 = RBdf2019.sort_values('offense', ascending=False, ignore_index=True)
RBdf2019 = RBdf2019.loc[(RBdf2019['age'] != "")]
RBdf2019 = (RBdf2019[(RBdf2019['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2019['age'] = pd.to_numeric(RBdf2019['age'])
RBdf2019['age'] = RBdf2019['age'] - 2.5
RBdf2019 = RBdf2019[['name', 'offense', 'age', 'year']]
# print(RBdf2019)

RBdata2018 = open('RB2018.json')
RBdata2018 = json.load(RBdata2018)
RBdata2018 = RBdata2018['players']
RBdf2018 = pd.DataFrame(RBdata2018)
RBdf2018 = RBdf2018[['name', 'offense', 'age', 'offense_snaps']]
RBdf2018['year'] = 2018
RBdf2018 = RBdf2018.sort_values('offense', ascending=False, ignore_index=True)
RBdf2018 = RBdf2018.loc[(RBdf2018['age'] != "")]
RBdf2018 = (RBdf2018[(RBdf2018['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2018['age'] = pd.to_numeric(RBdf2018['age'])
RBdf2018['age'] = RBdf2018['age'] - 3.5
RBdf2018 = RBdf2018[['name', 'offense', 'age', 'year']]
# print(RBdf2018)

RBdata2017 = open('RB2017.json')
RBdata2017 = json.load(RBdata2017)
RBdata2017 = RBdata2017['players']
RBdf2017 = pd.DataFrame(RBdata2017)
RBdf2017 = RBdf2017[['name', 'offense', 'age', 'offense_snaps']]
RBdf2017['year'] = 2017
RBdf2017 = RBdf2017.sort_values('offense', ascending=False, ignore_index=True)
RBdf2017 = RBdf2017.loc[(RBdf2017['age'] != "")]
RBdf2017 = (RBdf2017[(RBdf2017['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2017['age'] = pd.to_numeric(RBdf2017['age'])
RBdf2017['age'] = RBdf2017['age'] - 4.5
RBdf2017 = RBdf2017[['name', 'offense', 'age', 'year']]
# print(RBdf2017)

RBdata2016 = open('RB2016.json')
RBdata2016 = json.load(RBdata2016)
RBdata2016 = RBdata2016['players']
RBdf2016 = pd.DataFrame(RBdata2016)
RBdf2016 = RBdf2016[['name', 'offense', 'age', 'offense_snaps']]
RBdf2016['year'] = 2016
RBdf2016 = RBdf2016.sort_values('offense', ascending=False, ignore_index=True)
RBdf2016 = RBdf2016.loc[(RBdf2016['age'] != "")]
RBdf2016 = (RBdf2016[(RBdf2016['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2016['age'] = pd.to_numeric(RBdf2016['age'])
RBdf2016['age'] = RBdf2016['age'] - 5.5
RBdf2016 = RBdf2016[['name', 'offense', 'age', 'year']]
# print(RBdf2016)

RBdata2015 = open('RB2015.json')
RBdata2015 = json.load(RBdata2015)
RBdata2015 = RBdata2015['players']
RBdf2015 = pd.DataFrame(RBdata2015)
RBdf2015 = RBdf2015[['name', 'offense', 'age', 'offense_snaps']]
RBdf2015['year'] = 2015
RBdf2015 = RBdf2015.sort_values('offense', ascending=False, ignore_index=True)
RBdf2015 = RBdf2015.loc[(RBdf2015['age'] != "")]
RBdf2015 = (RBdf2015[(RBdf2015['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2015['age'] = pd.to_numeric(RBdf2015['age'])
RBdf2015['age'] = RBdf2015['age'] - 6.5
RBdf2015 = RBdf2015[['name', 'offense', 'age', 'year']]
# print(RBdf2015)

RBdata2014 = open('RB2014.json')
RBdata2014 = json.load(RBdata2014)
RBdata2014 = RBdata2014['players']
RBdf2014 = pd.DataFrame(RBdata2014)
RBdf2014 = RBdf2014[['name', 'offense', 'age', 'offense_snaps']]
RBdf2014['year'] = 2014
RBdf2014 = RBdf2014.sort_values('offense', ascending=False, ignore_index=True)
RBdf2014 = RBdf2014.loc[(RBdf2014['age'] != "")]
RBdf2014 = (RBdf2014[(RBdf2014['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2014['age'] = pd.to_numeric(RBdf2014['age'])
RBdf2014['age'] = RBdf2014['age'] - 7.5
RBdf2014 = RBdf2014[['name', 'offense', 'age', 'year']]
# print(RBdf2014)

RBdata2013 = open('RB2013.json')
RBdata2013 = json.load(RBdata2013)
RBdata2013 = RBdata2013['players']
RBdf2013 = pd.DataFrame(RBdata2013)
RBdf2013 = RBdf2013[['name', 'offense', 'age', 'offense_snaps']]
RBdf2013['year'] = 2013
RBdf2013 = RBdf2013.sort_values('offense', ascending=False, ignore_index=True)
RBdf2013 = RBdf2013.loc[(RBdf2013['age'] != "")]
RBdf2013 = (RBdf2013[(RBdf2013['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2013['age'] = pd.to_numeric(RBdf2013['age'])
RBdf2013['age'] = RBdf2013['age'] - 8.5
RBdf2013 = RBdf2013[['name', 'offense', 'age', 'year']]
# print(RBdf2013)

RBdata2012 = open('RB2012.json')
RBdata2012 = json.load(RBdata2012)
RBdata2012 = RBdata2012['players']
RBdf2012 = pd.DataFrame(RBdata2012)
RBdf2012 = RBdf2012[['name', 'offense', 'age', 'offense_snaps']]
RBdf2012['year'] = 2012
RBdf2012 = RBdf2012.sort_values('offense', ascending=False, ignore_index=True)
RBdf2012 = RBdf2012.loc[(RBdf2012['age'] != "")]
RBdf2012 = (RBdf2012[(RBdf2012['offense_snaps'] > 300)].sort_values('offense', ascending=False, ignore_index=True))
RBdf2012['age'] = pd.to_numeric(RBdf2012['age'])
RBdf2012['age'] = RBdf2012['age'] - 9.5
RBdf2012 = RBdf2012[['name', 'offense', 'age', 'year']]
# print(RBdf2012)

RBdf = pd.concat([RBdf2021, RBdf2020, RBdf2019, RBdf2018, RBdf2017, RBdf2016, RBdf2015, RBdf2014, RBdf2013, RBdf2012], axis=0)
# print(RBdf)

MaxRBdf = ps.sqldf("Select Distinct name, max(offense), age, year from RBdf group by name")
MaxRBdf = ps.sqldf("Select *, case when year in (2021, 2012) then 'May Not be Maxed' else 'Maxed' end Full_data from MaxRBdf")
MaxRBdf = ps.sqldf("Select * from MaxRBdf where Full_data = 'Maxed'")

print(ps.sqldf('Select avg(age) from MaxRBdf'))
