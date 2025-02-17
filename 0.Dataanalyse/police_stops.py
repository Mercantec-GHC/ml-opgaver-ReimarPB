import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

data = pd.read_csv('./Data/Police/police.csv')

data.dropna(how="any", subset=["driver_gender", "violation", "stop_outcome", "driver_age_raw"], inplace=True)

def get_age_group(age):
    if age >= 70: return "70+"
    if age >= 50: return "50-69"
    if age >= 30: return "30-49"
    if age >= 20: return "20-29"
    if age > 13: return "13-19"
    return "0-13"

data["stop_month"] = pd.to_datetime(data["stop_date"], format="%Y-%m-%d").dt.month
data["stop_year"] = pd.to_datetime(data["stop_date"], format="%Y-%m-%d").dt.year
data["age"] = 2021 - data["driver_age_raw"]
data["age_group"] = data.apply(lambda row: get_age_group(row["age"]), axis=1)

print(data.head(50))
print()
print(data.groupby(["age_group"]).size())
print()
print(data.groupby(["driver_gender"])["violation"].agg(pd.Series.mode))
print()
print(data.groupby(["driver_race", "driver_gender"]).size())

