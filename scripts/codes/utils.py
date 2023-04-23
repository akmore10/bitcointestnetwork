import http.client
import json

address = {}
PORTS = (18400,18401,18402)
class WalletDetails:
    def __init__(self,name,address,port):
        self.name = name
        self.address = address
        self.port = port
    def __str__(self) -> str:
        return "Name : ",self.name + "\n" + "Address : " , self.address + "\n" + "Port : ",self.port + "\n"

def connection(payload,port,wallet_path = ""):
    conn = http.client.HTTPConnection("localhost", port)
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Authorization": "Basic Yml0Y29pbjpiaXRjb2lu",
    "Content-Type": "application/json" 
    }
    conn.request("POST", "/wallet/"+wallet_path, payload, headersList)
    response = conn.getresponse()
    result = response.read()
    return json.loads(result)

def creatingwallet(name,port):
    payload = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "createwallet",
    "params": {
        "wallet_name" : name
    }
    })

    result = connection(payload,port)
    return result
    

def getnewaddress(wallet_name,port):
    payload = json.dumps({
      "jsonrpc": "2.0",
      "id": 3,
      "method": "getnewaddress",
       "params": []
    })

    result = connection(payload,port,wallet_name)
    address[wallet_name] = result["result"]
    dumpaddress()
    return result

def getbalance(wallet_name,port):
    payload = json.dumps(
        {
          "jsonrpc": "2.0",
          "id": 3,
          "method": "getbalance",
           "params": []
        }
    )
    result = connection(payload,port,wallet_name)
    return result

def sendtoaddress(wallet_name, sendto, amount,port):
    payload = json.dumps(
        {
          "jsonrpc": "2.0",
          "id": 3,
          "method": "sendtoaddress",
           "params": {
             "amount":amount,
             "address": sendto,
             "fee_rate":2
           }
        }
    )

    result = connection(payload,port,wallet_name)
    print(result)

def getrawmempool(port=18400):
    payload = json.dumps(
        {
          "jsonrpc": "2.0",
          "id": 3,
          "method": "getrawmempool",
           "params": []
        }
    )

    result = connection(payload,port)
    return result["result"]

def generatetoaddress(wallet_name,address,blockcount,port):
    payload = json.dumps({
          "jsonrpc": "2.0",
          "id": 3,
          "method": "generatetoaddress",
           "params": [blockcount,address]
        }
    )
    result = connection(payload,port,wallet_name)
    return result

def dumpaddress():
    with open("address.txt", 'w') as f: 
        for key, value in address.items(): 
            f.write('%s:%s\n' % (key, json.dumps(value)))
    print("Written to file")

def getTransaction(wallet_name,hash,port):

    payload = json.dumps({
          "jsonrpc": "2.0",
          "id": 3,
          "method": "gettransaction",
           "params": [hash]
        }
    )
    result = connection(payload,port,wallet_name)
    return result
def listtransactions(wallet_name,port):
    payload = json.dumps({
          "jsonrpc": "2.0",
          "id": 3,
          "method": "listtransactions",
           "params": {
                "count" : 1000
           }
        }
    )
    result = connection(payload,port,wallet_name)
    return result