import pandas as pd

#Make Pandas DataFrame objects 
player_stats = pd.read_csv('data/2017-18_playerBoxScore.csv',
                           parse_dates=['gmDate'])
team_stats = pd.read_csv('data/2017-18_teamBoxScore.csv',
                           parse_dates=['gmDate'])
standings = pd.read_csv('data/2017-18_standings.csv',
                           parse_dates=['stDate'])