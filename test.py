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
    .drop(columns="venue_full_name", inplace=True)
)

# creating gt table
(
    gt.GT(data=team_attendance_avg)
    .cols_label(home_name="Team", Average_Attendance="Avg Attendance")
    .fmt_number(decimals=2)
)
