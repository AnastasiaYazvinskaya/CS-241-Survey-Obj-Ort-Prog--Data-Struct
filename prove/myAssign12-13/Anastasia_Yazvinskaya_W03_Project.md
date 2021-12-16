# 13: Prove: Data Analysis

__Author: Anastasia Yazvinskaya__

## Elevator pitch

_For this Assignment I work with a dataset of NBA basketball data and analyze it using pandas._

## Part 1
### QUESTION 1
_Calculate the mean and median number of points scored. (In other words, each row is the amount of points a player scored during a particular season. Calculate the median of these values. The result of this is that we have the median number of points players score each season.)_
 - Output:
    Mean number of points per season:
    492.13
    Median number of points per season:
    329.00
 - 
 - Code:
    ```
    mean = players_data.points.mean()
    median = players_data.points.median()
    print(f"""1.
    Mean number of points per season:\n{mean:.2f}
    Median number of points per season:\n{median:.2f}""")
    ```
### QUESTION 2
_Determine the highest number of points recorded in a single season. Identify who scored those points and the year they did so._
 - Output:

 - 
 - Code:
    ```
    top10_points = players_data[["playerID", "year", "points"]].sort_values("points", ascending=False).head(10)
    print(f"""\n2.
    TOP-10 players who scores the hidhest number of points in a single season:\n {top10_points}""")
    ```
### QUESTION 3
_Produce a boxplot that shows the distribution of total points, total assists, and total rebounds (each of these three is a separate box plot, but they can be on the same scale and in the same graphic)._
 - Chart:
 ![](Part1dot3.png)
 - 
 - Code:
    ```
    sb.boxplot(data=players_data[["points", "assists", "rebounds"]])
    plt.show()
    ```
### QUESTION 4
_Produce a plot that shows how the number of points scored has changed over time by showing the median of points scored per year, over time. The x-axis is the year and the y-axis is the median number of points among all players for that year._
 - Chart:
 ![](Part1dot4.png)
 - 
 - Code:
    ```
    median_points = players_data[["points", "year"]].groupby("year").median()
    sb.scatterplot(data = median_points, x="year", y="points")
    plt.show()
    ```

## Part 2
### QUESTION 1
_Some players score a lot of points because they attempt a lot of shots. Among players that have scored a lot of points, are there some that are much more efficient (points per attempt) than others?_
 - Output:
 
 - 
 - Code:
    ```
    # Field goal
    players_data["fgEfficiency"] = players_data.fgMade / players_data.fgAttempted
    players_data = players_data[(players_data.fgAttempted > 0) & (players_data.fgEfficiency <= 1)]
    # Free throw
    players_data["ftEfficiency"] = players_data.ftMade / players_data.ftAttempted
    players_data = players_data[(players_data.ftAttempted > 0) & (players_data.ftEfficiency <= 1)]
    # Three throw
    players_data["threeEfficiency"] = players_data.threeMade / players_data.threeAttempted
    players_data = players_data[(players_data.threeAttempted > 0) & (players_data.threeEfficiency <= 1)]
    sb.boxplot(data=players_data[["fgEfficiency", "ftEfficiency", "threeEfficiency"]])
    plt.show()
    ```
### QUESTION 2
_It seems like some players may excel in one statistical category, but produce very little in other areas. Are there any players that are exceptional across many categories?_
 - Chart:
 ![](Part2dot2.png)
 - 
 - Code:
    ```
    
    ```
### QUESTION 3
_Much has been said about the rise of the three-point shot in recent years. It seems that players are shooting and making more three-point shots than ever. Recognizing that this dataset doesn't contain the very most recent data, do you see a trend of more three-point shots either across the league or among certain groups of players? Is there a point at which popularity increased dramatically?_
 - Chart:
 ![](Part2dot3.png)
 - 
 - Code:
    ```
    
    ```

## Part 3
### QUESTION 1
_Many sports analysts argue about which player is the GOAT (the Greatest Of All Time). Based on this data, who would you say is the GOAT? Provide evidence to back up your decision._
 - Chart:
 ![](Part3dot1.png)
 - 
 - Code:
    ```
    
    ```
### QUESTION 2
_The biographical data in this dataset contains information about home towns, home states, and home countries for these players. Can you find anything interesting about players who came from a similar location?_
 - Chart:
 ![](Part3dot2.png)
 - 
 - Code:
    ```
    
    ```
### QUESTION 3
_Find something else in this dataset that you consider interesting. Produce a graph to communicate your insight._
 - Chart:
 ![](.png) 
 - 
 - Code:
    ```
    
    ```

## APPENDIX A (PYTHON SCRIPT)

```
# Import pandas, altair and numpy libraries
import pandas as pd
import altair as alt
import numpy as np

# Save data to the local file system
alt.data_transformers.enable('json')

# Create a data frame based on existing data
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
dat = pd.read_csv(url)
dat

# 1 Grand Question
# How does your name at your birth year compare to its use historically?

# Table just for name Anastasia
t_name = dat.query('name == "Anastasia"')
# Findig a line where name is Anastasia and the year is 1998
name_in_1998 = dat.query('name == "Anastasia" & year == 1998')
# Base chart which will show how the name was used over time
base = (alt.Chart(t_name, title="How the name (Anastasia) was used over time")
    .encode(
        alt.X('year'),
        alt.Y('Total')
    )
    .mark_line(color="red")
)
# Bar for the 1998 year
bar = (alt.Chart(name_in_1998)
    .encode(
        alt.X('year'),
        alt.Y('Total', scale = alt.Scale(domain = (0, 1600)))
    )
    .mark_bar(color="green")
)
# Merging charts
chart1 = bar + base
chart1

# 2 Grand Question
# If you talked to someone named Brittany on the phone, what is your guess of their age? What ages would you not guess?

# Table just for name Brittany
t_name = dat.query('name == "Brittany"')
# Base chart which will show how the name was used over time
base = (alt.Chart(t_name, title="How the name (Brittany) was used over time")
    .encode(
        alt.X('year'),
        alt.Y('Total')
    )
    .mark_line(color="red")
)
base

# 3 Grand Question
# Mary, Martha, Peter, and Paul are all Christian names. From 1920 - 2000, compare the name usage of each of the four names.

# Table for names Mary, Martha, Peter, and Paul
t_name = dat.query('(name == "Mary" | name == "Martha" | name == "Peter" | name == "Paul") & year >=1920 & year <=2000')
# Base chart which will show how the names were used over time
base = (alt.Chart(t_name, title="How the names (Mary, Martha, Peter, Paul) were used over time (1920-2000)")
    .encode(
        alt.X('year', scale = alt.Scale(domain = (1920, 2000))),
        alt.Y('Total'),
        alt.Color('name')
    )
    .mark_line()
)
base

# 4 Grand Question
# Think of a unique name from a famous movie. Plot that name and see how increases line up with the movie release.

# Table for name Dominic
t_name = dat.query('name == "Dominic"')
# Base chart which will show how the name was used over time
base = (alt.Chart(t_name, title="How the name (Dominic) was used over time")
    .encode(
        alt.X('year'),
        alt.Y('Total')
    )
    .mark_line()
)
# Table from 2001 year
t_name = dat.query('year >= 2001')
line = (alt.Chart(t_name)
    .encode(
        alt.X('year'),
        alt.Y('Total')
    )
    .mark_line(color="red")
)

# Merging charts
chart2 = base + line
chart2
```