import pandas as pd
data = {
  "a": {
    "Duration": 60,
    "Pulse": 110
  },
  "b": {
    "Duration": 60,
    "Pulse": 117
  },
  "c": {
    "Duration": 60,
    "Pulse": 103
  },
  "v": {
    "Duration": 45,
    "Pulse": 109
  },
  "n": {
    "Duration": 60,
    "Pulse": 102
  }
}
df = pd.DataFrame(data) 
print(df)
