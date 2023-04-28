from utils import getrawmempool,getRawTransactions
import pandas as pd

data = []
result = getrawmempool(18400)
for res in result:
    data.append(getRawTransactions(res))
df = pd.DataFrame(data)
# print(df.columns)
df = df.drop("vin",axis=1)
df.to_csv("transactions.csv",index=False)

# result = result["result"]

# for res in result:
#     if res["category"] == "generate":
#         continue
#     data.append(res)
# df = pd.DataFrame(data)

# df.to_csv("transactions.csv",index=False)