# Chainlink Balance Monitor v0.1

Monitor your Chainlink nodes Ethereum balance on the primary and emergency funding addresses. Results print to console as well as get saved as timeseries JSON files for ingesting into your favorite SIEM/Metrics software. I personally am ingesting this into Splunk.

# Install

### Navigate to your Chainlink directory, clone the repo, set up your .env file
* cd ~/.chainlink
* git clone https://github.com/Alkhara/ChainlinkBalanceMonitor.git
* cd ChainlinkBalanceMonitor/
* nano .env

### Set your variables
* PROVIDER=https://mainnet.infura.io/v3/52929....
* CHAINLINK_NODE_ADDRESS=0xA8317D47....
* CHAINLINK_NODE_EF_ADDRESS=0x4C7DDEd...

### Build the docker
* docker build -t chainlinkbalancemonitor .

### Run it
* cd ~/.chainlink/ChainlinkBalanceMonitor && docker run --network {{your-docker-network-your-siem-is-in}} --hostname clbm -it --env-file=.env -v ~/.chainlink/ChainlinkBalanceMonitor/balance_tracker.json:/etc/balance_tracker.json chainlinkbalancemonitor



