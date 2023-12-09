import pandas as pd
import polars as pl
import great_tables as gt
from sportsdataverse import nba as nba


# Loading in nba schedule
df = nba.load_nba_schedule(seasons=2022, return_as_pandas=True)

# polar filter
# df.filter(pl.col("venue_full_name")== "Madison Square Garden")
team_attendance_avg = (
    df.groupby(["venue_full_name", "home_name"])
    .agg(Average_Attendance=("attendance", "mean"))
    .reset_index()
    .sort_values(by="Average_Attendance", ascending=False)
    .drop(columns="venue_full_name")
)

# dropping Team Lebron (its the last row in this dataframe)
team_attendance_avg = team_attendance_avg.iloc[:-1]
team_attendance_avg.shape  # checking shape of table
team_attendance_avg.dtypes  # checking column types

# creating gt table
(
    gt.GT(data=team_attendance_avg)
    .cols_label(home_name="Team", Average_Attendance="Avg Attendance")
    .fmt_number(columns="Average_Attendance", decimals=2)
)
