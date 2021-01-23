from web3 import Web3
from dotenv import load_dotenv
import json
import time
import os


load_dotenv()


#######################################
# Chainlink Node Address Monitor v0.1 #
#                                     #
# This python script will create a    #
# time series json log of your two    #
# balances so it can be indexed in a  #
# logging solution of your choice. I  #
# personally built this to ingest to  #
# Splunk.                             #
#                                     #
#                                     #
# Happy Linking!                      #
# Alkhara                             #
#######################################


# Check for required .env variables and if
# they don't exist, prompt for them.

provider = os.getenv('PROVIDER', 'blank')
cl_node_addr = os.getenv('CHAINLINK_NODE_ADDRESS', 'blank')
cl_ef_node_addr = os.getenv('CHAINLINK_NODE_EF_ADDRESS', 'blank')


if provider == 'blank':
        print('Your .env file is missing a value for PROVIDER=')
        print('Enter your provider: ')
        provider = input()

if cl_node_addr == 'blank':
        print('Your .env file is missing a value for CHAINLINK_NODE_ADDRESS=')
        print('Enter your Chainlink Node Address:')
        cl_node_addr = input()

if cl_ef_node_addr == 'blank':
        print('Your .env file is missing a value for CHAINLINK_NODE_EF_ADDRESS=')
        print('Enter your Chainlink Emergency Funding Address:')
        cl_node_ef_addr = input()


# Connect to your Ethereum Provider

w3 = Web3(Web3.HTTPProvider(provider))

# Check Primary Address

def get_cl_node_balance():
        ts = time.time()
        cl_node_balance = w3.eth.get_balance(cl_node_addr)
        x = {
        "ts": str(ts),
        "address": cl_node_addr,
        "balance": cl_node_balance,
        "type": "primary"
        }
        ts_cl_addr = json.dumps(x)
        print(ts_cl_addr)
        with open("/path/to/store/file/balance_tracker.json", "a") as data:
                data.write(ts_cl_addr)
                data.close()

# Check Emergency Funding Address

def get_cl_ef_node_balance():
        ts = time.time()
        cl_ef_node_balance = w3.eth.get_balance(cl_ef_node_addr)
        x = {
        "ts": str(ts),
        "address": cl_ef_node_addr,
        "balance": cl_ef_node_balance,
        "type": "emergency"
        }
        ts_cl_ef_addr = json.dumps(x)
        print(ts_cl_ef_addr)
        with open("/path/to/store/file/balance_tracker.json", "a") as data:
                data.write(ts_cl_ef_addr)
                data.close()

# Check each every 5 seconds

def looper():
        while True:
                get_cl_node_balance()
                time.sleep(15)
                get_cl_ef_node_balance()
                time.sleep(15)

# Forever

def main():
        looper()

# GO

if __name__ == "__main__":
        main()