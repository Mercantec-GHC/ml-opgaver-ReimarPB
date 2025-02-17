import numpy as np
import pandas as pd

dataframe = pd.DataFrame(data=np.random.randint(low=0, high=101, size=(3, 4)), columns=["Eleanor", "Chidi", "Tahani", "Jason"])

dataframe["Janet"] = dataframe["Tahani"] + dataframe["Jason"]

print(dataframe)
print()
print(dataframe['Eleanor'][1])

