import streamlit as st
import pandas as pd
import numpy as np

st.title("Web App Football Data")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['England', 'Germany', 'Italy', 'Spain', 'France'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season', ['2022/2021', '2021/2020', '2020/2019'])

# Webscrapping football-data
def load_data(league, season):
    if selected_league == 'England' :
        league = 'E0'
    if selected_league == 'Germany' :
        league = 'D1'
    if selected_league == 'Italy' :
        league = 'I1'
    if selected_league == 'Spain' :
        league = 'SP1'
    if selected_league == 'France' :
        league = 'F1'

    if selecte_season == '2021/2022' :
        season = '2122'
    if selecte_season == '2020/2021' :
        season = '2021'
    if selecte_season == '2019/2020' :
        season = '1920'
        
    url = "https://www.football-data.co.uk/mmz4281/" + season + "/" + league + ".csv"
    data = pd.read_csv(url)
    return data

df = load_data(selected_league, selected_season)

st.subheader ('DataFrame: ' + selected_league)
st.dataframe(df)



