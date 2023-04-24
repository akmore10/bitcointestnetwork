from utils import *

# creating wallets
# creatingwallet("akmore",18400)
# print("Creating wallet akmore")
# creatingwallet("colin",18401)
# print("Creating wallet colin")
# creatingwallet("amrutha",18402)
# print("Creating wallet amrutha")
# creatingwallet("ishan",18400)
# print("Creating wallet ishan")

# getting public address
# print(getnewaddress("akmore",18400))
# print("Creating getnewaddress akmore")
# print(getnewaddress("colin",18401))
# print("Creating getnewaddress colin")
# print(getnewaddress("amrutha",18402))
# print("Creating getnewaddress amrutha")
# print(getnewaddress("ishan",18400))
# print("Creating getnewaddress ishan")

#generating 
# print(generatetoaddress("akmore","bcrt1qd8ynd8whlj33yaem2qr2n33azytrd52fph4mha",50,18400))
# print(generatetoaddress("akmore","bcrt1qd8ynd8whlj33yaem2qr2n33azytrd52fph4mha",50,18400))
# print(generatetoaddress("colin","bcrt1qt7ewfj9dvq6saxa78cdgjgucprf2aalu489str",50,18401))
# print(generatetoaddress("colin","bcrt1qt7ewfj9dvq6saxa78cdgjgucprf2aalu489str",50,18401))
# print(generatetoaddress("amrutha","bcrt1q93l0rtuny75rrc5x0fr54d0qtxflrd7r9cqd8w",100,18402))
# print(generatetoaddress("amrutha","bcrt1q93l0rtuny75rrc5x0fr54d0qtxflrd7r9cqd8w",100,18402))
# print(generatetoaddress("ishan","bcrt1q8s5gm93qqwxl8z5dkexagaw76qnwvw6h27cqm0",100,18400))
# print(generatetoaddress("ishan","bcrt1q8s5gm93qqwxl8z5dkexagaw76qnwvw6h27cqm0",100,18400))

# print("Getting balance of akmore")
# print(getbalance("akmore",18400))
# print("Getting balance of colin")
# print(getbalance("colin",18401))
# print("Getting balance of amrutha")
# print(getbalance("amrutha",18402))
# print("Getting balance of ishan")
# print(getbalance("ishan",18400))

# for _ in range(100):
#     print("Sending 1 BTC to colin's wallet")
#     sendtoaddress("akmore","bcrt1qt7ewfj9dvq6saxa78cdgjgucprf2aalu489str",1,18400)
# print(getbalance("colin",18401))
# print("Getting the transaction id from Mempool")
# result = getrawmempool(18401)
# for res in result:
#     print(res)

print("Getting Transaction from the transaction id :")
print(getTransaction("akmore","4f99b42d2deda7ef7e670e133afb56f627e79b6e3b6428c9616cc63b3eeedfec",18400))

