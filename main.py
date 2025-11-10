from data_loader import load_data
from analysis import dropout_rate, dropout_cause

if __name__ == "__main__":
  data = load_data()
  rate = dropout_rate(data)
  causes = dropout_cause(data)
  print(f"Dropout rate: {rate}%")
  print(f"Dropout causes: {causes}")
