"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Prove 12
"""
import pandas as pd # Data manipulation library
import seaborn as sb # Graphing library
import matplotlib.pyplot as plt # show Graphs
import numpy as np

# Load the data
players = pd.read_csv("nba_basketball_data/basketball_players.csv")
master = pd.read_csv("nba_basketball_data/basketball_master.csv")

players_info = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

# PART 1

# 1. Calculate the mean and median number of points scored.
points_mean = players_info.points.mean()
points_median = players_info.points.median()
print(f"""Mean number of points per season:\n{points_mean:.2f}
Median number of points per season:\n{points_median:.2f}""")

# 2. Determine the highest number of points recorded in a single season.
#    Identify who scored those points and the year they did so.
highest_point_data = players_info[players_info.points == players_info.points.max() ][["firstName", "middleName", "lastName", "year", "points"]]
print(f"""\nThe highest number of points ({highest_point_data.points.item()}) was scored in {highest_point_data.year.item()} year by {highest_point_data.firstName.item()} {highest_point_data.middleName.item()} {highest_point_data.lastName.item()}""")

# 3. Produce a boxplot that shows the distribution of total points, total assists, and total rebounds
players_info["total_points"] = players_info.points + players_info.PostPoints
players_info["total_assists"] = players_info.assists + players_info.PostAssists
players_info["total_rebounds"] = players_info.rebounds + players_info.PostRebounds
sb.boxplot(label="", 
           data=players_info[["total_points", "total_assists", "total_rebounds"]])
plt.show()

# 4. Produce a plot that shows how the number of points scored has changed over time by showing the median of points scored per year, over time.
#    The x-axis is the year and the y-axis is the median number of points among all players for that year.
year_points = players_info[["points", "year"]].groupby("year").median()
sb.lineplot(label="", 
            data = year_points, 
            x="year", y="points")
plt.show()

# PART 2

# 1. Some players score a lot of points because they attempt a lot of shots. 
#    Among players that have scored a lot of points, are there some that are much more efficient (points per attempt) than others?
players_info["efficiency"] = players_info.points / (players_info.fgAttempted + players_info.ftAttempted + players_info.threeAttempted)
player_points_attempted = players_info[(players_info.fgAttempted + players_info.ftAttempted + players_info.threeAttempted) > 0][["playerID", "efficiency"]].groupby("playerID").mean()
top10_points_players = player_points_attempted.sort_values("efficiency", ascending=False).head()
top10_points_players = pd.merge(top10_points_players, master, how = "left", left_on = "playerID", right_on = "bioID")[["firstName","middleName", "lastName", "efficiency"]]
print(top10_points_players)

# 2. It seems like some players may excel in one statistical category, but produce very little in other areas. 
#    Are there any players that are exceptional across many categories?
exceptional_player = players_info[["playerID", "points", "rebounds", "assists", "steals", "blocks", "turnovers"]].groupby("playerID").mean().sort_values(["points","rebounds","assists","steals","blocks","turnovers"], ascending=False).head(10)
exceptional_player = pd.melt(exceptional_player.reset_index(), id_vars="playerID", var_name="category")
sb.barplot(label="", 
           data=exceptional_player,
           x="playerID", y="value", hue="category")
plt.show()

# 3. Much has been said about the rise of the three-point shot in recent years. 
#    It seems that players are shooting and making more three-point shots than ever. 
#    Recognizing that this dataset doesn't contain the very most recent data, do you see a trend of more three-point shots either across the league or among certain groups of players? 
#    Is there a point at which popularity increased dramatically?
players_info["total_threeAttempted"] = players_info.threeAttempted + players_info.PostthreeAttempted
players_info["total_threeMade"] = players_info.threeMade + players_info.PostthreeMade
threeData_per_year = players_info.groupby("lg")

# PART 3

# 1. Many sports analysts argue about which player is the GOAT (the Greatest Of All Time). 
#    Based on this data, who would you say is the GOAT?
#    Provide evidence to back up your decision.
players_stat = players_info[["playerID",  "points", "rebounds", "assists", "steals", "blocks", "turnovers"]].groupby("playerID").mean().sort_values(["points", "rebounds", "assists", "steals", "blocks", "turnovers"], ascending=False)
players_stat["GOAT_score"] = players_stat.sum(axis = 1)
top10_goat = players_stat.head(10)
top10_goat = pd.merge(top10_goat["GOAT_score"], master, how = "inner", left_on = "playerID", right_on = "bioID")[["firstName", "middleName", "lastName", "GOAT_score"]]
sb.barplot(label="", 
           data=top10_goat,
           x="lastName", y="GOAT_score")
plt.show()

# 2. The biographical data in this dataset contains information about home towns, home states, and home countries for these players. 
#    Can you find anything interesting about players who came from a similar location?
#print(master.columns)
location_group = players_info[["birthState", "points"]].groupby(["birthState"]).mean().sort_values("points", ascending=False).head(10)
#print(location_group)
sb.barplot(label="", 
           data=location_group.reset_index(), 
           x="birthState", y="points")
plt.show()
# 3. Find something else in this dataset that you consider interesting. 
#    Produce a graph to communicate your insight.
