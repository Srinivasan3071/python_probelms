# import pandas as pd

# # data = {
# #   "calories": [420, 380, 390],
# #   "duration": [50, 40, 45]
# # }

# # #load data into a DataFrame object:
# # df = pd.DataFrame(data)

# # print(df) 
# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# index_labels = ["Day 1", "Day 2", "Day 3"]

# df = pd.DataFrame(data, index=index_labels)

# print(df)

import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.loc[0])

