from utils import listtransactions
import pandas as pd
data = []
result = listtransactions("akmore",18400)
result = result["result"]

for res in result:
    if res["category"] == "generate":
        continue
    data.append(res)
df = pd.DataFrame(data)

df.to_csv("transactions.csv",index=False)