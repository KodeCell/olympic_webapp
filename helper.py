import numpy as np

def fetch_medal_tally(df,year,country):
    flag = 0
    data = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal', 'Season'])
    if year == 'Overall' and country == 'Overall':
        new_data = data
    if year == 'Overall' and country != 'Overall':
        flag = 1
        new_data = data[data['region'] == country]
    if year != 'Overall' and country == 'Overall':
        new_data = data[data['Year'] == year]
    if year != 'Overall' and country != 'Overall':
        new_data = data[(data['region'] == country) & (data['Year'] == year)]
    if flag == 1:
        x = new_data.groupby('Year').sum()[['Bronze', 'Silver', 'Gold']].sort_values('Year',
                                                                                      ascending=False).reset_index()
    else:
        x = new_data.groupby('region').sum()[['Bronze', 'Silver', 'Gold']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['Total'] = x['Bronze'] + x['Silver'] + x['Gold']
    return x

def medal_tally(df):
    data = df.drop_duplicates(subset=['Team', 'NOC', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal', 'Season'])
    medal_tally = data.groupby('region').sum()[['Bronze', 'Silver', 'Gold']].reset_index()
    medal_tally['Total'] = medal_tally['Bronze'] + medal_tally['Gold'] + medal_tally['Silver']
    medal_tally = medal_tally.sort_values('Total', ascending=False).reset_index()
    medal_tally = medal_tally.drop('index', axis='columns')



    return medal_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Overall')
    countries = np.unique(df['region'].dropna().values).tolist()
    countries.sort()
    countries.insert(0,'Overall')
    return years, countries

def nations_over_time(df):
    df = df[df['Season'] == 'Summer']
    nations = df.drop_duplicates(['Year','region'])['Year'].value_counts().reset_index().sort_values('index')
    nations.rename(columns = {'index' : 'Year', 'Year' : 'number of countries'},inplace = True)
    return nations

def events_over_time(df):
    df = df[df['Season'] == 'Summer']
    nations = df.drop_duplicates(['Year','Event'])['Year'].value_counts().reset_index().sort_values('index')
    nations.rename(columns = {'index' : 'Year', 'Year' : 'number of Events'},inplace = True)
    return nations

def athletes_over_time(df):
    df = df[df['Season'] == 'Summer']
    nations = df.drop_duplicates(['Year','Name'])['Year'].value_counts().reset_index().sort_values('index')
    nations.rename(columns = {'index' : 'Year', 'Year' : 'number of Athletes'},inplace = True)
    return nations

