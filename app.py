import streamlit as st
import preprocess
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = preprocess.preprocessing()

st.sidebar.title('Olympic Analysis')

user_menu = st.sidebar.radio(
    'Select an option',
    ('Dataset','Medal Tally', 'Overall Analysis')
)
st.sidebar.header('Medal Tally')
if user_menu == 'Dataset':
    st.dataframe(df)
if user_menu == 'Medal Tally':
    years,countries = helper.country_year_list(df)

    # since the function takes a list and the title as input therefore we made a function to create a list of the years
    selected_year = st.sidebar.selectbox('Select Year',years)
    selected_country = st.sidebar.selectbox('Select Country',countries)
    medal_tally1 = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Performance')
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title(f'Overall performance of countries in {selected_year}')
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(f'Overall performance of {selected_country} in all years')
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(f'Performance of {selected_country} in {selected_year}')
    st.table(medal_tally1)

if user_menu == 'Overall Analysis':
    sports = df['Sport'].unique().size
    winter = df[df['Season'] == "Summer"]['Year'].unique().size
    summer = df[df['Season'] == "Winter"]['Year'].unique().size
    total = df['Year'].unique().size
    cities = df['City'].unique().size
    events = df['Event'].unique().size
    athletes = df['Name'].unique().size
    nations = df['region'].unique().size

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Total Summer Olympics')
        st.title(summer)
    with col2:
        st.header('Total Winter Olympics')
        st.title(winter)
    with col3:
        st.header('Total number of olympics')
        st.title(total)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Total number of Sports')
        st.title(sports)
    with col2:
        st.header('Total number of events')
        st.title(events)
    with col3:
        st.header('Total number of athletes')
        st.title(athletes)
    st.header('Total number of Countries')
    st.title(nations)

    st.title('Participation of nations over years')
    nations_over_time = helper.nations_over_time(df)
    fig = px.line(nations_over_time, x='Year', y='number of countries')
    st.plotly_chart(fig)

    st.title('Number of events over years')
    events_over_time = helper.events_over_time(df)
    fig2 = px.bar(events_over_time,x = 'Year',y = 'number of Events')
    st.plotly_chart(fig2)

    st.title('Number of Athletes over years')
    events_over_time = helper.athletes_over_time(df)
    fig3= px.line(events_over_time,x = 'Year',y = 'number of Athletes')
    st.plotly_chart(fig3)

    st.title('Number of Events over time(every sport')
    fig,ax = plt.subplots(figsize = (20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(x.pivot_table(index = 'Sport',columns = 'Year',values = 'Event',aggfunc = 'count').fillna(0).astype('int'),annot = True)
    st.pyplot(fig)






