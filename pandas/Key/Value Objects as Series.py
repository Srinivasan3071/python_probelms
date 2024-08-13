import pandas as pd

calories = [1, 2, 3]  # Convert the set to a list

myvar = pd.Series(calories)

# Dropping the entry at index 1
myvar = myvar.drop(1)

print(myvar)
