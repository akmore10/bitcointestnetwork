import unittest
from scripts.codes.utils import *

class UnitTest(unittest.TestCase):
    def test_generatetoaddress(self):
        wallet_name = "akmore"
        address = "bcrt1qx0lr3equlemu3n2vq3kfp6tpzxunyyncntmsxg"
        blockcount = 5
        port = 18400
        result = generatetoaddress(wallet_name, address, blockcount, port)
        self.assertIsNotNone(result)
    
    def test_getBalance(self):
        wallet_name = "akmore"
        port = 18400
        result = getbalance(wallet_name , port)
        self.assertIsNotNone(result)

    def test_creatingwallet(self):
        name = "something"
        port = 18400

        result = creatingwallet(name,port)
        self.assertIsNotNone(result)
    
    def test_getnewaddress(self):
        wallet_name = "akmore"
        port = 18400

        result = getnewaddress(wallet_name,port)
        self.assertIsNotNone(result)
    

    def test_sendtoaddress(self):
        wallet_name = "colin"
        sendto = ""
        amount = 0
        port = 18400

        result = sendtoaddress(wallet_name,sendto,amount,port)
        self.assertIsNotNone(result)
    
    def test_getrawmempool(self):
        result = getrawmempool()
        self.assertIsNotNone(result)






