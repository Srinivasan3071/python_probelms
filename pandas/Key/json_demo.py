import pandas as pd
data = {
  "a": {
    "Duration": 60,
    "Pulse": 110,
    "Maxpulse": 130,
    "Calories": 409.1
  },
  "b": {
    "Duration": 60,
    "Pulse": 117,
    "Maxpulse": 145,
    "Calories": 479.0
  },
  "c": {
    "Duration": 60,
    "Pulse": 103,
    "Maxpulse": 135,
    "Calories": 340.0
  },
  "v": {
    "Duration": 45,
    "Pulse": 109,
    "Maxpulse": 175,
    "Calories": 282.4
  },
  "n": {
    "Duration": 60,
    "Pulse": 102,
    "Maxpulse": 148,
    "Calories": 406.0
  }
}
df = pd.DataFrame(data).T # Transpose to match the original format

print(df)
