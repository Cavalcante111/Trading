import streamlit as st
import pandas as pd
import numpy as np

st.title("WebApp Extraindo Dados de Futebol")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['England', 'Germany', 'Italy', 'Spain', 'France', 'Brasil'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season', ['2024/2025', '2023/2024', '2022/2023', '2021/2022', '2020/2021', '2019/2020'])

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

    if selected_season == '2024/2025' :
        season = '2425'
    if selected_season == '2023/2024' :
        season = '2324'
    if selected_season == '2022/2023' :
        season = '2223'
    if selected_season == '2021/2022' :
        season = '2122'
    if selected_season == '2020/2021' :
        season = '2021'
    if selected_season == '2019/2020' :
        season = '1920'
        
    if selected_league == 'Brasil' :
        url = "https://www.football-data.co.uk/new/BRA.csv"
    else
        url = "https://www.football-data.co.uk/mmz4281/" + season + "/" + league + ".csv"
    data = pd.read_csv(url)
    return data

df = load_data(selected_league, selected_season)

st.subheader("DataFrame: " + selected_league)
st.dataframe(df)



