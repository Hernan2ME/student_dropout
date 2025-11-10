import pandas as pd

def dropout_rate(df):
  total = len(df)
  dropped = len(df[df["status"] == "Dropped"])
  rate = dropped / total * 100


  return round(rate, 2)

def dropout_cause(df):
    causa = df["cause"].value_counts().idxmax()

    return causa

