import pandas as pd

games_pd = pd.DataFrame(columns = [
    "Game ID",
    "Player1",
    "Player2",
    "Winner"
])

players = pd.DataFrame(columns = [
    "Name",
    "Wins",
    "Losses",
    "Draws"
])

moves = pd.DataFrame(columns = [
    "Game ID",
    "Turn",
    "Player",
    "Position"
])