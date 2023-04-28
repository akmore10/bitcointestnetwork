from utils import *


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
# print(generatetoaddress("akmore","bcrt1q50mdnh0davealarn4kl43edvv4gg8khh7uuxpf",50,18400))
# print(generatetoaddress("akmore","bcrt1q50mdnh0davealarn4kl43edvv4gg8khh7uuxpf",50,18400))
# print(generatetoaddress("colin","bcrt1qgr78dgnuk3ljarcyj57dqs4x0hzxgsv4fjlw4u",50,18401))
# print(generatetoaddress("colin","bcrt1qgr78dgnuk3ljarcyj57dqs4x0hzxgsv4fjlw4u",50,18401))
# print(generatetoaddress("amrutha","bcrt1qafkecw7tvjhaeagv5xx9mux5fqmzyks3c5ahxt",100,18402))
# print(generatetoaddress("amrutha","bcrt1qafkecw7tvjhaeagv5xx9mux5fqmzyks3c5ahxt",100,18402))
# print(generatetoaddress("ishan","bcrt1qwc79ndthkt6htd3ltzh5w833chrjdg44uffw8k",100,18400))
# print(generatetoaddress("ishan","bcrt1qwc79ndthkt6htd3ltzh5w833chrjdg44uffw8k",100,18400))

# print("Getting balance of akmore")
# print(getbalance("akmore",18400))
# print("Getting balance of colin")
# print(getbalance("colin",18401))
# print("Getting balance of amrutha")
# print(getbalance("amrutha",18402))
# print("Getting balance of ishan")
# print(getbalance("ishan",18400))

# for _ in range(50):
#     print("Sending 1 BTC to amrutha's wallet")
#     sendtoaddress("akmore","bcrt1qafkecw7tvjhaeagv5xx9mux5fqmzyks3c5ahxt",1,18400)
# print(getbalance("colin",18401))

# print("Getting the transaction id from Mempool")
result = getrawmempool(18400)
print(len(result))



# print(getRawTransactions("f7cd3697314df130b840ea6838cfa9acd4d60574f8fda77cddbdcc053e975eae"))

